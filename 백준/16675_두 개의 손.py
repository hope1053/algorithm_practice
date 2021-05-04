RSP = input().split(' ')
ms, tk = RSP[:2], RSP[2:]

win = {'R':'P', 'S':'R', 'P':'S'}

if ms[0] == ms[1] and win[ms[0]] in tk:
    print('TK')
elif tk[0] == tk[1] and win[tk[0]] in ms:
    print('MS')
else:
    print('?')

