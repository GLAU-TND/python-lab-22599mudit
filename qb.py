try:
    print(2+'33')
except TypeError as e:
    print('Error2 handled',e)

try:
    h='mudit'
    h=float(h)
except ValueError as e:
    print('Error1 handled',e)

class Attributes(object): 
	pass

object = Attributes()
try:
    print (object.attribute) 
except AttributeError as e:
    print('error3 handled',e)
