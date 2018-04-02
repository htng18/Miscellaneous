def cats(delim="",*args):

	""" 
		This function is to concatenate the different input 
		strings with the input delimiter.
		Parameters:
		delim: The input delimiter to be concatenated.
		args: The input string to be concatenated.

		For example,
		>>> cats('-',"A",123","456","789")
		>>> 'A-123-456-789'

	"""

	if not isinstance(delim,str):
		raise TypeError("Delimiter must be a string.")

	if not all(isinstance(item,str) for item in args):
		raise TypeError("Input should be a string.")



	cat=""
	
	for i in args[0:-1]:
		cat=cat+i+delim
	
	cat=cat+args[-1]

	return cat

