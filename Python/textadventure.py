begin= input("Type Start to play"+"\n")
print(begin)

start= ("Helicopter of the Apes")
print(start)

one= "Caesar"
two= "Maurice"
three= "hooman"

cc1= "hide in the closet"
cc2= "run past guards"
cc3= "ride the elevator"

cc1_1= "5 secs"
cc1_2="30 secs"
cc1_3="1 min"

mm1= "hide inside the vents"
mm2= "jump over the military guards"
mm3="ride up the elevator"


choice= input("Type your character choice:"+" "+ one + "   " +  two + "   " + three + "\n")

#choice3= input()#For Maurice

if (choice == one):
    print(one)
    if(choice==one):
        print("Initiate Caesar the Leader Protocal")
        print("Your name is Caesar, and you lead the apes on this planet. Your mission is to reach the helicopter at the top of the building and escape to the jungle to recconect with your tribe. Avoid the humans to stay alive."+"\n")
        choice2= input("You're on the 20th floor and you hear footsteps, do you" +" "+ cc1+","+" "+ cc2 +","+" or "+ cc3+"\n")
        if (choice2==cc1):
            print("You have decided to hide in the closet.")
            choice3= input("How long do you wait? 5 secs, 30 secs, or 1 min."+ "\n")
            if (choice3==cc1_1):
                print("You exit the closet and as soon the the military sees you, they shoot you down. You're dead"+"\n"+"Game Over")
            elif (choice3==cc1_2):
                print("You run to the elevator and try to make your escape up to the top, but when it arrives, more guards come out. Bang Bang Plop, You're dead"+"\n"+"Game Over")
            elif(choice3==cc1_3):
                print("You wait inside the closet. You hear the elevator arrive as more guards come to sweep the floor. They pass you, you head out of the closet. But as soon as you do, you fall unconcious. There was a trap. You've been captured."+"\n"+"Caesar Protocol End.")
        elif(choice2==cc2):
            print("You have decided to run past the military guards.")
        elif (choice2==cc3):
            print("You have decided to take the easy way out and ride up the elevator. Congrats 'fearless leader'."+"\n"+"you win, yay.")

elif(choice== two):
    print(two)
    if(choice==two):
        print("Initiate Maurice the Orangutan Protocal")
        print("Your name is Maurice and your mission is to reach the helicopter at the top of the building in order to return very important information to Caesar in the jungle. Avoid the humans and stay alive.")

elif(choice== three):
    print(three)
    if(choice==three):
        print("You're hooman, piss off.")
        print("GAME OVER")
else:
    print("That is not a valid option, try again")
    print(choice)
