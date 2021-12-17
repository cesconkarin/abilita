print("Esercizi list_eeeeee")
l=[]
import math
k=["Karin","Cescon"]


print(k[1])
m=[0,1,2,3,4]
print(m[0:3])
print(m[-4])
m[0:3]
print(m)


a=range(8)
b=[int((x*3)+math.pi) for x in a]
c=[x*3 for x in a]
print(b[0:6])
print(c[0:6])



l=list(range(1000000))
v=list(range(10000))
t1=time.perf_counter()
s=l+v
t2=time.perf_counter()
print("+execution time: :", t2-t1, "s")
t3=time.perf_counter()
l.extend(v)
t4=time.perf_counter()
print("extend execution time:", t4-t3, "s")


stack=[1,2,3,4]
print("initial stack:", stack)
for i in range (5,7):
  stack.append(i)
print("append:", stack)
stack.pop()
print("pop:", stack)


tup1=()
print(tup1)

tup2=(20,)
print(tup2[0])

tup3= 1,2,3,4
print(tup3)
print(tup3[2])
#del(tup3)
#print("dopo aver cancellato:", tup3)

print(len(tup3))
tup4=tup3+tup2
print(tup4)
print("il massimo è",max(tup4))


#dictionary
#dictionary with integer keys
my_d1={1:"apple", 7:"flower"}
my_d2=dict({1:"apple", "fiore":"flower"})
print(my_d1[1], my_d1[7])
print(my_d1.get(7))
print(my_d2[1], my_d2["fiore"])
print(my_d2.get("fiore"))

my_d2["fiore"]="tulip"
print(my_d2.get("fiore"))

my_d2["landscape"]="sea"
print(my_d2.get("landscape"))
print(my_d2)
print(my_d2.pop(1))
print(my_d2)
print(len(my_d2))
print(type(my_d2))



number=23
guess=int(input("enter an integer:"))

if guess == number:
 print("congrats, you've guessed it!")
elif guess < number:
  print("no, it's a little higher than that")
else:
  print("no, it's a little lower than that")
print("done")

number=18
running = True

while running:
  guess=int(input("enter an integer:"))

  if guess == number:
    print("congrats, you've guessed it!")
    running = False
  elif guess < number:
    print("no, it's a little higher than that")
  else:
    print("no, it's a little lower than that")
else:
  print("The while lop is over")
print("done")

