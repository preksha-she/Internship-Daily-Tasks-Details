import ast
import operator
import os
import sys

"""Simple CLI calculator.

Supports: +, -, *, /, //, %, ** (use ^ as alias for **), unary +/-, and parentheses.
Commands: help, clear, exit, quit
"""

OPS = {
	ast.Add: operator.add,
	ast.Sub: operator.sub,
	ast.Mult: operator.mul,
	ast.Div: operator.truediv,
	ast.FloorDiv: operator.floordiv,
	ast.Mod: operator.mod,
	ast.Pow: operator.pow,
}


def eval_node(node):
	if isinstance(node, ast.Expression):
		return eval_node(node.body)
	if isinstance(node, ast.Constant):
		return node.value
	if isinstance(node, ast.Num):
		return node.n
	if isinstance(node, ast.BinOp):
		left = eval_node(node.left)
		right = eval_node(node.right)
		op_type = type(node.op)
		if op_type in OPS:
			return OPS[op_type](left, right)
		raise ValueError(f"Unsupported operator: {op_type}")
	if isinstance(node, ast.UnaryOp):
		operand = eval_node(node.operand)
		if isinstance(node.op, ast.UAdd):
			return +operand
		if isinstance(node.op, ast.USub):
			return -operand
	raise ValueError(f"Unsupported expression: {ast.dump(node)}")


def evaluate(expr: str):
	# allow ^ as alias for **
	expr = expr.replace('^', '**')
	try:
		parsed = ast.parse(expr, mode='eval')
	except SyntaxError as e:
		raise ValueError("Invalid syntax") from e
	# ensure AST contains only safe nodes
	for node in ast.walk(parsed):
		if not isinstance(node, (ast.Expression, ast.BinOp, ast.UnaryOp,
								 ast.Constant, ast.Num, ast.Add, ast.Sub,
								 ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
								 ast.Pow, ast.UAdd, ast.USub, ast.Load, ast.Tuple,
								 ast.List, ast.Expr, ast.Call, ast.Name, ast.Subscript,
								 ast.Slice)):
			# Reject any complex/unsafe nodes (calls/names will be rejected here)
			allow = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Num,
					 ast.Add, ast.Sub, ast.Mult, ast.Div, ast.FloorDiv, ast.Mod,
					 ast.Pow, ast.UAdd, ast.USub, ast.Load)
			if not isinstance(node, allow):
				raise ValueError("Disallowed expression")
	return eval_node(parsed)


def print_help():
	print("Simple calculator — enter arithmetic expressions")
	print("Operators: +  -  *  /  //  %  ^ (power, e.g. 2^3)")
	print("Commands: help, clear, exit, quit")


def repl():
	print_help()
	while True:
		try:
			s = input('calc> ').strip()
		except (EOFError, KeyboardInterrupt):
			print('\nExiting...')
			return
		if not s:
			continue
		if s.lower() in ('exit', 'quit'):
			print('Bye')
			return
		if s.lower() == 'help':
			print_help()
			continue
		if s.lower() == 'clear':
			os.system('cls' if os.name == 'nt' else 'clear')
			continue
		try:
			result = evaluate(s)
			print(result)
		except ZeroDivisionError:
			print('Error: division by zero')
		except ValueError as e:
			print('Error:', e)
		except Exception:
			print('Error: invalid expression')


if __name__ == '__main__':
	repl()