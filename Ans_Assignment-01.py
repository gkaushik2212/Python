#1
print ('Hello My name is "Kaushik". I love coding')
print ("This is 'my first program'.")


x = input("Enter value for x:")
y = input("Enter value for y:")
z = input("Enter value for z:")

def info():
    x=print("Value1= "+x)
    y=print("value2= "+y)
    z=print("value3= "+z)
    return
type(x),type(y),type(z)

#2
print('Hello! My name is XYZ')
print('"Hello i am candidate"')
print('"234.56"')
print('"34"')
print('a+3j')

#3
def y():
    x=10+20*(45+67.0)
    return
print (x)
print(type(x))

x=(True & False) | False
print(type(x),+ x)

x=(True | True) & (~ False & True)
print(type(x),+ x)

x = (3>89) | (34>32)
print(type(x),+ x)

x= ~True & False
print(type(x),+ x)

#4
number = int(input("Enter a number:"))
if((number % 2 ==0)and (number % 5==0)):
    print('Hurray is is what i am looking for')
else:
    print('Wrong input')

#5
 x = int(input("Enter a integer"))
if x in range(10,50):
    print("Yes i am in the range")
else:
    print("Oops")
    
