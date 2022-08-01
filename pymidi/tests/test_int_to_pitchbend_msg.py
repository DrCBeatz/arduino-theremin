# unit tests for arduino theremin midi pitchbend functions.
#
# installation: type 'pip install pytest' in terminal.
# to run tests: type 'pytest' in working directory.

from pymidi.pitchbend.int_to_pitchbend_msg import int_to_pitchbend_msg
from pymidi.pitchbend.pitchbend_msg_to_bytes import pitchbend_msg_to_bytes
from pymidi.util.clean_bytestring import clean_bytestring

# helper functions:

def check_int_to_pitchbend_msg_value(initial_value: int = 0, channel: int = 0) -> bool:
    '''
    helper function for unit tests which converts result of 
    int_to_pitchbend_msg() back to original value passed as argument and 
    returns true if both are equal.
    '''
    result = int_to_pitchbend_msg(initial_value, channel)
    msb = result & 0b1111111
    lsb = result >> 8 & 0b1111111
    result_value = msb << 7 | lsb
    return initial_value == result_value

def check_int_to_pitchbend_msg_midi_channel(value: int = 0, channel: int = 0) -> bool:
    '''
    helper function for unit tests which checks that midi channel passed to int_to_pitchbend_msg()
    can be extracted from the function's return value
    '''
    return channel == int_to_pitchbend_msg(value, channel) >> 16 & 0b1111

def extract_pitchbend_value_from_bytes(test_value: int) -> int:
    '''
    helper function for extracting pitchbend value from bytes midi message.
    '''
    result = int_to_pitchbend_msg(test_value)
    bytes = pitchbend_msg_to_bytes(result)
    lsb = bytes[1]
    msb = bytes[2]
    return msb << 7 | lsb

# tests:

class TestCheckIntToPitchBendMsgClass:
    '''
    these tests use check_int_to_pitchbend_msg_value() to check that
    the value passed to int_to_pitchbend_msg() matches what is extracted from
    the result
    '''

    # 0 is default value for check_int_to_pitchbend_msg_value()
    # so this is the maximum negative pitchbend value
    def test_max_negative_pitchbend_value(self):
        assert check_int_to_pitchbend_msg_value()

    # 0x2000 is the value for no pitchbend (i.e. middle value)
    def test_no_pitchbend_value(self):
        assert check_int_to_pitchbend_msg_value(0x2000)
    
    # 0x3FFF is maximum positive pitchbend value
    def test_max_positive_pitchbend_value(self):
        assert check_int_to_pitchbend_msg_value(0x3FFF)

    # checks that changing the midi channel doesn't change the extracted value
    def test_non_default_midi_channel(self):
        assert check_int_to_pitchbend_msg_value(check_int_to_pitchbend_msg_value(0x3FFF, 5), 2)


class TestIntToPitchBendMsgGuardrailsClass:
    '''
    checks guardrails for max/min pitchbend values.
    '''
    # checks if negative value argument is set to 0
    def test_negative_pitchbend_value(self):
        assert int_to_pitchbend_msg(-1) == int_to_pitchbend_msg(0)
    
    # checks that values greater than 0x3FFF are set to 0x3FFF
    def test_excess_pitchbend_value(self):
        assert int_to_pitchbend_msg(0xFFFF) == int_to_pitchbend_msg(0x3FFF)

    def test_cast_float_value_to_int(self):
        assert int_to_pitchbend_msg(1.1) == int_to_pitchbend_msg(1)

class TestIntToPitchBendMsgMidiChannelClass:
    '''
    tests for (midi) channel argument/parameter in int_to_pitchbend_msg()
    '''
    # uses check_int_to_pitchbend_msg_midi_channel() to test that midi
    # channel argument can be extracted from int_to_pitchbend_msg() result.
    def test_check_int_to_pitchbend_msg_midi_channel(self):
        assert check_int_to_pitchbend_msg_midi_channel(0x2000, 5)
        assert check_int_to_pitchbend_msg_midi_channel(0x1000, 1)
        assert check_int_to_pitchbend_msg_midi_channel(0x3FFF, 7)
        assert check_int_to_pitchbend_msg_midi_channel(0x2EEF, 15)
        
    # checks that negative midi channel passed as argument is set to 0 in result
    def test_negative_midi_channel(self):
        assert int_to_pitchbend_msg(0xFFFF, -1) == int_to_pitchbend_msg(0xFFFF)
    
    # checks that midi channel greater than 15 is set to 0 in result
    def test_excess_midi_channel(self):
        assert int_to_pitchbend_msg(0xFFFF, 17) == int_to_pitchbend_msg(0xFFFF)
    
    # checks that decimal channel argument is cast to int in result
    def test_cast_midi_channel_float_to_int(self):
        assert int_to_pitchbend_msg(0xFFFF, 0.9) == int_to_pitchbend_msg(0xFFFF)
        assert int_to_pitchbend_msg(0xFFFF, 1.4) == int_to_pitchbend_msg(0xFFFF, 1)
        assert int_to_pitchbend_msg(0xFFFF, 14.9) == int_to_pitchbend_msg(0xFFFF, 14)

class TestPitchbendMsgToBytesClass:
    '''
    checks that pitchbend_msg_to_bytes() and int_to_pitchbend_msg() produce
    same pitchbend values.
    '''

    # checks middle (no pitchbend) value:
    def test_pitchbend_msg_to_bytes_mid_value(self):
        test_value = 0x2000
        result_value = extract_pitchbend_value_from_bytes(test_value)
        assert test_value == result_value
    
    # checks min value (max negative pitch bend):
    def test_pitchbend_msg_to_bytes_min_value(self):
        test_value = 0
        result_value = extract_pitchbend_value_from_bytes(test_value)
        assert test_value == result_value

    # checks max value (max positive pitch bend):
    def test_pitchbend_msg_to_bytes_min_value(self):
        test_value = 0x3FFF
        result_value = extract_pitchbend_value_from_bytes(test_value)
        assert test_value == result_value
    
    # checks excess value is converted to max value:
    def test_pitchbend_msg_to_bytes_excess_value(self):
        test_value = 0x4FFF
        result_value = extract_pitchbend_value_from_bytes(test_value)
        assert result_value < test_value and result_value == 0x3FFF

    # checks negative value is converted to min value:
    def test_pitchbend_msg_to_bytes_negative_value(self):
        test_value = -1
        result_value = extract_pitchbend_value_from_bytes(test_value)
        assert result_value > test_value and result_value == 0

    # checks changing midi channel results in correct value:
    def test_pitchbend_msg_to_bytes_channel(self):
        test_channel = 5
        result = int_to_pitchbend_msg(0, test_channel)
        bytes = pitchbend_msg_to_bytes(result)
        result_channel = bytes[0] & 0b1111
        assert test_channel == result_channel

class TestCleanByteStringClass:
    '''
    checks output of clean_bytestring()
    '''
    value = '1234'
    
    # checks if clean_bytestring() returns same numeric value.

    def test_clean_bytestring_no_added_characters(self):
        result = clean_bytestring(b'1234')
        assert self.value == result
    
    # checks if clean_bytestring() removes added spaces.
    def test_clean_bytestring_added_spaces(self):
        result = clean_bytestring(b'1 23 4 ')
        assert self.value == result
    
    # checks if clean_bytestring() removes newline and return characters.
    def test_clean_bytestring_newline_return_characters(self):
        result = clean_bytestring(b'1\n23\r4')
        assert self.value == result
    
    # checks that order of numbers matters
    def test_clean_bytestring_reverse_not_equal(self):
        result = clean_bytestring(b'4321')
        assert result != self.value

    # checks that passing null value returns 0    
    def test_clean_bytestring_null_value(self):
        result = clean_bytestring(None)
        assert result == 0