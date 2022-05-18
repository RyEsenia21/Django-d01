def my_var():
	hasa = 'has a type'
	vint = 42
	vstr = "42"
	vstr2 = "quarante-deux"
	vfloat = 42.0
	vbool = True
	vlist = [42]
	vdict = {42: 42}
	vtuple = (42,)
	vset = set()
	print(vint,hasa,type(vint))
	print(vstr,hasa,type(vstr))
	print(vstr2,hasa,type(vstr2))
	print(vfloat,hasa,type(vfloat))
	print(vbool,hasa,type(vbool))
	print(vlist,hasa,type(vlist))
	print(vdict,hasa,type(vdict))
	print(vtuple,hasa,type(vtuple))
	print(vset,hasa,type(vset))
	
if __name__ == '__main__':
	my_var()

