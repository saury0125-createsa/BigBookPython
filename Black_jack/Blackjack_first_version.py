"""this program is a 21 points gambling simulator"""
import random
import sys
instructions="""Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
Money: 5000
How much do you bet? (1-5000, or QUIT)"""

#general variables
choice="(H)it, (S)tand, (D)ouble down"
HEARTS   = chr(9829) # Character 9829 is '♥'.
DIAMONDS = chr(9830) # Character 9830 is '♦'.
SPADES   = chr(9824) # Character 9824 is '♠'.
CLUBS    = chr(9827) # Character 9827 is '♣'.
money=5000
o_stand=False
p_stand=False
i=2
card_table_p=[]
card_table_o=[]
score_o=0
score_p=0

print(instructions)
beti=str(input(">"))
if beti=="quit" or beti=="QUIT":
    sys.exit()
else: bet=int(beti)   
if bet<1 or bet>5000:
    print("please enter the vaild number")
else:
    print("Bet: ",bet)

def choose_card():
    #生成选择的牌的点数以及花色
    number=random.randint(1,13)
    card_color_n=random.randint(1,4)
    #把牌花色的概率转换为花色符号
    if card_color_n==1:
        card_color=HEARTS
    elif card_color_n==2:
        card_color=DIAMONDS
    elif card_color_n==3:
        card_color=SPADES
    else:
        card_color=CLUBS
    return number,card_color

#Because JQK都算10，所以这是一个cardnumber-cardvalue的转换器
def card_value(card_number):
    if card_number>=10:
        card_value=10
    else :
        card_value=card_number
    return card_value

def first_r():
    global o_stand,p_stand
    # 1st round
    o_numberf,o_colorf=choose_card() #雇主
    o_valuef=card_value(o_numberf)
    o_numbers,o_colors=choose_card()
    o_values=card_value(o_numbers)

    if (o_valuef==1 and (11+o_values)<=21): score_o=11+o_values
    elif o_values==1 and (11+o_valuef)<=21: score_o=11+o_valuef
    else: score_o=o_values+o_valuef
    
    if score_o>=17:
        o_stand=True
    #if owner的分>=17那么以后owner无法抽卡

    #因为雇主是机器人，所以默认雇主选择点数更接近21点的你那个

    print("DEALER: ???")
    print_card(o_numberf,o_colorf,False,False)
    print_card(o_numbers,o_colors,False,False)
    print()

    #玩家
    p_numberff,p_colorf=choose_card()
    p_numberf=card_value(p_numberff)
    p_numberss,p_colors=choose_card()
    p_numbers=card_value(p_numberss)

    #因为要print玩家的点数，而这又有些麻烦，所以下面一段是用来判断的
    if p_numbers!=1 and p_numberf!=1:
        score=p_numberf+p_numbers
    else:
         #如果有1个A且相加小于21 那么应该问player怎么选
         #如果大于21，则不问直接返回score等于相加
         #如果2个A 则问两个A都算1还是其中1个A算11

        if p_numberf==1 and p_numbers==1:#情况三
            print("you have two A plase choose one of the following options")
            print("option(1):Let your total score be 2")
            print("option(2):Let your total score be 12")
            chose=int(input(">"))
            if chose!=1 and chose!=2:
                print("please input the vaild answears")
            else:
                if chose==1:
                    score=2
                else:
                    score=12

        elif p_numberf==1 and 11+p_numbers<=21:
            print("you have two A plase choose one of the following options")
            score_f=1+p_numbers
            score_s=11+p_numbers
            print(f"option(1):Let your total score be {score_f}")
            print(f"option(2):Let your total score be {score_s}")
            chose=int(input(">"))
            if chose!=1 and chose!=2:
                print("please input the vaild answears")
            else:
                if chose==1:
                    score=score_f
                else:
                    score=score_s
                
        elif p_numbers==1 and 11+p_numberf<=21:
                print("you have two A plase choose one of the following options")
                score_f=1+p_numberf
                score_s=11+p_numberf
                print(f"option(1):Let your total score be {score_f}")
                print(f"option(2):Let your total score be {score_s}")
                chose=int(input(">"))
                if chose!=1 and chose!=2:
                    print("please input the vaild answears")
                else:
                    if chose==1:
                        score=score_f
                    else:
                        score=score_s
        else:score=p_numberf+p_numbers

    print(f"PLAYER: {score}")
    print_card(p_numberff,p_colorf,True,True)
    print_card(p_numberss,p_colors,True,True)#在这里ff和ss是number也就是13=13 而不是13=10这种value
    #明面上是print雇主的其中一个牌first 但实际上要返回雇主的值和玩家的值
    #如果没人赢，进入下一轮 否则game_over
    if score>=21 or score_o>=21:
        game_over(score,score_o)
        return
#######################################如果第一轮没结束，那么进入action环节
    else:actions(score,score_o)

def display(isPlayer):
     global card_table_p,card_table_o
     if isPlayer:
         card_table=card_table_p
     else:card_table=card_table_o
     for a in range(4):
        row = "".join(c[a] for c in card_table)
        print(row)
     

def final_open(p,o):
    print(f"PLAYER: {p}")
    display(True)
    print()
    print(f"DEALER: {o}")
    display(False)
    print()

def continue_play():
    global money,bet,p_stand,o_stand,i
    i=2
    p_stand=False
    o_stand=False

    print(f"Money: {money}")
    print(f"How much do you bet? (1-{money}, or QUIT)")
    response=input(">")
    if response=="quit" or response=="QUIT":
        sys.exit()
    else:bet=int(response)
    if 1<=bet<=money:
        first_r()
    else:print("please input the vaild number"),sys.exit()

def game_over(player,owner):
    global money,bet,card_table_p,card_table_o
    if player==owner or (player>21 and owner>21):
        print("You won $0")
    elif player>21 or(owner<=21 and player<owner):
        print(f"You lost {bet}!")
        money=money-bet
    else:
        print(f"You won {bet}!")
        money=money+bet
    print("game over")
    see=str(input("do you want to see the final card_board?(y/n)"))
    if see=="y" or see=="Y":
        final_open(player,owner)
    card_table_o=[]
    card_table_p=[]
    if money<=0:
        print("You are bankrupt.")
        sys.exit()
    else:
        continue_play()
    return 

def print_card(card_number,card_color,is_show,is_play):
    global card_table_o,card_table_p
    #一次打印一张牌 
    line1,line2,line3,line4="","","",""
        #如果不隐藏牌
        #把特殊符号的数字变成相应的符号
    if card_number==1: show_number="A"
    elif card_number==11: show_number="J"
    elif card_number==12: show_number="Q"
    elif card_number==13: show_number="K"
    else: show_number=card_number#不特殊的数字依旧是数字

    line1=" ___ "
    line2=f"|{show_number}  |"
    line3=f"| {card_color} |" 
    line4=f"|__{show_number}|"
    if card_number==10:
        line2=f"|{show_number} |"
        line4=f"|_{show_number}|"
    card=[line1,line2,line3,line4]
    if is_play:
        card_table_p.append(card)
        for i in range(4):
         row = "".join(c[i] for c in card_table_p)
         print(row)
    else:
        card_table_o.append(card)

        if is_show:
            for i in range(4):
                row = "".join(c[i] for c in card_table_o)
                print(row)
    #我现在在想一种收集牌上牌桌的方法 可能是一个2D list global variable那种，就是相当于执行一次存一次，依赖于
    #这个def里面尚未创建的count(count第一次=0)这样可以做index
    #而且甚至于可以就不用printline1-4了，直接print那个array就可以了
        else:
        #如果要隐藏牌的话
            line1 = " ___ "
            line2 = "|## |"
            line3 = "|###|"
            line4 = "|_##|"
            card_table_oh = card_table_o.copy()
            card_table_oh[0]=[line1,line2,line3,line4]
            for i in range(4):
                row = "".join(c[i] for c in card_table_oh)
                print(row)
"""刚刚我已经处理了 开局bet 第一次抽牌并显示点数 print牌 裁定胜负 而之后则建立在第一次没有结束上
    相当于while ((玩家<=21 and 庄主<=17) or Continu )---在这里continu是boolean 如果是双方都Standing那么continu
    就会变成False"""

def actions(player,owner):
    global o_stand,i,p_stand,bet,score_o,score_p
    while True:
        if i==2:
            score_o=owner
            score_p=player
#determine if owner can hit(score<17)
        if score_o>=17:
            o_stand=True
            if p_stand:
                game_over(score_p,score_o)
                return
#为了游戏美观其实是也可以想办法加show一下最后的牌在gameover之前
        else:
        #如果没有owner继续开抽
            print()
            print("dealer begin their second round")
            o_number,o_color=choose_card()
            o_value=card_value(o_number)
        #这里是看owner的number value 和 color
            score_o=o_value+score_o
            
            if o_number==1 and score_o+10<=21:
                score_o=score_o+10

            elif score_o>=21:
               #print_card()
                 print(f"DEALER: {score_o}")
                 print_card(o_number,o_color,True,False)
                 game_over(score_p,score_o)
                 return
            
            print()
            print(f"DEALER: {score_o}")
            print_card(o_number,o_color,True,False)

            
            #谁先爆牌谁over
        if not p_stand:
            print("choose:(H)it, (S)tand, (D)ouble down")
            actions=str(input(">"))

            if actions=="H" or actions=="h":
                number,color=choose_card()
                p_value=card_value(number)
                score_p=score_p+p_value
                print(f"You drew a {number} of {color}.")
                print()
                print(f"DEALER: {score_o}")
                for a in range(4):
                         row = "".join(c[a] for c in card_table_o)
                         print(row)
                print(f"PLAYER: {score_p}")
                print_card(number,color,True,True)
         #就是之前的分加上新分
        
                if score_p>=21:
                    game_over(score_p,score_o)
                    return

                elif number==1 and score_p+10<=21:
                    choose=int(input(f"choose:(1)--total score = {score_p} and (2)---total score = {score_p+10}" ))
                    if choose==2:
                     score_p=score_p+10
                    elif choose!=1:
                        print("please input the vaild number")
                        return

            elif actions=="S" or actions=="s":
                    p_stand=True
                    if p_stand and o_stand:#相当于两个人都stand触发结算
                        game_over(score_p,score_o)

            elif actions=="D" or actions=="d":
                if i==2:
                        bet=2*bet
                        number,color = choose_card()
                        p_value = card_value(number)
                        score_p = score_p + p_value
                        print(f"You drew a {number} of {color}.")
                        print()
                        print(f"DEALER: {score_o}")
                        for b in range(4):
                            row = "".join(c[b] for c in card_table_p)
                            print(row)
                        print(f"PLAYER: {score_p}")
                        print_card(number,color,True,True)
            
                        if score_p>=21:
                           game_over(score_p,score_o)
                           return

                        elif number==1 and score_p+10<=21:
                            choose=int(input(f"choose:(1)--total score = {score_p} and (2)---total score = {score_p+10}" ))
                            if choose==2:
                                score_p=score_p+10
                            elif choose!=1:
                                print("please input the vaild number")
                                return

                        p_stand = True
                else:
                    print("since this isn't the second round,you can't do that")
                    return    #down
            else:
                print("please input the vaild answear")
                return
        i=i+1

first_r()


