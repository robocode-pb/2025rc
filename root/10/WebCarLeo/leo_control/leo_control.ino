// LEO - ARDUINO MEGA or MEGA 2560
#include <Servo.h> // Include the Servo library
Servo servo;


// En-enable-ввімкнути 
// A-лівий мотор   B-правий мотор
// b-назад         f-вперед
const int motorPinEnA  = 5;
const int motorPinA1   = 6;
const int motorPinA2   = 7;
const int motorPinB1   = 8;
const int motorPinB2   = 9;
const int motorPinEnB  = 10;

const int servoPin = 11;

void setup() {
  Serial.begin(9600);
  Serial.println("i am Leo");
  Serial1.begin(9600);
    servo.attach(servoPin);
    
    
    pinMode(motorPinEnA, OUTPUT); 
    pinMode(motorPinA1, OUTPUT);
    pinMode(motorPinA2, OUTPUT);
    pinMode(motorPinB1, OUTPUT);
    pinMode(motorPinB2, OUTPUT);
    pinMode(motorPinEnB, OUTPUT);

    pinMode(26, OUTPUT); // лівий поворотник світлодіод 
    pinMode(27, OUTPUT); // правий поворотник світлодіод 

}

// виконуюча функція, то повертає пустоту-void
void control(int angle, int l, int r, int speed) {
    servo.write(angle);
    analogWrite(motorPinEnA, speed);  // швидкість лівого
    digitalWrite(motorPinA1,  l);  // ліве назад
    digitalWrite(motorPinA2, not l);      // ліве вперед
    digitalWrite(motorPinB1,  r);  // праве назад
    digitalWrite(motorPinB2, not r);      // праве вперед
    analogWrite(motorPinEnB, speed);  // швидкість правого

    servo.write(angle); // Set the servo to the specified angle
}

void loop() {
  if (Serial1.available())
  {
    char data = Serial1.read();
    Serial.println(data);
             if(data == 'B') control(90, 1, 1, 150);
        else if(data == 'F') control(90, 0, 0, 150); // назад
        else if(data == 'L') control(10, 1, 1, 150); // вліво
        else if(data == 'R') control(170, 1, 1, 150); // вправо
        else if(data == 'S') control(90, 0, 0, 0); // зупинка
    }
}
