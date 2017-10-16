def bubble_sort(numbers):
    for j in range(len(numbers) -1, -1, -1):
        for i in range(j):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    print(numbers)


def main ():
    numbers = [23, 12, 9, 15, 6]
    bubble_sort(numbers)


if __name__ == "__main__":
    main()