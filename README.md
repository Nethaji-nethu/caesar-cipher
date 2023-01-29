# caesar-cipher
To encrypt or decrypt caesar cipher. on in otherwords, rot N algorithm implementation in python3

There are many online tools which have implemented rot N (rotate by N characters) algorithm (in other words caesar-cipher).

It works like below.
key = 1
  mappings:
    | abcdefghijklmnopqrstuvwxyz is interpreted as below for each character. i.e, a is interpreted as z, b = a, c = b, d = c so on and z = a
    | zabcdefghijklmnopqrstuvwxy
similarly, 

say, key = 2
  mappings:
    | abcdefghijklmnopqrstuvwxyz is interpreted as below for each character.
    | yzabcdefghijklmnopqrstuvwx
    
The same way, if you want the rotation to be anticlockwise i.e, to the left, you can do the same thing by giving key value as negative

say, key = -1
  mappings:
    | abcdefghijklmnopqrstuvwxyz is interpreted as below for each character.
    | bcdefghijklmnopqrstuvwxyza
