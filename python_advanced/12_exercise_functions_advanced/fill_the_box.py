def fill_the_box(h, l, w, *args):
    volume = h * l * w

    for arg in args:
        if arg == "Finish":
            break
        volume -= arg

    if volume > 0:
        return f"There is free space in the box. You could put {volume} more cubes."
    return f"No more free space! You have {abs(volume)} more cubes."
