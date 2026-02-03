"""Simple arithmetic operations example.

Run as a script for quick CLI use or import the functions.
Examples:
  python src/inter3.py 2 + 3
  python src/inter3.py 5 pow 2
"""
import sys

def add(a, b):
	return a + b

def sub(a, b):
	return a - b

def mul(a, b):
	return a * b

def div(a, b):
	return a / b

def power(a, b):
	return a ** b

def mod(a, b):
	return a % b

OPS = {
	'+': add,
	'-': sub,
	'*': mul,
	'/': div,
	'pow': power,
	'^': power,
	'%': mod,
}


def usage():
	print('Usage: python src/inter3.py <num1> <op> <num2>')
	print('Operators: +  -  *  /  pow (or ^)  %')


def main(argv):
	if len(argv) == 4:
		try:
			a = float(argv[1])
			op = argv[2]
			b = float(argv[3])
		except ValueError:
			print('Error: numbers must be numeric')
			return 1
		func = OPS.get(op)
		if not func:
			print('Error: unknown operator')
			usage()
			return 1
		try:
			res = func(a, b)
		except ZeroDivisionError:
			print('Error: division by zero')
			return 1
		print(res)
		return 0

	# no args: show examples
	usage()
	print('\nExamples:')
	print('  add(2, 3) ->', add(2, 3))
	print('  sub(5, 1) ->', sub(5, 1))
	print('  mul(4, 2.5) ->', mul(4, 2.5))
	print('  div(7, 2) ->', div(7, 2))
	print('  power(2, 8) ->', power(2, 8))
	print('  mod(10, 3) ->', mod(10, 3))
	return 0


if __name__ == '__main__':
	sys.exit(main(sys.argv))
