using System.Collections;
using System.Collections.Generic;
using UnityEngine;


[RequireComponent(typeof(Rigidbody2D))]
public class Move2d : MonoBehaviour
{
    [Header("Рух")]
    public float moveH;
    public float moveV;
    [SerializeField] float moveSpeed = 1.0f;

    [Header("Стрибок")]
    [SerializeField] float jumpSpeed = 1.0f;

    [Header("Кнопки керування")]
    [SerializeField] ButtonHold buttonJump;
    [SerializeField] ButtonHold buttonLeft;
    [SerializeField] ButtonHold buttonRight;

    [Header("Перевірка землі")]
    [SerializeField] GroundChecker groundChecker;

    Rigidbody2D rb;

    void Start(){
        rb = GetComponent<Rigidbody2D>();
    }

    void Update(){}

    void FixedUpdate(){
        moveH = rb.velocity.x;
        moveV = rb.velocity.y;

        bool leftPressed = Input.GetKey(KeyCode.A) || Input.GetKey(KeyCode.LeftArrow) || (buttonLeft != null && buttonLeft.press);
        bool rightPressed = Input.GetKey(KeyCode.D) || Input.GetKey(KeyCode.RightArrow) || (buttonRight != null && buttonRight.press);
        bool jumpPressed = Input.GetKey(KeyCode.W) || Input.GetKey(KeyCode.UpArrow) || Input.GetKey(KeyCode.Space) || (buttonJump != null && buttonJump.press);

        if (leftPressed) {
            moveH = -moveSpeed;
        } else if (rightPressed) {
            moveH = moveSpeed;
        }

        rb.velocity = new Vector2(moveH, moveV);

        if (jumpPressed && groundChecker.onGround) {
            rb.AddForce(Vector2.up * jumpSpeed, ForceMode2D.Impulse);
        }
    }
}
