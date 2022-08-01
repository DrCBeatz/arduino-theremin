# int_to_pitchbend_msg(value, channel = 0)

# function accepts two parameters: 'value' (an unsigned integer to be converted
# to pitchbed midi message) and an optional parameter 'channel' (for the midi
# channel of the pitchbend message, default is 0 for midi channel 0) .

# pitchbend 'value' is 14-bit unsigned integer with the following range:
# 0x0000 is minimum pitch bend value (-pitch bend)
# 0x2000 (8192 base 10) is middle pitch bend value (no pitch bend)
# 0x3FFF (16383 base 10) max pitch bend value (+pitch bend)

# function returns midi pitchbend message consisting of 3 bytes.
# midi pitchbend message structure (1 status byte + 2 data bytes):
# 0b11100000 + 0b01111111 + 0b01111111
# [ status ]   [lsb data]   [msb data]

# note that status byte has 1 as leftmost (most significant) bit 
# and data bytes have 0 as leftmost bit.
# the reason for this is you could send status byte once and then 
# keep sending data bytes for the same parameter without 
# having to resend the status byte.
# data bytes therefore have only 7-bits because leftmost bit is always 0.

# high nibble (leftmost 4-bits) of status byte is the type of midi message 
# (e.g. 0xE is pitchbend in this case).
# and low nibble (rightmost 4-bits) is midi channel (0 to 15).

def int_to_pitchbend_msg(value: int, channel: int = 0) -> int:
    # make minimum pitch bend value 0 and max value 0xFFFF or 16838.
    if value < 0:
        value = 0
    elif value > 0x3FFF:
        value = 0x3FFF

    # set midi channel to 0 if outside of range 0 to 15.
    if channel < 0 or channel > 15:
        channel = 0
    
    # add midi channel to status byte. 
    # 0xE0 to 0xEF is status byte for pitch bend midi message 
    # for midi channels 0 to 15.
    status_byte = 0xE0 + int(channel)

    # extract least significant byte (lsb) using 7-bit AND mask.
    lsb = int(value) & 0b1111111
    
    # extract most significant byte (msb) by bitshifting right 7-bits.
    msb = int(value) >> 7 
    
    # append status byte to pitch bend value (lsb followed by msb).
    return (status_byte << 16  | msb ) | (lsb << 8)