f = open('123313.txt', 'r')
lines = f.read().splitlines()
f.close()

old_salary = int(lines[3])
new_salary = 1.11 * old_salary
lines[3] = str(new_salary)

f = open('123313.txt', 'w')
f.write('\n'.join(lines))
f.close()
