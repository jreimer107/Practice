from math import floor

NUM_ROTATIONS = 4
IMAGE_SIDE_LEN = 5
HAS_ODD_SIZE = IMAGE_SIDE_LEN % 2 != 0


def generate_image(side_len):
    image = []
    i = 1
    for x in range(side_len):
        image.append([])
        for y in range(side_len):
            image[x].append(i)
            i += 1
    return image


def swap_out(x: int, y: int, new_pixel: int) -> int:
    """Swaps out a pixel in the image for a given one. Returns the original.

    Args:
        x (int): Row of the pixel.
        y (int): Column of the pixel.
        new_pixel (int): New pixel value.

    Returns:
        int: Old pixel value.
    """
    temp = image[x][y]
    image[x][y] = new_pixel
    return temp


def rotate_pointers(ring_start: int, ring_end: int, x: int, y: int, num_rotations: int):
    """Given coordinates to a pixel, rotates those coordinates around the image.

    Args:
        ring_start (int): Row or column index where the ring starts
        ring_end (int): Row or column index where the ring ends
        x (int): Current row.
        y (int): Current column.
        num_rotations (int): How many pixes we should rotate around.

    Returns:
        tuple[int, int] The rotated coordinates.
    """
    remaining_rotations = num_rotations
    while remaining_rotations > 0:
        if x == ring_start and y != ring_end:  # top
            rotations = min(ring_end - y, remaining_rotations)
            y += rotations
        elif x != ring_start and y == ring_start:  # left
            rotations = min(x - ring_start, remaining_rotations)
            x -= rotations
        elif x == ring_end and y != ring_start:  # bottom
            rotations = min(y - ring_start, remaining_rotations)
            y -= rotations
        else:  # right
            rotations = min(ring_end - x, remaining_rotations)
            x += rotations

        remaining_rotations -= rotations
      
    return x, y


def juggle(ring_start: int, ring_end: int, x: int, y: int, num_rotations: int) -> None:
    """Given a pixel, rotates that pixel and any resulting displaced pixels.

    Args:
        ring_start (int): Row or column index where the ring starts.
        ring_end (int): Row or column index where the ring ends.
        x (int): Pixel row.
        y (int): Pixel column.
        num_rotations (int): How many pixes we should rotate around.
    """
    start_x = x
    start_y = y
    temp = image[start_x][start_y]
    x, y = rotate_pointers(ring_start, ring_end, x, y, num_rotations)
    while x != start_x or y != start_y:
        temp = swap_out(x, y, temp)
        x, y = rotate_pointers(ring_start, ring_end, x, y, num_rotations)
    image[x][y] = temp


def print_image():
    """Prints the image."""
    for i in range(IMAGE_SIDE_LEN):
        for j in range(IMAGE_SIDE_LEN):
            print(str(image[i][j]), end="\t")
        print()


def rotate_ring(ring_num: int, num_rotations: int) -> None:
    """Rotates a ring of the image.

    Args:
        ring_num (int): Radius of the ring.
        num_rotations (int): How many times we should rotate the center pixels of the image.
    """
    ring_side_len = 2 * ring_num
    if HAS_ODD_SIZE:
        ring_side_len += 1

    num_rings = floor(IMAGE_SIDE_LEN / 2)
    ring_start = num_rings - ring_num
    ring_end = IMAGE_SIDE_LEN - ring_start - 1

    x = ring_start
    y = ring_start
    iterations = ring_num
    if HAS_ODD_SIZE:
        iterations += ring_num

    for i in range(iterations):
        juggle(ring_start, ring_end, x, y, num_rotations * ring_num)
        x, y = rotate_pointers(ring_start, ring_end, x, y, 1)


def rotate_image(num_rotations: int) -> None:
    """Rotates the image.

    Args:
        num_rotations (int): How many times we should rotate the center pixels of the image.
    """
    num_rings = floor(IMAGE_SIDE_LEN / 2)
    for j in range(num_rings):
        rotate_ring(j + 1, num_rotations)


def main():
    """Main function. Generates, rotates and prints the image."""
    global image
    image = generate_image(IMAGE_SIDE_LEN)
    print_image()
    print("-----------")
    rotate_image(NUM_ROTATIONS)
    print_image()


if __name__ == '__main__':
    main()
