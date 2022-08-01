'''
unit test for serial data to midi message function
'''

from pymidi.serial_data_to_midi_msg import serial_data_to_midi_msg

class TestSerialDataToMidiMsgClass():
    value = 63
    value2 = 0x2000
    msg = str('v' + str(value)).encode()
    msg2 = str('p' + str(value2)).encode()
    def test_serial_data_to_midi_msg1(self):
        result = serial_data_to_midi_msg(self.msg)
        assert result[0] == 0xB0 and result[1] == 0x07 and result[2] == self.value

    def test_serial_data_to_midi_msg2(self):
        result = serial_data_to_midi_msg(self.msg2)
        assert result[0] == 0xE0 and result[1] == self.value2 & 0b1111111 and result[2] == self.value2 >> 7

    def test_serial_data_to_midi_msg3(self):
        result = serial_data_to_midi_msg(b'oh hai')
        assert result[0] == 0xB0 and result[1] == 0x07 and result[2] == 0
