import sys

users = []
allGroups = []
lines = open(sys.argv[1], 'r')
for line in lines:
    line = line.replace('\n', '').replace('\r', '')
    if len(line) > 0:
        user = [x.split(',') for x in line.split(':')]
        users.append([user[0][0], user[1], user[2]])
        allGroups.extend(user[2])

lines.close()

allGroups = set(allGroups)
users = {x[0]: [x[1], x[2]] for x in users}
for k in sorted(users.keys()):
    friends = users[k][0]
    groups = users[k][1]
    suggestions = []
    for group in allGroups:
        friendsRatio = len([x for x in friends if group in users[x][1] and group not in groups]) / float(len(friends))
        if friendsRatio >= 0.5:
            suggestions.append(group)
    if len(suggestions) > 0:
        print(k + ':' + ','.join(sorted(suggestions)))