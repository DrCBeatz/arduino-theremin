def pitchbend_msg_to_bytes(pitchbend_msg: int) -> bytes:
    '''
    converts integer pitchbend message to bytes.
    '''
    status_byte = pitchbend_msg >> 16 & 0b11111111
    msb_byte = pitchbend_msg & 0b11111111
    lsb_byte = pitchbend_msg >> 8 & 0b11111111
    return bytes([status_byte, lsb_byte, msb_byte])