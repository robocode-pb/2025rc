
1. Для чого цей прапорець ?
   
![file_1669312868307](https://github.com/user-attachments/assets/6b49aca1-9db6-447d-b7c2-1b25eba596ce)

2. Що робить даний код?
``` c#
if (Input.GetKey (KeyCode. UpArrow)) {
  motor.motorSpeed = 1000;
  frontWheel.motor = motor;
  backWheel.motor = motor;
  backWheel.useMotor = true;
  frontWheel.useMotor = true;
}
```

3. Яка різниця `FixedUpdate()` та `Update()` ?

4. Що відбудеться?
``` c#
private void Start() {
  isGround = true;
  if(!isGround) {
    Debug.Log("On Ground!");
  }  else {
    Debug.Log("Fly");
  }
}
```

5. Зі збільшенням `pixel per unit` що станеться з спрайтом?

![image](https://github.com/user-attachments/assets/010bd258-64b5-4ada-8262-b2d104b69fb0)

6. Яка різниця між наступними функціями?
``` c#
OnTriggerStay2D
OnTriggerEnter2D
OnTriggerExit2D
```

7. За що відповідає кожний параметр?

![image](https://github.com/user-attachments/assets/76b06598-e2a0-491f-9d4d-875996534314)
