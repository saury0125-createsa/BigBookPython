#bagels
import random
#i=0
start=False
while start==False:
    start=True
    bagel=False
    real_number=random.randint(100,999)
    print(real_number)
    gewei=real_number%10
    shiwei=((real_number-gewei)%100)//10
    baiwei=(real_number-gewei-shiwei)//100
    print("""Bagels, a deductive logic game.
    By Al Sweigart al@inventwithpython.com
    I am thinking of a 3-digit number. Try to guess what it is mn.
    Here are some clues:
    When I say:    That means:
    Pico         One digit is correct but in the wrong position.
    Fermi        One digit is correct and in the right position.
    Bagels       No digit is correct.
    I have thought up a number.
    You have 10 guesses to get it.
    在这个程序里，如果你输入了三位数以上的数，我们会自动删掉你千位以及以上的位数,并且不会说你猜对了""")
    i=0
    while i<10:
        i+=1
        g=s=b=bagel=False
        guess=int(input(f"Guess #{i}:"))
        if guess==real_number:
            print("You got it!")
            re=input("Do you want to play again? (yes or no)")
            if re=="yes":
                start=False
                i=0
                break
            else:
                print("Thanks for playing!")
                break
        else:
            g_gewei=guess%10
            g_shiwei=((guess-g_gewei)%100)//10
            g_baiwei=(guess-g_gewei-g_shiwei)//100
            c=g_baiwei
            if c>=10:
                g_baiwei=c%10
            if gewei==g_gewei:
                print("Fremi")
                bagel=True
                g=True
            if shiwei==g_shiwei:
                print("Fremi")
                bagel=True
                s=True
            if baiwei==g_baiwei:
                print("Fremi")
                bagel=True
                b=True
            if (gewei==g_baiwei or gewei==g_shiwei)and g==False:
                print("Pico")
                bagel=True
            if (baiwei==g_shiwei or baiwei==g_gewei)and b==False:
                print("Pico")
                bagel=True
            if (shiwei==g_gewei or shiwei==g_baiwei)and s==False:
                print("Pico")
                bagel=True
            if bagel==False:
                print("Bagels")
        if i==10 and start==True:
            re=input("Do you want to play again? (yes or no)")
            if re=="yes":
                start=False
                i=0
                break
            else:
                print("Thanks for playing!")
                break


    