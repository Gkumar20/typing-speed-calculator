import time
import random,os

decision=True
while decision:
    os.system('cls')
    with open("book.txt","r") as f:
        total_word=int(input("\nEnter total number word for typing : \n"))
        stored_words=f.read()
        k=stored_words.split()
        typing_stored_word=[]

    n1=0
    while total_word>n1:
        choice1=random.choice(k)
        typing_stored_word.append(choice1)
        n1+=1

    print("start the typing... \n\n")
    n=0
    wrong=[]
    corct=[]
    for i in typing_stored_word:
        print(i)
        time.sleep(1)
        t1 = time.time()
        inter=input("\nEnter printed word : ")
        t2 = time.time()
        if inter!=i:
            wrong.append(inter)
            corct.append(i)

    print(f"\nwrong typing word is  {wrong}\ncorrect in above wrong word is  {corct}")

    t = t2 - t1
    print(f"\nSpeed of typing : {total_word*60/t} word per minute\n")

    print("\nYou want again typing then press",'y','\nfor exit tap any key!!')
    dic=input()
    if dic!='y':
        decision=False
