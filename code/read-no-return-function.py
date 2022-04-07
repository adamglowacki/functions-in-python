def read_file(person):
  f = open(person + '.txt', 'r')
  lines = f.read().splitlines()
  f.close()
