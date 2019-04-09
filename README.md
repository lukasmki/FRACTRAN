# FRACTRAN Interpreter

[FRACTRAN][1] is a Turing-complete programming language invented by the mathematican [John Conway][2].

A FRACTRAN program is an ordered list of positive fractions together with an initial positive integer input n.

The program is run by updating the integer _n_ as follows:

1. for the first fraction _f_ in the list for which _nf_ is an integer, replace _n_ by _nf_
2. repeat this rule until no fraction in the list produces an integer when multiplied by _n_, then halt.

[1]: https://en.wikipedia.org/wiki/FRACTRAN
[2]: https://en.wikipedia.org/wiki/John_Horton_Conway

## Elements of FRACTRAN code

FRACTRAN code has three parts:

- n, an optional positive starting integer
- n1/d1, n2/d2, ..., nk/dk, a sequence of fractions
- m, the maximum number of iterations (if omitted, default 100)

Example code:

```frac
2 17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1 15
```

This FRACTRAN code starts with `n=2` and executes over the following sequence of fractions until `m=15` numbers are generated or until the sequence terminates.

The FRACTRAN interpreter can also handle mathematical operations.

For example, consider the FRACTRAN program:

    2**a*3**b 2/3

which yields

    [2^a * 3^b, 2^(a-1) * 3^(b+1), 2^(a-2) * 3^(b+2), ..., 2^(0) * 3^(a+b)]

The interpreter evaluates each numerator, denominator, and starting number before executing.

```python
>>> fractran("2**4*3**1 3/2")
[48, 72, 108, 162, 243]
```

### Anatomy of a .frac file

```bash
1    2 17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1 15
2    This program generates 15 prime numbers.
```

FRACTRAN code should be on the first line of the file and only span one line. Only the first line of the file is read by the interpreter, so the rest of the file can be used to comment on the code.

## Usage

The interpreter can execute FRACTRAN code a few ways.

Through .frac files:

```bash
$ python fractran.py primes.frac
[2, 15, 825, 725, 1925, 2275, 425, 390, 330, 290, 770, 910, 170, 156, 132]
```

```bash
$ python fractran.py
File destination: primes.frac
[2, 15, 825, 725, 1925, 2275, 425, 390, 330, 290, 770, 910, 170, 156, 132]
```

Or by keyboard input:

```bash
$ python fractran.py
File destination:
Input fractran code: 2 3/2
[2, 3]
```

It can also be imported as a module for FRACTRAN execution:

```python
>>> from fractran import fractran
>>> result = fractran("2 3/2")
>>> print(result)
[2, 3]
```

## License

GNU GPLv3. See LICENSE for details.