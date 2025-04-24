import numpy as np

def make_odd_box(size):
    box = np.zeros((size, size), dtype=int)
    row, col = 0, size // 2  
    for num in range(1, size * size + 1):
        box[row, col] = num
        new_row, new_col = (row - 1) % size, (col + 1) % size  
        if box[new_row, new_col]:  
            row += 1
        else:
            row, col = new_row, new_col
    return box

def make_double_even_box(size):
    box = np.arange(1, size * size + 1).reshape(size, size)
    flip = np.ones((size, size), dtype=bool)
    for row in range(size):
        for col in range(size):
            if (row % 4 == col % 4) or (row % 4 + col % 4 == 3):
                flip[row, col] = False
    box[flip], box[~flip] = box[~flip], box[flip]
    return box

def make_single_even_box(size):
    half = size // 2
    small_size = half * half
    small_box = make_odd_box(half)
    box = np.zeros((size, size), dtype=int)

    for i in range(2):
        for j in range(2):
            box[i * half:(i + 1) * half, j * half:(j + 1) * half] = (
                small_box + small_size * (i * 2 + j)
            )

    swap_zone = (size - 2) // 4
    for row in range(half):
        for col in range(swap_zone):
            box[row, col], box[row + half, col] = box[row + half, col], box[row, col]
            box[row, -(col + 1)], box[row + half, -(col + 1)] = box[row + half, -(col + 1)], box[row, -(col + 1)]
    col = swap_zone
    for row in range(half):
        box[row, col], box[row + half, col] = box[row + half, col], box[row, col]
    return box

def make_magic_box(size):
    if size % 2 == 1:
        return make_odd_box(size)
    elif size % 4 == 0:
        return make_double_even_box(size)
    else:
        return make_single_even_box(size)

sizes = [4, 5, 6, 7, 8]
for size in sizes:
    print(f"Magic Box for size = {size}:")
    print(make_magic_box(size), "\n")
