#function w/o return type w/o parameter

def display():
    print("Hello friends")

display()


# w/o return type with parameter

def my_fun(x):
    print("your value is : ",x)

my_fun(54)

# with return value without parameter

print(">>>>>with return value without parameter")

def validate():
    num=int(input("enter even num : ")) #local parameter
    return num%2

if validate()==0:
    print("even")
else:
    print("Odd")


# with return value with parameter

print(">>>>>>>>>>>>>>>>>>with return value with parameter")


def prime(num):
    for i in range(2,num):
        if num%i==0 and num>2:
            print("Not a prime num")
            return num
        else:
            print("Prime num")
            return num


ip=int(input("Enter a number to check waether it's prime or not ? : "))
print("Your num is : ",prime(ip))








