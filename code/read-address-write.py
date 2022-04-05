f = open('123790.txt', 'r')
lines = f.read().splitlines()
f.close()

lines[2] = 'Katowice, Polarna'

f = open('123313.txt', 'w')
f.write('\n'.join(lines))
f.close()
