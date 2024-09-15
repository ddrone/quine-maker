import sys

source = sys.stdin.read()

append = '\nf(%s)' % repr(source)

print(source + append)
