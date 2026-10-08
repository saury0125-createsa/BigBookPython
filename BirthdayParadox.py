import random

def birthday_generater(c,numb):
    if numb>100 or numb<=0:
        print("plz enter the correct number")
        return
    list31=["Jan","Mar","May","Jul","Aug","Oct","Dec"]
    list30=["Apr","Jun","Sep","Nov"]
    finalist=[]
    i=1
    final=""
    while i<=numb:
        i+=1
        ranMonth=random.randint(1,12)
        if ranMonth<=7:
            ranDay=random.randint(1,31)
            Month=list31[random.randint(0,6)]
        elif ranMonth>7 and ranMonth<=11:
            ranDay=random.randint(1,30)
            Month=list30[random.randint(0,3)]
        else:
            ranDay=random.randint(1,29)
            Month="Feb"
        final=final+" "+f"{Month} {ranDay}"
        finalist.append(f"{Month} {ranDay}")
    if c!=0:
        print(f"Here are {numb} birthdays:\n"+final)
    return countMatch(c,finalist)

def countMatch(c,finalist):
    i=0
    repeat={}
    for a in finalist:
        for b in finalist:
            if a==b:
                i+=1
        if i>=2:
            repeat[a]=i
        i=0
    repeatlist=sorted(repeat,key=repeat.get)
    if len(repeatlist)!=0:
        if c==0:
            return True
        for name in repeatlist:
            print("In this simulation, multiple people have a birthday on "+name,end=", ")
        return True
    else: 
        if c==0:
            return False
        print("In this simulation no people have a same birthday")
        return False

def tenMillee():
    i=0
    sucess=0
    while i< 100000:
        i+=1
        if birthday_generater(0,people_size):
            sucess+=1
    p=float(sucess/100000)
    if p>0:
        print(f"""Out of 100,000 simulations of {people_size} people, there was a 
              matching birthday in that group {sucess} times. This means
that {people_size} people have a {p*100} % chance of
having a matching birthday in their group.
That's probably more than you would think!""")
    else:
        print(f"""Out of 100,000 simulations of {people_size} people, there was a 
              matching birthday in that group {sucess} times. This means
that {people_size} people have a {p*100} % chance of
having a matching birthday in their group.""")

people_size=int(input("How many birthdays shall I generate? (Max 100)"))
birthday_generater(1,people_size)
print(f"Generating {people_size} random birthdays 100,000 times...")
tenMillee()

    
