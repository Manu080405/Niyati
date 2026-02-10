l=[1,2,3,4,5,6,6,7,8,9,10]
s=0
for i in l:
  s=s+i

print("Sum : ",s)

def p_n(name="Manu",greeting="Hello"):
  print(f"{greeting} {name}")
p_n()

n=input("Enter the name : ")
a=int(input("Enter the age : "))
print("The name is ",n,"and age is ",a)


n=input("Enter the name : ")
a=int(input("Enter the age : "))
dic={}
dic[n]=a
print(dic)


min_balance=10000
pin=int(input("Enter tha Pin : "))
amt=int(input("Enter amount : "))
pincode=3456
if pin==pincode:
  if amt<min_balance:
    print("Suffiecient Money")
    print("Withdrawing",amt)
    min_balance=min_balance-amt
    print("Available balance : ",min_balance)
  else:
    print("Insufficient amount")
else:
  print("Inavlaid PIN")

f=open("/content/Demo.csv")

fn=f.readlines()
print(fn)

fs=[fn.strip() for fn in fn]
print(fs)

h1=fs[0]
print(h1)

dic={}

dic[h1]=0
print(dic)

headers = fs[0].split(',')

dic = {h: [] for h in headers}


for row in fs[1:]:
    values = row.split(',')
    for h, v in zip(headers, values):
        if v.isdigit():
            dic[h].append(int(v))
        else:
            dic[h].append(v)

print(dic)
