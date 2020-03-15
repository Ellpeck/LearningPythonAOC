width = 25
height = 6


def make_layer():
    return [[0 for x in range(0, height)] for x in range(0, width)]


def load_image(data):
    image = []
    x = 0
    y = 0
    layer = 0
    for num in data:
        pixel = int(num)

        curr_layer = None
        if layer < len(image):
            curr_layer = image[layer]
        else:
            curr_layer = make_layer()
            image.append(curr_layer)

        curr_layer[x][y] = pixel
        x += 1
        if x >= width:
            x = 0
            y += 1
            if y >= height:
                y = 0
                layer += 1
    return image


data = open("input/8").read()
image = load_image(data)

# part 1
# find layer with least zeros
lowest_zeros = width * height
lowest_zeros_layer = 0
for layer in image:
    zeros = 0
    for x in range(0, width):
        for y in range(0, height):
            if layer[x][y] == 0:
                zeros += 1
    if zeros < lowest_zeros:
        lowest_zeros = zeros
        lowest_zeros_layer = layer

# sum ones and twos on lowest layer
ones = 0
twos = 0
for x in range(0, width):
    for y in range(0, height):
        val = lowest_zeros_layer[x][y]
        if val == 1:
            ones += 1
        elif val == 2:
            twos += 1
print(ones * twos)


# part 2
for y in range(0, height):
    for x in range(0, width):
        for l in range(0, len(image)):
            color = image[l][x][y]
            if color == 2:  # transparent
                continue
            print("#" if color == 1 else " ", end="")
            break
    print()
