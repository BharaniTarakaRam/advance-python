#we can create a decarator function
def smartlogin(func):
	print("this is inside decarator function")
	#we can create a nested function
	def inner(uname,pword):
		if uname=="" and pword=="":
			print("Please enter username,password values")
		else:
			return func(uname,pword)
	return inner

@smartlogin  #it invokes decarator function
def login(uname,pword): #it is a normal function
	if uname=='ram' and pword=='kumar':
		print("valid username & password values")
	else:
		print("Invalid username & passsword values")

#test the appln
uname=input("enter username:")
pword=input("enter password:")

#accessing the function
login(uname,pword)







