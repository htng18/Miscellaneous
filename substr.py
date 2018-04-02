def substr(word=None,position=1,length=None):

	""" This function is to extract an input word by its starting
		position and the length to be extracted. 
		
		Parameters:
		word: the input string to be extracted.
		poisition: starting position of the input string.
		length: the length of string to be extracted.

		For example,
		>>> substr('ABCDEFG',1,3)
		>>> 'ABC'
																"""

	if word is None:
		word = ''

	if not isinstance(word,str):
		raise TypeError("Input word must be a string.")

	if not isinstance(position,int):
		raise TypeError("Position must be an integer.")

	if not isinstance(length,int):
		raise TypeError("Length must be an integer.")

	if position<1:
		raise ValueError("Position must be larger than one.")

	if length<0:
		raise ValueError("Length must be larger than or equal to zero.")



	return word[position-1:position-1+length]


#print(substr("ABCDEFHI",1,3))