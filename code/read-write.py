f = open('123313.txt', 'r')
lines = f.read().splitlines()
f.close()

f = open('123313.txt', 'w')
f.write('\n'.join(lines))
f.close()
