import sys

def bubblesort(numbers, iterations):
    iterations = min(iterations, len(numbers))
    while iterations >= 1:
        for k in range(len(numbers) - 1):
            if numbers[k] > numbers[k + 1]:
                numbers[k], numbers[k + 1] = numbers[k + 1], numbers[k]
        iterations -= 1
    return numbers

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers, iterations = line.split(' | ')
        result = bubblesort([int(x) for x in numbers.split(' ')], int(iterations))
        print(' '.join([str(x) for x in result]))

lines.close()

