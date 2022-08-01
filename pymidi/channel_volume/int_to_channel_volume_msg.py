def int_to_channel_volume_msg(value: int, channel: int = 0) -> int:
    # make minimum volume value 0 and max value 127.
    if value < 0:
        value = 0
    elif value > 127:
        value = 127

    # set midi channel to 0 if outside of range 0 to 15.
    if channel < 0 or channel > 15:
        channel = 0
    
    # add midi channel to status byte. 
    # 0xB0 to 0xBF is status byte for control change midi message
    # for midi channels 0 to 15.
    status_byte = 0xB0 + int(channel)

    # 2nd byte is type of midi control change;
    # 0x07 is channel volume.
    # (if 0x07 won't work then try 0x27)
    control_change_byte = 0x07
    
    # 3rd byte is data byte (i.e. volume level)
    data_byte = int(value)
    
    # append: 1) status byte to 2) control change byte and 3) data byte.
    return (status_byte << 16 | data_byte ) | (control_change_byte << 8)