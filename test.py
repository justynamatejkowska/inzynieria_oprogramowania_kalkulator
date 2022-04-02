
def  hello(name):
	return "Hello" + str(name)
print ("jak miło cie widziec :)")

def odejmij(a,b):
	return a-b

def dodaj(a,b):
	wynik = float(a) + float(b)
	return wynik

pierwsza = input()
druga = input()
print (dodaj(pierwsza, druga))

def add_num(a,b):#function for multiplication
    multiply=a*b;
    return multiply; #return value
num1=int(input("input the number one: ")) #input from user for num1
num2=int(input("input the number one: ")) #input from user for num2
print("The product is",add_num(num1,num2)) #call te function 
