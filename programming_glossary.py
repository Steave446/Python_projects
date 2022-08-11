glossary = {
	'print():' : '\nUsed to print text and functions to the CLI.\n\nArguments:\nReferences (i.e. defined values)\nText (contained within single or double quotations)\nMixed - can mix text and functions by using (f"text{function(argument)}")\n',
	'sleep()' : '\nUsed to pause script for set amount of time, in seconds.\nNot a built in function; must be imported before execution with "import sleep from time"\n\nArguments:\nIntegers - represents time in seconds\n\t(can use decimal values)',

}

for term in glossary:
	print(term, glossary.get(term))
	print("\n-----------\n")