import random
playerName_1 = str(input("please enter your name : "))
choicePoint = int(input("please enter your choice Point : "))
point_1 = 0
point_2 = 0
print(f"points : {choicePoint}")
while True :
    print("1) rock")
    print("2) paper")
    print("3) scissors")
    print("----------------------------------------------------")

    randomNumber = random.randint(0,2)
    if randomNumber == 0:
        computerMove = "rock"
    elif randomNumber == 1:
        computerMove = "paper"
    elif randomNumber == 2:
        computerMove = "scissors"

    player_1 = (input("player_1 make your Move :"))
    print("----------------------------------------------------")

    if player_1 == "1":
        player_1 = "rock"
    elif player_1 == "2":
            player_1 = "paper"
    elif player_1 == "3":
            player_1 = "scissors"
    else:
        print("somthings wrong....")
    player_2 = computerMove
    print(f"player_1  Move : {player_1}")
    print(f"player_2  Move : {computerMove}")
    print("----------------------------------------------------")
    if player_1 == player_2:
        print("that is tie...")
        print(f"{playerName_1}: {point_1}")
        print(f"Computer: {point_2}")
    elif player_1 == "rock":
        if player_2 == "paper":
            point_2 +=1
            print(f"{playerName_1}: {point_1}")
            print(f"Computer: {point_2}")
        elif player_2 == "scissors":
            point_1 +=1
            print(f"{playerName_1}: {point_1}")
            print(f"Computer: {point_2}")
    elif player_1 == "paper":
        if player_2 == "scissors":
            point_2 +=1
            print(f"{playerName_1}: {point_1}")
            print(f"Computer: {point_2}")
        elif player_2 == "rock":
            point_1 +=1
            print(f"{playerName_1}: {point_1}")
            print(f"Computer: {point_2}")
    elif player_1 == "scissors":
        if player_2 == "rock":
            point_2 +=1
            print(f"{playerName_1}: {point_1}")
            print(f"Computer: {point_2}")
        elif player_2 == "paper":
            point_1 +=1
            print(f"{playerName_1}: {point_1}")
            print(f"Computer: {point_2}")
    else:
        print("somthings wrong....")
    if point_1 == choicePoint:
        print(f"{playerName_1} is win.....")
        point_1 = 0
        point_2 = 0
        exit =  str(input("Do you Want continue? :")).lower()
        if exit == "y":
            print("--------------------------------------------------------")
            playerName = str(input("Please Enter your Name : "))
            choicePoint = int(input("please Enter your choice Point :"))
            print("--------------------------------------------------------")
            continue
        elif exit == "n":
            break
    elif point_2 == choicePoint:
        print("Computer is win.....")
        point_1 = 0
        point_2 = 0
        exit =  str(input("Do you Want continue? :")).lower()
        if exit == "y":
            print("--------------------------------------------------------")
            playerName = str(input("Please Enter your Name : "))
            choicePoint = int(input("please Enter your choice Point :"))
            print("--------------------------------------------------------")
            continue
        elif exit == "n":
            break


