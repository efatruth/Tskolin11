using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;

public class PlayerMovement : NetworkBehaviour {

    public float speed = 6f;
    public float gravity = -9.8f;

    [SerializeField] private AnimationCurve jumpFallOff;
    [SerializeField] private float jumpMultiplier;
    [SerializeField] private KeyCode jumpKey;
     
    private bool isJumping;

    private CharacterController _charCont;
	// Use this for initialization
	void Awake () {
        _charCont = GetComponent<CharacterController>();
	}
	
	// Update is called once per frame
	void FixedUpdate () {

        // Since update is running on ALL computers, this makes it so that other players cannot interact with objects that they do not own.
        if (hasAuthority == false)
        {
            return;
        }

        float deltaX = Input.GetAxis("Horizontal") * speed;
        float deltaZ = Input.GetAxis("Vertical") * speed;
        Vector3 movement = new Vector3(deltaX, 0, deltaZ);
        movement = Vector3.ClampMagnitude(movement, speed);

        movement.y = gravity;

        movement *= Time.deltaTime;
        movement = transform.TransformDirection(movement);
        _charCont.Move(movement);

        JumpInput();
	}

    void JumpInput()
    {
        if (Input.GetKeyDown(jumpKey) && !isJumping)
        {
            isJumping = true;
            StartCoroutine(JumpEvent());
        }
    }

    IEnumerator JumpEvent()
    {
        _charCont.slopeLimit = 90.0f;
        float timeInAir = 0.0f;

        do
        {
            float jumpForce = jumpFallOff.Evaluate(timeInAir);
            _charCont.Move(Vector3.up * jumpForce * jumpMultiplier * Time.deltaTime);
            timeInAir += Time.deltaTime;

            yield return null;
        } while (!_charCont.isGrounded && _charCont.collisionFlags != CollisionFlags.Above);
        _charCont.slopeLimit = 45.0f;
        isJumping = false;
    }
}
