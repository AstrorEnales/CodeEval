import sys

for i in range(13)[1::]:
    print(''.join(['%4d' % (i * j) for j in range(13)[1::]]).strip())        
