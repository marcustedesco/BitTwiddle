PF1 = 'f>f<1&|'
PF2 = '1<f>&>8|9|3~7&^'

tos = 0

def Push(stack,element):
	global tos
	stack[tos]=element
	tos+=1
	return

def Pop(stack):
	global tos
	tos-=1
	return stack[tos]

def BitTwiddle(expression):

	stack=[0]*len(expression)

	def Shift (direction, expr):
		if direction==0:
			return (expr<<1)&15
		return expr>>1
	def Not (expr):
		return (~expr)&15
	def And (expr1, expr2):
		return expr1&expr2
	def Xor (expr1, expr2):
		return expr1^expr2
	def Or (expr1, expr2):
		return expr1|expr2
	
	for element in expression:
		if element=='<':
			Push(stack,Shift(0,Pop(stack)))
		elif element=='>':
			Push(stack,Shift(1,Pop(stack)))
		elif element=='~':
			Push(stack,Not(Pop(stack)))
		elif element=='&':
			Push(stack,And(Pop(stack),Pop(stack)))
		elif element=='^':
			Push(stack,Xor(Pop(stack),Pop(stack)))
		elif element=='|':
			Push(stack,Or(Pop(stack),Pop(stack)))
		else:
			Push(stack,int(element,16))

	#could use the hex() function and print 3rd char
	print ('%x' % Pop(stack))

	return

BitTwiddle(PF1)
BitTwiddle(PF2)
BitTwiddle('f9>&3~8^|c~b||')