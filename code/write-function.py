def write_file(person, lines):
  f = open(person + '.txt', 'w')
  f.write('\n'.join(lines))
  f.close()
