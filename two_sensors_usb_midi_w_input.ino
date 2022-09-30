/*
 * MIDIUSB_test.ino
 *
 * Created: 4/6/2015 10:47:08 AM
 * Author: gurbrinder grewal
 * Modified by Arduino LLC (2015)
 */ 

#include "MIDIUSB.h"
const int echoPin = 4;
const int trigPin = 5;

const int echoPin2 = 6;
const int trigPin2 = 7;
// First parameter is the event type (0x09 = note on, 0x08 = note off).
// Second parameter is note-on/note-off, combined with the channel.
// Channel can be anything between 0-15. Typically reported to the user as 1-16.
// Third parameter is the note number (48 = middle C).
// Fourth parameter is the velocity (64 = normal, 127 = fastest).

void noteOn(byte channel, byte pitch, byte velocity) {
  midiEventPacket_t noteOn = {0x09, 0x90 | channel, pitch, velocity};
  MidiUSB.sendMIDI(noteOn);
}

void noteOff(byte channel, byte pitch, byte velocity) {
  midiEventPacket_t noteOff = {0x08, 0x80 | channel, pitch, velocity};
  MidiUSB.sendMIDI(noteOff);
}

void pitchBend(int channel,int value) {
      if (value > 0x3FFF) {
        value = 0x3FFF;
    }
    //byte status_byte = 0xE0;
    //byte lsb = value & 0x7f;
    //byte msb = value >> 7;
    //midiEventPacket_t event = {0x0B, 0xE0 | channel, control, value};
    //midiEventPacket_t event = {status_byte << 16 | msb | (lsb << 8)};
  //MidiUSB.sendMIDI(event);
  byte lowValue = value & 0x7F;
  byte highValue = value >> 7;
  midiEventPacket_t event = {0x0E, 0xE0 | channel, lowValue, highValue};
  MidiUSB.sendMIDI(event);
  MidiUSB.flush();
}


void setup() {
  Serial.begin(115200);
    pinMode(echoPin, INPUT);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin2, INPUT);
  pinMode(trigPin2, OUTPUT);
  //noteOff(0, 60, 40);
  //noteOn(0, 60, 40);
}

// First parameter is the event type (0x0B = control change).
// Second parameter is the event type, combined with the channel.
// Third parameter is the control number number (0-119).
// Fourth parameter is the control value (0-127).

void controlChange(byte channel, byte control, byte value) {
  midiEventPacket_t event = {0x0B, 0xB0 | channel, control, value};
  MidiUSB.sendMIDI(event);
  MidiUSB.flush();
}

float readSensorDataVolume(){
  digitalWrite(trigPin, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);  
  int distance = pulseIn(echoPin, HIGH)/58;  //58 Equivalent to (340m/s*1us)/2
  int correctedInput = (min(distance,100)*1.27);
  return correctedInput;
}


float readSensorDataPitch(){
  digitalWrite(trigPin2, LOW); 
  delayMicroseconds(2);
  digitalWrite(trigPin2, HIGH); 
  delayMicroseconds(10);
  digitalWrite(trigPin2, LOW);  
  unsigned int distance = pulseIn(echoPin2, HIGH)/58;  //58 Equivalent to (340m/s*1us)/2
  unsigned int correctedInput = ((0 - (min(distance,100))) * 160);
  return correctedInput; 
}

void loop() {
 // int i = 0;
  //if i = 0
 // unsigned int volumeValue = readSensorDataVolume();
 // unsigned int pitchValue = readSensorDataPitch();

     pitchBend(0,pitchValue);
   MidiUSB.flush();
  controlChange(0x00,7,volumeValue);
  MidiUSB.flush();
  delay(10);
   //pitchBend(0,100);
  MidiUSB.flush();
   delay(10);
    //MidiUSB.flush();
  //noteOn(0, 48, 64); 
}
