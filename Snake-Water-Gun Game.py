import random
# Snake Water Gun Game
print("This is Snake,Water,Gun Game!\n")
num=1
chance=0
p=input("Enter your name...")
humain_point=0
print("you have total inly 10 chance for play this game\n")
print(" Snake Water Gun Game!\n")
while(num<=10):

    d1={"1":"water","2":"gun","3":"snake"}
    list2=["water","gun","snake"]

    n=random.choice(list2)
    print("Enter 1, 2 or 3 for playing this Game")
    # print(n,"\n")#THIS IS USE FOR PRINTING THE RANDOM NUMBER USING BY THE COMPUTER!...
    op=input("Enter  \n1=> for WATER, \n2=> for GUN,\n3=> for SNAKE\t-> ")
    a=d1[op]
    print(f"{p} You choose water",a)

    if (n=="snake" and a=="water") or (n=="water" and a=="snake\n"):
        print("Snake can drink the water!\n")
        if (n=="water" and a=="snake"):
            print("You Won! the game\nBecause Snke can drink Water")
            print(f"Computer=> {n} \nAnd you choose=> {a}")
            humain_point=humain_point+1
            print(f"{p} Your Point is{humain_point}")


        elif (n=="snake" and a=="water"):
            print(f"{p} You loose the game\n"
                  "\bBecause snake drink the water")
            print(f"Computer=> {n} \nAnd you choose=> {a}")

    elif (n=="water" and a=="gun") or (n=="gun" and a=="water"):
        print("Water can spoil the Gun!")


        if (n=="gun" and a=="water"):
            print(f"{p} You Won! the Game...\nBecause Gun Can't fire in the Water")
            print(f"Computer=> {n} \nAnd you choose=> {a}")
            humain_point=humain_point+1
            print(f"{p} Your Point is{humain_point}")

        elif (n=="water" and a=="gun"):
            print(f"Computer=> {n} \nAnd you choose=> {a}")
            print(f"{p} You loose the Game\n")

    elif (n=="gun" and a=="snake") or (n=="snake" and a=="gun"):
        print("Gun kill the Snake!\n")

        if (n=="snake" and a=="gun"):
            print(f"{p} You Won! the Game\n Because Gun can kill the Snake")
            print(f"Computer=> {n} \nAnd you choose=> {a}")
            humain_point=humain_point+1
            print(f"{p} Your Point is{humain_point}")

        elif (n=="gun" and a=="snake"):
            print(f"{p} You Loose the Game \n Because Gun can Kill the Snake")
            print(f"Computer=> {n} \nAnd you choose=> {a}")

    elif n==a:
        print("Foul! \n Sorry you both choose same")
    print(10-num,"no. of chance you have to left\n")
    num=num+1
    print("")
    chance=chance+1
    print(chance,"chance you have used\n")
print(f"Your point is {humain_point}")
print("Thank's Python!")
input()
