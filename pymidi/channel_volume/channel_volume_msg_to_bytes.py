def channel_volume_msg_to_bytes(channel_volume_msg: int) -> bytes:
    '''
    converts integer channel volume midi message to bytes.
    '''
    status_byte = channel_volume_msg >> 16 & 0b11111111
    data_byte = channel_volume_msg & 0b11111111
    control_change_byte = channel_volume_msg >> 8 & 0b11111111
    return bytes([status_byte, control_change_byte, data_byte])