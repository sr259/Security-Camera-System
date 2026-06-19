#include <Adafruit_STHS34PF80.h>
#include <SoftwareSerial.h>
#include <string.h>

//Bluetooth
uint8_t TX = 3;
uint8_t RX = 4;
SoftwareSerial bt(RX, TX);
const uint8_t BT_STATE = 5;
bool connectedBT = false;

//Adafruit_STHS34PF80
Adafruit_STHS34PF80 motion;
volatile bool sensorInterrupt = false;
uint8_t INT = 2;

void motionISR(){
  sensorInterrupt = true;
}


void setup() {
  Serial.begin(9600);
  bt.begin(9600);

  //Check to see if STHS sensor is acitve
  if(!motion.begin()){
    Serial.println("Could not find a valid STHSP34PF80 sensor, check your wiring");
    while(1) delay(10);
  }
  pinMode(INT,INPUT);
  Serial.println("STHSP34PF80 found!");
  motion.setIntSignal(STHS34PF80_INT_OR);
  motion.setIntMask(0b010); //
  attachInterrupt(digitalPinToInterrupt(INT), motionISR, RISING);
  pinMode(BT_STATE, INPUT);

}

void loop() {
    // check BT Status
    connectedBT = digitalRead(BT_STATE);

    if(sensorInterrupt){
      sensorInterrupt = false;
      if(motion.isMotion()){
          if(connectedBT){
            bt.println("Motion Detected");
          }else{
            Serial.println("Bluetooth not connected");
          }
      }
    }
}

