def x(ch):
	y = int(ch,16)
	print("Integer value ",y)
	z = hex(y)  # returns 3-character string
	print ("Hex value ", z)
	print ("Hex value ", z[2])   # print third character
x("F")
