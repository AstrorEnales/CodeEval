import sys

money = {'PENNY': .01,'NICKEL': .05,'DIME': .10,'QUARTER': .25,'HALF DOLLAR': .50,'ONE': 1.00,'TWO': 2.00,'FIVE': 5.00,'TEN': 10.00,'TWENTY': 20.00,'FIFTY': 50.00,'ONE HUNDRED': 100.00}

def handleMoney(change, amount, result):
    amountNumber = money[amount]
    if change >= amountNumber:
        count = int(change / amountNumber)
        result.extend([amount] * count)
        change -= count * amountNumber
        change = round(change, 2)
    return [result, change]

lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        pp, ch = [float(x) for x in line.split(';')]
        if ch < pp:
            print('ERROR')
        elif ch == pp:
            print('ZERO')
        else:
            change = ch - pp
            result = []
            result, change = handleMoney(change, 'ONE HUNDRED', result)
            result, change = handleMoney(change, 'FIFTY', result)
            result, change = handleMoney(change, 'TWENTY', result)
            result, change = handleMoney(change, 'TEN', result)
            result, change = handleMoney(change, 'FIVE', result)
            result, change = handleMoney(change, 'TWO', result)
            result, change = handleMoney(change, 'ONE', result)
            result, change = handleMoney(change, 'HALF DOLLAR', result)
            result, change = handleMoney(change, 'QUARTER', result)
            result, change = handleMoney(change, 'DIME', result)
            result, change = handleMoney(change, 'NICKEL', result)
            result, change = handleMoney(change, 'PENNY', result)
            print(','.join(result))

lines.close()
