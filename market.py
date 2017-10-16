my_file = open("list.txt", "r")
list=list(my_file.read())
my_file.close()
my_file=open("list.txt","w")
my_file.truncate()
class market(object):
  def __init__(self,name,number,price):
    self.name=name
    self.number=int(number)
    self.price=int(price)
def check(n):
  for self in list:
    if self.number==n:
      return self
num=input("how many kinds of things do you want to add?")
num=int(num)
for i in range(0,num):
   name=input("name?")
   number=input("number?")
   price=input("price?")
   name = market(name,number,price)
   list.append(name)
num=input("how many kinds of things do you want to delete?")
num=int(num)
for i in range(0,num):
   name=input("name?")
   list.remove(name)
for i in list:
  my_file.write(i.name)
my_file.close()
f=open("receipt.txt","w")
num=input("how many kinds of things do you buy?")
num=int(num)
total=0;
for i in range(0,num):
   name=input("name?If you don't know. Please enter a space.")
   number=input("number?If you don't know. Please enter a space. ")
   n = input("numbers?")
   n=int(n)
   if name!=" " :
     for i in list:
        if i.name==name:
           total+=n*i.price
           number=int(i.number)
     f.write(name + " " + str(number) + " " + str(n) + "\n")
     continue
   elif	name==" " and number!=" " :
     number=int(number)
     name=check(number)
     total+=n*name.price
     f.write(name + " " + number + " " + n + "\n")
     continue
   else:
     f.write("GO AWAY!!!\n")
f.write("total:")
f.write(str(total))
f.close()
