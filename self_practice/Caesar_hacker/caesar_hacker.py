import string
A_Z = list(string.ascii_uppercase)

def de_cipher(sentence,key):
    global A_Z
    final=[]
    j=0
    is_find=False
    print(f"Key #{key}: ")
    for i in sentence:
        j=0
        while j<=len(A_Z)-1 and is_find==False:
            if i==A_Z[j]:
                is_find=True
                if j+key>=0:
                    final.append(A_Z[j-key])
                else:
                    final.append(A_Z[j+key+26])
            j+=1
        if is_find==False:
            final.append(i)
        is_find=False

    for k in final:
        print(k,end='')

def main_menu():
    print("Enter the encrypted Caesar cipher message to hack.")
    sentence=input("> ")
    sentence=sentence.upper()
    for i in range(7):
        de_cipher(sentence,i)
        print()
    
    return

main_menu()