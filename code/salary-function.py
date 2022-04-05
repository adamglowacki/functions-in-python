def change_salary(lines, x):
  old_salary = int(lines[3])
  new_salary = x * old_salary
  lines[3] = str(new_salary)
