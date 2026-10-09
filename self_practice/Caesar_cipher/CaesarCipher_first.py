import string
list_letter=list(string.ascii_uppercase)
#sentence默认是uppercase

def e_cipher(rank,sentence):#rank就是key
    """in this function it will receive two input : key and the sentence that
        needed to be encrypted and it will print the encryped sentence in 
        upper case

        >>> e_cipher(4,"Meet me by the rose bushes tonight.")
        QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
        
        """
    sentence=sentence.upper()
    j=k=0
    final=[]
    is_letter=False
    for i in sentence:
        while j<=len(list_letter)-1 and is_letter==False:
            if i==list_letter[j]:
                is_letter=True
                if j+rank<=len(list_letter)-1:
                    i=list_letter[j+rank]
                    final.append(i)
                else:
                    i=list_letter[j+rank-26]
                    final.append(i)
            j+=1
        if is_letter==False:
            final.append(i)
        is_letter=False
        j=0
    for k in final:
        print(k,end='')

def d_cipher(rank,sentence):
    """in this function it will receive two input : key and the sentence that
        needed to be decrypted and it will print the decryped sentence in 
        upper case
    
        >>> e_cipher(4,"QIIX QI FC XLI VSWI FYWLIW XSRMKLX.")
        MEET ME BY THE ROSE BUSHES TONIGHT.
            """
    sentence=sentence.upper()
    j=k=0
    final=[]
    is_letter=False
    for i in sentence:
        while j<=len(list_letter)-1 and is_letter==False:
            if i==list_letter[j]:
                is_letter=True
                #if j+rank<=len(list_letter)-1:
                if j-rank>=0:
                    i=list_letter[j-rank]
                    final.append(i)
                else:
                    i=list_letter[j-rank+26]
                    final.append(i)
            j+=1
        if is_letter==False:
            final.append(i)
        is_letter=False
        j=0
    for k in final:
        print(k,end='')
    

def main_menu():
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    choice=input("> ").lower()
    if choice not in ('e','d'):
        print("plz input the valid choice( e or d )")
        return
    key=int(input("Please enter the key (0 to 25) to use."))
    if key<0 or key>25:
        print("invalid key")
        return
    if choice=='e':
        print("Enter the message to encrypt.")
        sentence=input(">")
        e_cipher(key,sentence)
        print()
    else:
        print("Enter the message to decrypt.")
        sentence=input(">")
        d_cipher(key,sentence)
        print()

#e_cipher(4,"Meet me by the rose bushes tonight.")
#d_cipher(4,"QIIX QI FC XLI VSWI FYWLIW XSRMKLX.")