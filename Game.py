// Attach
to
Player
prefab
using
UnityEngine;

[RequireComponent(typeof(CharacterController))]
public


class PlayerController: MonoBehaviour


{
    [Header("Movement")]
public
float
moveSpeed = 5
f;
public
float
rotationSpeed = 10
f;
public
float
jumpHeight = 2
f;
public
float
gravity = -9.81
f;

private
CharacterController
controller;
private
Vector3
velocity;
private
Transform
cameraMain;

void
Start()
{
    controller = GetComponent < CharacterController > ();
cameraMain = Camera.main.transform;
}

void
Update()
{
    HandleMovement();
}

void
HandleMovement()
{
    float
h = Input.GetAxis("Horizontal");
float
v = Input.GetAxis("Vertical");
Vector3
move = cameraMain.forward * v + cameraMain.right * h;
move.y = 0;

if (move.magnitude > 0.1f)
{
    Quaternion
targetRotation = Quaternion.LookRotation(move);
transform.rotation = Quaternion.Slerp(transform.rotation, targetRotation, rotationSpeed * Time.deltaTime);
}

if (controller.isGrounded & & velocity.y < 0)
velocity.y = -2f;

if (Input.GetButtonDown("Jump") & & controller.isGrounded)
velocity.y = Mathf.Sqrt(jumpHeight * -2f * gravity);

controller.Move(move * moveSpeed * Time.deltaTime);
velocity.y += gravity * Time.deltaTime;
controller.Move(velocity * Time.deltaTime);
}
}
// Attach
to
MusicManager
GameObject
using
FMODUnity;
using
UnityEngine;

public


class MusicManager: MonoBehaviour


{
    [EventRef]
public
string
musicEventPath = "event:/Music/Exploration";
private
FMOD.Studio.EventInstance
musicInstance;

void
Start()
{
    musicInstance = RuntimeManager.CreateInstance(musicEventPath);
musicInstance.start();
}

public
void
SetIntensity(float
intensity) // 0 - 1
range
{
    musicInstance.setParameterByName("Intensity", intensity);
}

void
OnDestroy()
{
    musicInstance.stop(FMOD.Studio.STOP_MODE.ALLOWFADEOUT);
musicInstance.release();
}
}
Assets/
├── Scripts/
│   ├── Player/
│   ├── Enemies/
│   └── Systems/
├── Art/
│   ├── Characters/
│   ├── Environments/
│   └── FX/
├── Audio/
│   ├── FMOD/
│   └── SFX/
└── Prefabs/