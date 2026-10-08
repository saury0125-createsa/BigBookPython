import random
import sys
class Card:
    def __init__(self,number,color):
        self.number=number
        if color==1: self.color=chr(9829)
        elif color==2:self.color=chr(9830)
        elif color==3:self.color=chr(9824)
        else:self.color=chr(9827)

    def cal_value(self):
        return 10 if self.number>=10 else self.number
    #value计算器

    def apperance(self):
        if self.number==1: show_number="A"
        elif self.number==11: show_number="J"
        elif self.number==12: show_number="Q"
        elif self.number==13: show_number="K"
        else: show_number=self.number#不特殊的数字依旧是数字
        
        line1=" ___ "
        line2=f"|{show_number}  |"
        line3=f"| {self.color} |" 
        line4=f"|__{show_number}|"
        if self.number==10:
            line2=f"|{show_number} |"
            line4=f"|_{show_number}|"

        return line1,line2,line3,line4
    

class Board: #print board
    def __init__(self,score):#person==1 dealer ==2 player
        self.score=score
    
    def print_board(self,person,card,line1,line2,line3,line4):
        self.person="Player"if person==1 else "Dealer"
        self.card=card  #card的类型就是card
        new1,new2,new3,new4=card.apperance()
        #这里是已有的board加上新的
       
        line1=line1+" "+new1
        line2=line2+" "+new2
        line3=line3+" "+new3
        line4=line4+" "+new4

        print()
        print(self.person+":"+str(self.score))
        print(line1)
        print(line2)
        print(line3)
        print(line4)
        print()

        return line1,line2,line3,line4

    def print_initial_dealer(self,card1,card2):
        new1,new2,new3,new4=card1.apperance()
        new2_hide="|#  |"
        new3_hide="| # |"
        new4_hide="|__#|" 
        new12,new22,new32,new42=card2.apperance()
        score=card1.cal_value()+card2.cal_value()
        print()
        print("Dealer: ##")
        print(new1+" "+new12)
        print(new2_hide+" "+new22)
        print(new3_hide+" "+new32)
        print(new4_hide+" "+new42)
        print()
        return new1+" "+new12,new2+" "+new22,new3+" "+new32,new4+" "+new42
    
    def initial_card(self):
        #相当于每局重置牌桌
        card_set=[]
        for i in range (52):
            card_set.append(i+1)

        return card_set

    def choose_card(self,card_set):
        #card_set就是每次抽卡 return new card set
        self.card_set=card_set
        n=len(self.card_set) #相当于处理随机的range
        current_card_index=random.randint(0,n-1)
        card=self.card_set[current_card_index] #card在牌堆中
        #根据card的大小返回牌number以及
        if card<=13:
            color=1
        elif card<=26:color=2;card=(card-13)%14
        elif card<=39:color=3;card=(card-13*2)%14
        else:color=4 ; card=(card-13*3)%14

        self.card_set.pop(current_card_index)

        return card,color,self.card_set
        #card指的是card的number

class Money:
    def __init__(self,current,bet):
        self.current=current
        self.bet=bet

    def start_bet(self):
        #判断用户输入的赌钱是否合理 所以我们在process上需要一个while
        if self.current-self.bet<0:
            print("invalid amount of bet")
            return
        else:
            print("Bet:",self.bet)
            
            return self.current,self.bet

    def win_lose(self,is_win):
        if is_win:
            self.current+=self.bet
        else:
            self.current-=self.bet
        return self.current


class Game:
    def dealer1_chose(self):
        boadrd1=Board(0)
        card_set=boadrd1.initial_card()#让牌堆初始化
        number1,color1,card_set=boadrd1.choose_card(card_set)
        card1=Card(number1,color1)#现在我们获得了card1的属性
        number2,color2,card_set=boadrd1.choose_card(card_set)
        card2=Card(number2,color2)#从牌堆里抽到了card2
        value=card1.cal_value()+card2.cal_value()
        boadrd1=Board(value)
        line1,line2,line3,line4=boadrd1.print_initial_dealer(card1,card2)
        #我们现在打印出来第一步的card1以及card2的牌桌
        return value,line1,line2,line3,line4,card_set

    def player1_chose(self,card_set):
        board1=Board(0)
        number1,color1,card_set=board1.choose_card(card_set)
        number2,color2,card_set=board1.choose_card(card_set)
        card1=Card(number1,color1)
        card2=Card(number2,color2)
        value=card1.cal_value()+card2.cal_value()
        line11,line12,line13,line14=card1.apperance()
        board1=Board(value)
        line1,line2,line3,line4=board1.print_board(1,card2,line11,line12,line13,line14)
        return value,line1,line2,line3,line4,card_set

    def game_over(self,owner,player,bet,money_user,list_d,list_p,is_double):#因为打印牌桌，所以应该会接受两个input
        bet=bet*2 if is_double else bet
        current=money_user.current
        money_user=Money(current,bet)
        if player==owner or (player>21 and owner>21):
            print("You won $0")
            current=money_user.current
        elif player>21 or(owner<=21 and player<owner):
            print(f"You lost {bet}!")
            current=money_user.win_lose(False)
        else:
            print(f"You won {bet}!")
            current=money_user.win_lose(True)
            print("game over")
        see=str(input("do you want to see the final card_board?(y/n)"))
        if see=="y" or see=="Y":#打印最终牌桌
            print()
            print("Dealer:",owner)
            for i in list_d:
                print(i)
            print()
            print("Player:",player)
            for j in list_p:
                print(j)
            print()
        if current<=0:
            print("You are bankrupt.")
            sys.exit()
        else:
            self.process(current)
            return True
            
            
        
    def main_menu(self):
        print("""Rules:
                 Try to get as close to 21 without going over.
                 Kings, Queens, and Jacks are worth 10 points.
                 Aces are worth 1 or 11 points.
                 Cards 2 through 10 are worth their face value.
                 (H)it to take another card.
                 (S)tand to stop taking cards.
                 On your first play, you can (D)ouble down to increase your bet
                 but must hit exactly one more time before standing.
                 In case of a tie, the bet is returned to the player.
                 The dealer stops hitting at 17.""")
        
        #先是print instruction，然后就是赌钱
        n=5000
        self.process(5000)
    
    def process(self,money):
        choice="(H)it, (S)tand, (D)ouble down"
        self.n=money
        is_double=False
        print("Money:",self.n)
        bet=(input(f"How much do you bet? (1-{self.n}, or QUIT)"))
        if bet=="quit" or bet=="QUIT":
            return
        else:
            money_user=Money(self.n,int(bet))
            while money_user.start_bet()==None or int(bet)<=0:
                bet=(input(f"How much do you bet? (1-{self.n})"))
                money_user=Money(self.n,int(bet))

        value_d,line1_d,line2_d,line3_d,line4_d,card_set=self.dealer1_chose()
        value_p,line1_p,line2_p,line3_p,line4_p,card_set=self.player1_chose(card_set)
        list_d=[line1_d,line2_d,line3_d,line4_d]
        list_p=[line1_p,line2_p,line3_p,line4_p]
        if value_d>=21 or value_p>=21:
            self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,False)
        else:##继续抽牌
            ##这里大概有个while
            con=True #con是while loop是否循环
            stand_d=stand_p=False
            while con:
                user_next=input(choice)
                if user_next.lower() in ('h','d'):
                    #if 是 h or d那么就是玩家开始继续抽牌
                    is_double=True if user_next.lower()=='d'else False
                    board_new=Board(value_p)
                    new_number,new_color,card_set=board_new.choose_card(card_set)
                    card_new=Card(new_number,new_color)
                    if card_new.number in (1,11,12,13):
                        if card_new.number==1: symbol="A"
                        elif card_new.number==11: symbol="J"
                        elif card_new.number==12: symbol="Q"
                        else:symbol="K"
                    else:symbol=card_new.number
                    print(f"You drew a {symbol} of {card_new.color}.")
                    value_p+=card_new.cal_value()
                    ###然后就是print最终牌桌
                    board_new=Board(value_p)
                    line1_p,line2_p,line3_p,line4_p=board_new.print_board(1,card_new,line1_p,line2_p,line3_p,line4_p)
                    list_p=[line1_p,line2_p,line3_p,line4_p]
                    #game_over这个def里面后面要进入新的循环，所以相当于在game_over这个def最后引用一个新方法
                    if value_p>=21:
                        con=False
                        self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,is_double)
                        break
                elif user_next.lower()=='s':
                    stand_p=True
                    if stand_p and stand_d:
                        con=False
                        self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,is_double)
                        break
                else:
                    print("plz input the valid choice")
                    sys.exit()

                if value_p>=21:
                    con=False
                    self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,is_double)
                    break
                else:
                    if value_d<17:
                        board_new_d=Board(value_d)
                        number_d,color_d,card_set=board_new_d.choose_card(card_set)
                        card_new_d=Card(number_d,color_d)
                        value_d+=card_new_d.cal_value()
                        board_new_d=Board(value_d)
                    
                        line1_d,line2_d,line3_d,line4_d=board_new_d.print_board(2,card_new_d,line1_d,line2_d,line3_d,line4_d)
                        list_d=[line1_d,line2_d,line3_d,line4_d]
                        if value_d>=21:
                            con=False
                            self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,is_double)
                            break
                        if is_double:
                            con=False
                            self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,is_double)
                            break
                    else:
                        stand_d=True
                        if stand_d and stand_p:
                            self.game_over(value_d,value_p,int(bet),money_user,list_d,list_p,is_double)
                            break
                    #else的话dealer不动牌

        
game1=Game()
game1.main_menu()