using UnityEngine;

[RequireComponent(typeof(Rigidbody2D))]
public class PlayerController : MonoBehaviour
{
    [Header("Move")]
    public float moveSpeed = 80f;
    public float acceleration = 0.2f;
    public float deceleration = 0.15f;

    [Header("Jump")]
    public float jumpForce = 6f;
    public float coyoteTime = 0.1f;
    public float jumpBuffer = 0.1f;
    public Transform groundCheck;
    public LayerMask groundMask;
    public Vector2 groundCheckSize = new(0.4f, 0.1f);

    [Header("Wall")]
    public Transform wallCheck;
    public Vector2 wallCheckSize = new(0.1f, 0.8f);
    public float wallSlideSpeed = 2f;
    public float wallJumpForce = 7f;

    private Rigidbody2D rb;
    private float coyoteCounter, jumpBufferCounter;
    private bool facingRight = true;
    private float moveInput;

    void Awake() => rb = GetComponent<Rigidbody2D>();

    void Update()
    {
        moveInput = Input.GetAxisRaw("Horizontal");

        // Coyote & jump buffer
        if (IsGrounded()) coyoteCounter = coyoteTime;
        else coyoteCounter -= Time.deltaTime;

        if (Input.GetButtonDown("Jump")) jumpBufferCounter = jumpBuffer;
        else jumpBufferCounter -= Time.deltaTime;

        // Wall slide
        if (!IsGrounded() && IsTouchingWall() && rb.velocity.y < 0)
            rb.velocity = new Vector2(rb.velocity.x, -wallSlideSpeed);

        // Jump
        if (jumpBufferCounter > 0 && coyoteCounter > 0)
        {
            rb.velocity = new Vector2(rb.velocity.x, jumpForce);
            jumpBufferCounter = 0;
            coyoteCounter = 0;
        }
        // Wall jump
        else if (jumpBufferCounter > 0 && IsTouchingWall())
        {
            rb.velocity = new Vector2(-moveInput * wallJumpForce, jumpForce);
            jumpBufferCounter = 0;
        }

        // Flip
        if (moveInput > 0 && !facingRight || moveInput < 0 && facingRight)
        {
            facingRight = !facingRight;
            transform.Rotate(0, 180, 0);
        }
    }

    void FixedUpdate()
    {
        float targetSpeed = moveInput * moveSpeed;
        float accel = Mathf.Abs(targetSpeed) > 0.01f ? acceleration : deceleration;
        rb.velocity = new Vector2(
            Mathf.MoveTowards(rb.velocity.x, targetSpeed, accel * Time.fixedDeltaTime * 100f),
            rb.velocity.y);
    }

    bool IsGrounded() => Physics2D.OverlapBox(groundCheck.position, groundCheckSize, 0, groundMask);
    bool IsTouchingWall() => Physics2D.OverlapBox(wallCheck.position, wallCheckSize, 0, groundMask);

    void OnDrawGizmosSelected()
    {
        Gizmos.color = Color.green;
        Gizmos.DrawWireCube(groundCheck.position, groundCheckSize);
        Gizmos.color = Color.red;
        Gizmos.DrawWireCube(wallCheck.position, wallCheckSize);
    }
}