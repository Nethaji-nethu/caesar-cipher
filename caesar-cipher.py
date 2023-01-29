import string

def caesar(rotate_string, number_to_rotate_by):
	map_lowercase = string.ascii_lowercase[number_to_rotate_by:] + string.ascii_lowercase[:number_to_rotate_by]
	map_uppercase = string.ascii_uppercase[number_to_rotate_by:] + string.ascii_uppercase[:number_to_rotate_by]
	#print(map_lowercase)
	#print(map_uppercase)
	return rotate_string.translate(str.maketrans(string.ascii_lowercase,map_lowercase)).translate(str.maketrans(string.ascii_uppercase,map_uppercase))

input_text = input('Enter the cipher / plain text to decode / encode : ')
key = int(input('enter the key to encode (1 to 26) / decode (-1 to -26) : '))
print(caesar(input_text,key))
