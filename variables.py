#
# Example file for working with variables
#

# Declare and init
f = 0;
print f

# Re-declare
f = "abc";
print f

# Re-declare
#print "string type " + 123
print "string type " + str(123)

# Global vs local variables in functions
def someFunction():
	#local
	f = "local def"
	print f

def someFunction2():
	global f
	f = "global def"
	print f

someFunction()
someFunction2()
print f

# Undefine variable in real time
#del f
#print f
