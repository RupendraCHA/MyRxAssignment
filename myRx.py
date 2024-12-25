def convert_to_Square(array):
    squares_array = []

    for num in array:
        if (num < 0):
            num = num * -1
            num_square = num * num
        else:
            num_square = num * num
        squares_array.append(num_square)
    squares_array.sort()
    print(squares_array)

def main():
    array = [-12, -8, -7, -5, 2, 4, 5, 11, 15]
    convert_to_Square(array)

main()