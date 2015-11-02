import sys
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        number = int(line)
        roman = ''
        if number >= 1000:
            roman = roman + 'M' * (number / 1000)
            number = number - (1000 * (number / 1000))
        if number >= 900:
            roman = roman + 'CM'
            number = number - 900
        if number >= 500:
            roman = roman + 'D'
            number = number - 500
        if number >= 400:
            roman = roman + 'CD'
            number = number - 400
        if number >= 100:
            roman = roman + 'C' * (number / 100)
            number = number - (100 * (number / 100))
        if number >= 90:
            roman = roman + 'XC'
            number = number - 90
        if number >= 50:
            roman = roman + 'L'
            number = number - 50
        if number >= 40:
            roman = roman + 'XL'
            number = number - 40
        if number >= 10:
            roman = roman + 'X' * (number / 10)
            number = number - (10 * (number / 10))
        if number == 9:
            roman = roman + 'IX'
            number = number - 9
        if number >= 5:
            roman = roman + 'V'
            number = number - 5
        if number == 4:
            roman = roman + 'IV'
            number = number - 4
        roman = roman + 'I' * number
        print(roman)

lines.close()
