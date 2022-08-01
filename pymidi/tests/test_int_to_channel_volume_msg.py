# unit tests for arduino theremin midi channel volume functions.
#
# installation: type 'pip install pytest' in terminal.
# to run tests: type 'pytest' in working directory.

import sys
sys.path.insert(0, '')

from pymidi.channel_volume.int_to_channel_volume_msg import int_to_channel_volume_msg
from pymidi.channel_volume.channel_volume_msg_to_bytes import channel_volume_msg_to_bytes

# helper functions:

def check_int_to_channel_volume_msg_value(initial_value: int = 0, channel: int = 0) -> bool:
    '''
    helper function for unit tests which converts result of 
    int_to_channel_volume_msg() back to original value passed as argument and 
    returns true if both are equal.
    '''
    result = int_to_channel_volume_msg(initial_value, channel)
    data_byte = result & 0b1111111
    return initial_value == data_byte

def check_int_to_channel_volume_msg_midi_channel(value: int = 0, channel: int = 0) -> bool:
    '''
    helper function for unit tests which checks that midi channel passed to int_to_channel_volume_msg()
    can be extracted from the function's return value
    '''
    return channel == int_to_channel_volume_msg(value, channel) >> 16 & 0b1111

def extract_channel_volume_value_from_bytes(test_value: int) -> int:
    '''
    helper function for extracting channel volume value from bytes midi message.
    '''
    result = int_to_channel_volume_msg(test_value)
    bytes = channel_volume_msg_to_bytes(result)
    data = bytes[2]
    return data

# tests:

class TestCheckIntToChannelVolumeMsgClass:
    '''
    these tests use check_int_to_channel_volume_msg_value() to check that
    the value passed to int_to_channel_volume_msg() matches what is extracted from
    the result
    '''
    # 0 is minimum (and default) volume value
    def test_min_channel_volume_value(self):
        assert check_int_to_channel_volume_msg_value()
    
    # 127 is maximum channel volume value
    def test_max_channel_volume_value(self):
        assert check_int_to_channel_volume_msg_value(127)

    # checks that changing the midi channel doesn't change the extracted value
    def test_non_default_midi_channel(self):
        assert check_int_to_channel_volume_msg_value(check_int_to_channel_volume_msg_value(127, 5), 2)


class TestIntToChannelVolumeMsgGuardrailsClass:
    '''
    checks guardrails for max/min channel volume values.
    '''
    # checks if negative value argument is set to 0
    def test_negative_channel_volume_value(self):
        assert int_to_channel_volume_msg(-1) == int_to_channel_volume_msg(0)
    
    # checks that values greater than 127 are set to 127
    def test_excess_channel_volume_value(self):
        assert int_to_channel_volume_msg(127) == int_to_channel_volume_msg(127)

    def test_cast_float_value_to_int(self):
        assert int_to_channel_volume_msg(1.1) == int_to_channel_volume_msg(1)

class TestIntToChannelVolumeMsgMidiChannelClass:
    '''
    tests for (midi) channel argument/parameter in int_to_channel_volume_msg()
    '''
    # uses check_int_to_channel_volume_msg_midi_channel() to test that midi
    # channel argument can be extracted from int_to_channel_volume_msg() result.
    def test_check_int_to_channel_volume_msg_midi_channel(self):
        assert check_int_to_channel_volume_msg_midi_channel(63, 5)
        assert check_int_to_channel_volume_msg_midi_channel(31, 1)
        assert check_int_to_channel_volume_msg_midi_channel(127, 7)
        assert check_int_to_channel_volume_msg_midi_channel(100, 15)
        
    # checks that negative midi channel passed as argument is set to 0 in result
    def test_negative_midi_channel(self):
        assert int_to_channel_volume_msg(127, -1) == int_to_channel_volume_msg(127)
    
    # checks that midi channel greater than 15 is set to 0 in result
    def test_excess_midi_channel(self):
        assert int_to_channel_volume_msg(127, 17) == int_to_channel_volume_msg(127)
    
    # checks that decimal channel argument is cast to int in result
    def test_cast_midi_channel_float_to_int(self):
        assert int_to_channel_volume_msg(127, 0.9) == int_to_channel_volume_msg(127)
        assert int_to_channel_volume_msg(127, 1.4) == int_to_channel_volume_msg(127, 1)
        assert int_to_channel_volume_msg(127, 14.9) == int_to_channel_volume_msg(127, 14)

class TestChannelVolumeMsgToBytesClass:
    '''
    checks that channel_volume_msg_to_bytes() and int_to_channel_volume_msg() produce
    same values.
    '''
    # checks min volume value:
    def test_channel_volume_msg_to_bytes_min_value(self):
        test_value = 0
        result_value = extract_channel_volume_value_from_bytes(test_value)
        assert test_value == result_value

    # checks max value:
    def test_channel_volume_msg_to_bytes_min_value(self):
        test_value = 127
        result_value = extract_channel_volume_value_from_bytes(test_value)
        assert test_value == result_value
    
    # checks excess value is converted to max value:
    def test_channel_volume_msg_to_bytes_excess_value(self):
        test_value = 255
        result_value = extract_channel_volume_value_from_bytes(test_value)
        assert result_value < test_value and result_value == 127

    # checks negative value is converted to min value:
    def test_channel_volume_msg_to_bytes_negative_value(self):
        test_value = -1
        result_value = extract_channel_volume_value_from_bytes(test_value)
        assert result_value > test_value and result_value == 0

    # checks changing midi channel results in correct value:
    def test_channel_volume_msg_to_bytes_channel(self):
        test_channel = 5
        result = int_to_channel_volume_msg(0, test_channel)
        bytes = channel_volume_msg_to_bytes(result)
        result_channel = bytes[0] & 0b1111
        assert test_channel == result_channel
    
    def test_status_byte(self):
        test_value = 0
        result = int_to_channel_volume_msg(test_value)
        bytes = channel_volume_msg_to_bytes(result)
        assert bytes[0] == 0xB0 and bytes[2] == test_value
    
    def test_status_byte_and_midi_channel(self):
        test_value = 0
        midi_channel = 3
        status = 0xB0 + midi_channel
        result = int_to_channel_volume_msg(test_value, midi_channel)
        bytes = channel_volume_msg_to_bytes(result)
        assert bytes[0] == status and bytes[2] == test_value
    
    def test_control_change_byte(self):
        test_value = 127
        result = int_to_channel_volume_msg(test_value)
        bytes = channel_volume_msg_to_bytes(result)
        assert bytes[1] == 0x07 and bytes[2] == test_value
