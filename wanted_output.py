def f(x):
  print(x, end='')

f((lambda s, p: s.format(p, repr(s), repr(p)))('{0}\nf((lambda s, p: s.format(p, repr(s), repr(p)))({1}, {2}))\n', "def f(x):\n  print(x, end='')\n"))
