# Quine maker

Chances are, you have probably heard what a quine is. In case you haven't, it's a program that prints its own source code, and it's quite enlightening to have a go at writing it on your own. (In case you'd like to see one, check out `quine_simple.py` in this repository.)

What you might not know, that in **any** Turing-complete programming language and any one-argument function `f` in that language, it's possible to produce a program `P` that acts exactly as `f` on `P`'s source code. This repository is an implementation of such a program tranformation for Python 3, implemented in `make_quine.py`. The implementation expects the source file to be a valid Python 3 program having a function `f` of one argument, and will produce a program `P` running `f` on `P`'s source. In this case, a regular quine can be implemented by invoking `make_quine.py` on the following simple program:

```python
def f(x):
  print(x, end='')
```

Since `function.py` is provided in the repository, you can test that it works by running

```bash
python3 make_quine.py < function.py > gen_quine.py
diff gen_quine.py <(python3 gen_quine.py)
```
