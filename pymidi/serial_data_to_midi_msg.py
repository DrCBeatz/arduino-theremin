from pymidi.util.clean_bytestring import clean_bytestring
from pymidi.channel_volume.int_to_channel_volume_msg import int_to_channel_volume_msg
from pymidi.pitchbend.int_to_pitchbend_msg import int_to_pitchbend_msg
from pymidi.channel_volume.channel_volume_msg_to_bytes import channel_volume_msg_to_bytes
from pymidi.pitchbend.pitchbend_msg_to_bytes import pitchbend_msg_to_bytes

def serial_data_to_midi_msg(serial_data: bytes) -> bytes:
    # clean string using regular expression to filter out non-numeric characters
    # (except for 'p' and 'v').
    serial_msg = clean_bytestring(serial_data)

    # 1st character of serial_msg string is msg_type
    # ('v' for volume or 'p' for pitchbend).
        
    try:
        msg_type = serial_msg[0]
    except:
        msg_type = 'v' # if there's no message type character default to 'v' 

    # cast serial value as int; if casting fails set value to 0.
    try:
        serial_value = int(serial_msg[1:])
    except:
        serial_value = 0

    # check msg_type value and create midi message            
        
    if msg_type == 'v': # volume message
        # get channel volume message
        channel_volume_msg = int_to_channel_volume_msg(serial_value)

        # turn channel volume message into bytes
        data = channel_volume_msg_to_bytes(channel_volume_msg) 
    elif msg_type == 'p': # pitchbend message
        # get pitchbend message
        pitchbend_msg = int_to_pitchbend_msg(serial_value)

        # turn pitchbend message into bytes
        data = pitchbend_msg_to_bytes(pitchbend_msg)

    return data