def celsius_to_fahrenheit():
    f =p*9/5+32
    print(f)

def fahrenheit_to_celsius():
    c =  (fahrenheit - 32) * 5/9
    print(c)
def celsius_to_kelvin():
    r= p + 273.15
    print(r)

def kelvin_to_celsius():
    k= p-273.15
    print(k)

def fahrenheit_to_kelvin():
    m=(p-32)*5/9+273.15
    print(m)


def kelvin_to_fahrenheit():
    n= (p-273.15)*9/5+32
    print(n)


p=int(input("ENTER THE VALUE OF TEMPERATURE: "))
h=int(input("Conversion type Enter 1 for cel to far, enter 2 for far to cel, enter 3 for cel to kel, enter 4 for kel to cel, enter 5 for far to kel, enter 6 for kel to far"))

if h==1:
    celsius_to_fahrenheit()

elif h==2:
    fahrenheit_to_celsius()

elif h==3:
    celsius_to_kelvin()

elif h==4:
    kelvin_to_celsius()

elif h==5:
    fahrenheit_to_kelvin()

elif h==6:
    kelvin_to_fahrenheit()























