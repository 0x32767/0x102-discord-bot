from pprint import pprint


class Node:
	def __init__(self, op_name: str, args: list[str]) -> None:
		self.op_name = op_name
		self.args = args


	def __repr__(self):
		return str(self)

	def __str__(self):
		return f"{self.op_name} :: {self.args}"


class Stack(object):
	def __init__(self, max_size:int=100):
		self.max_size = max_size
		self.stk = []

	def pop(self):
		return self.stk.pop()

	def push(self, element):
		if len(self.stk) >= self.max_size:
			raise Exception("stack overflow!")
		self.stk.append(element)
		return

	def dup(self):
		e = self.pop()
		self.push(e)
		self.push(e)

	def add(self):
		self.push(self.pop() + self.pop())

	def sub(self):
		self.push(self.pop() - self.pop())

	def mul(self):
		self.push(self.pop() * self.pop())

	def div(self):
		self.push(self.pop() / self.pop())

	def __repr__(self):
		return str(self.stk)

	@property
	def top(self):
		return self.stk[-1]


def create_node(ins: str) -> Node:
	op = ins.split(" ")

	print(Node(op[0], op[:-1]))

	return Node(op[0], op[:-1])


def execute(nodes, stack_ = None, from_ = None):
	stack = Stack() if not stack_ else stack_
	done = False

	for ins in nodes:
		if not ins.op_name == from_ and not done:
			done = True

		if ins.op_name == "push":
			stack.push(int(ins.args[0]) if ins.args[0].isdigit() else ins.args[0])

		elif ins.op_name == "pop":
			stack.pop()

		elif ins.op_name == "dup":
			stack.dup()

		elif ins.op_name == "sub":
			stack.sub()

		elif ins.op_name == "add":
			stack.add()

		elif ins.op_name == "mul":
			stack.mul()

		elif ins.op_name == "div":
			stack.div()

		elif ins.op_name == "ret":
			return

		elif ins.op_name == "jez":
			if stack.top == 0:
				execute(nodes, stack_=stack, from_=ins.args[0])

		elif ins.op_name == "gsb":
			execute(nodes, stack_=stack, from_=ins.args[0])

		elif ins.op_name == "print":
			print(stack)

		elif ins.op_name == "hlt":
			exit(0)


with open("pcclng.ynk", "r") as f:
	nodes = []
	for line in f.readlines():
		line = line.removesuffix("\n")

		if (d := line.split(" "))[0]:
			c = d.pop(0)
			d = d or None

			nodes.append(Node(c, d))

	execute(nodes)
