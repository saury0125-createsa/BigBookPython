"""this program is a generater of world map, and the map is made by the word that you entered"""
#初始化了地图，还有用于做index的i
bitmap = """
....................................................................
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
 ...................................................................."""
i=0

print("Enter the message to display with the bitmap.")
#检查message是否vaild
message=str(input(">"))
length=len(message)
if message=="":
    print("please enter the vaild input")

else:
    #bitmap.splitlines()是把多行的东西强制分成一个元素一行，相当于把worldmap变成了2D array
    for lines in bitmap.splitlines():
        for element in lines:
            if element==" ":
                print(" ",end="")
                #print("a",end="")代表不会换行
            elif element==".":
                print(element,end="")
            #using message to fill the * in the bitmap and calculate the message's index
            else:
                if i==length:
                    i=0
                    print(message[i],end="")#end=""的目的是不让print换行
                    i=i+1
                else:
                    print(message[i],end="")
                    i=i+1
        print()#in order to change print the second line 换行作用