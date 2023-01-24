def valid_ram_sizes(max_capacity):
    valid_sizes = [2]
    while valid_sizes[-1] * 2 <= max_capacity:
        valid_sizes.append(valid_sizes[-1] * 2)
    return valid_sizes


