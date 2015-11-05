import sys

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        numbers, x = line.split(';')
        x = int(x)
        numbers = [int(num) for num in numbers.split(',')]
        results = []
        for i in range(len(numbers) - 1):
            for j in range(i + 1, len(numbers)):
                if (numbers[i] + numbers[j]) == x:
                    results.append(str(numbers[i]) + "," + str(numbers[j]))
        print(';'.join(results) if len(results) > 0 else 'NULL')

lines.close()
