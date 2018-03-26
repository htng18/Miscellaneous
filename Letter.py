def LETTERS(input,case=0):

	"""This function is to output the letters from a to z (A to Z) 
	by inputting a list of integers from 1 to 26 for case = 0 (1).
	Example 1,
	LETTERS([1,2])
	['a','b']
    Example 2,
    LETTERS([1,2],1)
    ['A','B']  
	"""
	
	if not isinstance(case,int):
		raise TypeError(case,"case must be an integer.")

	if not (case in (0,1)):
	 	raise ValueError("case should be 0 or 1")
	
	if case==0:
		charnum=96
	else:
		charnum=64
	
	if not isinstance(input, list):
		raise TypeError("Input should be a list")
	if not all(isinstance(item,int) for item in input):
		raise TypeError("Input should be integers.")
	if not set(input).issubset(set(list(range(1,27)))):
		raise ValueError("Input integers should be larger than 0 and smaller than 27")
	else: 
		return list(map(chr,map(lambda x:x+charnum,input)))
		
	
