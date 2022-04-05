# READ FILE
f = open('123313.txt', 'r')
lines = f.read().splitlines()
f.close()

# CHANGE SALARY
old_salary = int(lines[3])
new_salary = 1.11 * old_salary
lines[3] = str(new_salary)

# WRITE FILE
f = open('123313.txt', 'w')
f.write('\n'.join(lines))
f.close()

# ---

# READ FILE
f = open('123790.txt', 'r')
lines = f.read().splitlines()
f.close()

# CHANGE ADDRESS
lines[2] = 'Katowice, Polarna'

# WRITE FILE
f = open('123790.txt', 'w')
f.write('\n'.join(lines))
f.close()

# ---

# READ FILE
f = open('123856.txt', 'r')
lines = f.read().splitlines()
f.close()

# CHANGE SALARY
old_salary = int(lines[3])
new_salary = 1.10 * old_salary
lines[3] = str(new_salary)

# WRITE FILE
f = open('123856.txt', 'w')
f.write('\n'.join(lines))
f.close()
