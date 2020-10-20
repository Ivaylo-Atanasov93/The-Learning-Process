def decode_position(position, board_size):
    row = (position - 1) // board_size
    col = (position - 1) % board_size
    return (row, col)


def all_single_value(ll, value):
    for v in ll:
        if v != value:
            return False
    return True