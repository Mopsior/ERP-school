def get_available_options(length: int):
    available_options = ''
    for i in range(length):
        if i < (length - 1):
            available_options += f'{i+1}, '
        else:
            available_options += str(i+1)
    return available_options