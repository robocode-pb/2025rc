#include "Cam.h"

const char* ssid     = "Robocode_5G";
const char* password = "19robocode19";


const int motorPinA1  = 4;  // Motor A IN1
const int motorPinA2  = 2;  // Motor A IN2
const int motorPinB1  = 14; // Motor B IN1
const int motorPinB2  = 15; // Motor B IN2
const int LeoSerialTX = 13;

// HTML + обробка команд
String handleCommand(String cmd) {
  Serial.print("CMD: ");
  Serial.println(cmd);
 // motor(cmd);

       if(cmd=="F") leo.println('F');
  else if(cmd=="B") leo.println('B');
  else if(cmd=="L") leo.println('L');
  else if(cmd=="R") leo.println('R');
  else if(cmd=="S") leo.println('S');
  else if(cmd=="Q") leo.println('Q'); // поворотник правий
  else if(cmd=="E") leo.println('E'); // поворотник лівий
  
  return htmlControl;
}

void setup() {
  Serial.begin(115200);
  leo.begin(9600, SERIAL_8N1, -1, LeoSerialTX);

  CamBegin();
  WiFiBegin(ssid, password);
  startCameraServer();
  // Set motor pins as outputs
  pinMode(motorPinA1, OUTPUT);
  pinMode(motorPinA2, OUTPUT);
  pinMode(motorPinB1, OUTPUT);
  pinMode(motorPinB2, OUTPUT);

//  // Set up PWM channels using the new LEDC API
//  ledcAttach(motorPinA1, 5000, 8); // Motor A IN1
//  ledcAttach(motorPinA2, 5000, 8); // Motor A IN2
//  ledcAttach(motorPinB1, 5000, 8); // Motor B IN1
//  ledcAttach(motorPinB2, 5000, 8); // Motor B IN2
}

void motor(String cmd) {
  int s = 100;
       if (cmd == "F") setMotor(0,1,1,0);
  else if (cmd == "B") setMotor(s,0,0,s);
  else if (cmd == "L") setMotor(0,0,0,s);
  else if (cmd == "R") setMotor(s,0,0,0);
  else if (cmd == "S") setMotor(0,0,0,0);

}

void setMotor(int a1, int a2, int b1, int b2){
    digitalWrite(motorPinA1, a1);
    digitalWrite(motorPinA2, a2);
    digitalWrite(motorPinB1, b1);
    digitalWrite(motorPinB2, b2);
//    ledcWrite(motorPinA1, a1); // Motor A IN1
//    ledcWrite(motorPinA2, a2); // Motor A IN2
//    ledcWrite(motorPinB1, b1); // Motor B IN1
//    ledcWrite(motorPinB2, b2); // Motor B IN2
}

void loop() { 
    digitalWrite(33, !digitalRead(33));
    delay(100);
}
