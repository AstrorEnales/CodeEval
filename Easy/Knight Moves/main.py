import sys

letters = 'abcdefgh'

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        fields = []
        letter = letters.index(line[0])
        number = int(line[1])
        if number >= 3:
            if letter >= 1:
                fields.append(letters[letter - 1] + str(number - 2))
            if letter <= 6:
                fields.append(letters[letter + 1] + str(number - 2))
        if number <= 6:
            if letter >= 1:
                fields.append(letters[letter - 1] + str(number + 2))
            if letter <= 6:
                fields.append(letters[letter + 1] + str(number + 2))
                
        if letter >= 2:
            if number >= 2:
                fields.append(letters[letter - 2] + str(number - 1))
            if number <= 7:
                fields.append(letters[letter - 2] + str(number + 1))
        if letter <= 5:
            if number >= 2:
                fields.append(letters[letter + 2] + str(number - 1))
            if number <= 7:
                fields.append(letters[letter + 2] + str(number + 1))
        
        print(' '.join(sorted(fields)))

lines.close()
