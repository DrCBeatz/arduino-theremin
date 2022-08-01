#include <iostream>

using namespace std;

int valueToChannelVolumeMsg(int valueByte) {
    if (valueByte < 0) {
        valueByte = 0;
    }

    // max channel volume value is 127
    if (valueByte > 0x7f) {
        valueByte = 0x7f;
    }
    int statusByte = 0xB0;
    int ccByte = 0x07;
    return statusByte << 16 | valueByte | (ccByte << 8);
}

int valueToPitchBendMsg(int value) {
    if (value < 0) {
        value = 0;
    }
    
    // max pitchbend value is 16383
    if (value > 0x3FFF) {
        value = 0x3FFF;
    }

    int statusByte = 0xE0;
    int lsb = value & 0x7f;
    int msb = value >> 7;
    return statusByte << 16 | msb | (lsb << 8);
}

// This function writes the midi message to the arduino serial port:

void sendMidiMsg(uint8_t status_byte, uint8_t data1_byte, uint8_t data2_byte) {
    Serial.write((int)status_byte);
    Serial.write((int)data1_byte);
    Serial.write((int)data2_byte);
}


// This is the test function which prints the 3 bytes of the midi msg on the screen:

void printMidiMsg(uint8_t status_byte, uint8_t data1_byte, uint8_t data2_byte) {
    cout << (int)status_byte << endl;
    cout << (int)data1_byte << endl;
    cout << (int)data2_byte << endl;
}

int main (void) {
    const int PITCH_BEND_MSG = 0;
    const int CHANNEL_VOLUME_MSG = 1;

    int midiMsgType = PITCH_BEND_MSG;
    // int midiMsgType = CHANNEL_VOLUME_MSG;

    int value = 0x3fff;
    // int value = 0x7f;

    int midiMsg;

    if (midiMsgType == PITCH_BEND_MSG) {
        midiMsg = valueToPitchBendMsg(value);
    } else if (midiMsgType == CHANNEL_VOLUME_MSG) {
        midiMsg = valueToChannelVolumeMsg(value);
    }
    
    // extract 3 bytes of midi message
    int statusByte = midiMsg >> 16;
    int dataByte1 = midiMsg >> 8 & 0x7f;
    int dataByte2 = midiMsg & 0x7f;

    printMidiMsg(statusByte, dataByte1, dataByte2);

    // sendMidiMsg(statusByte, dataByte1, dataByte2) 

    return 0;
}