import sys

source = sys.stdin.read()

append = """
f((lambda s, p: s.format(p, repr(s), repr(p)))('{0}\\nf((lambda s, p: s.format(p, repr(s), repr(p)))({1}, {2}))\\n', """

print(source + append + repr(source) + '))\n', end='')
