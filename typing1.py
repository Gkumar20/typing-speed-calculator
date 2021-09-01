import datetime,os,random
repeat=True
while repeat==True:
    os.system("cls")
    No_of_lines=int(input("Enter number of lines for typing : "))
    with open("book.txt","r") as f:
        list1=f.readlines()

    print("You can typing start Now...\n")
    wrong1=[]
    wrong2=[]
    n=0
    while No_of_lines>n:
        choice1=random.choice(list1)
        print(f"\n{choice1}")
        t1=datetime.datetime.now().time().second
        typin_input=input("type Now... = ")
        t2=datetime.datetime.now().time().second
        char1=list(choice1.split())
        char2=list(typin_input.split())
        for index,item in enumerate(char1):
            try:
                if item != char2[index]:
                    wrong1.append(item)
                    wrong2.append(char2[index])
            except:
                pass
        n+=1

    print("\nYour Mistakes in these points : \n")
    for i,j in enumerate(wrong1):
        print(wrong2[i] ,"->", j)

    t=t2-t1
    print(f"speed of Typing is {len(char2)*60//t} WPM")
    inpt=input("for exit press='y' and to return for typing press='n': ")
    if inpt=='y':
        repeat=False
    elif inpt=='n':
        pass
    else:
        print("you entered wrong key...\n you can again typing")


