def relative_aspect_resolution_converter(relative_coordinates, resolution):

    converted_resolution = [0,0,0,0]
    resolution_x: int = resolution[0]
    resolution_y: int = resolution[1]


    for _ in range(len(relative_coordinates)):
        if (_ % 2) == 0:
            converted_resolution[_] = int(relative_coordinates[_] * resolution_x)
        else:
            converted_resolution[_] = int(relative_coordinates[_] * resolution_y)

    return converted_resolution