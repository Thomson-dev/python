name ='Tim'

print('Hi.\nhow are you')


print(name[0]) #print the first 
print(name.upper()) #

txt = "Hello welcome to my world"
x = txt.find("welcome")
print(x)

for x in "banana":
    print(x)

name = "Thomson"
print(len(name))    

#Check String
txt = "The best things in life are free"
if "free" in txt:
    print("free is present in text")


#Check if not String
txt ="The best things in life are free"

if "expensive" not in txt:
    print("expensive not present in txt")

#Slicing
b ="Hello world"
print(b[2:5])   
print(b[:5])


a = "Hello,world"
print(a.replace('H', 'J'))


#Split
print(a.split(","))


#Format
age =35
txt = "My name is Thomson and i'm {}"
print(txt.format(age))


quantity=3
item = 100
price = 49.50

txt = "I want to pay {2} dollar for {0} piece of item {1}"

print(txt.format(quantity, item, price))