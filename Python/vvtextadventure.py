#Start Screen
begin= input("Type Start to play")
print(begin)

start= "Helicopter of the Apes"
print(start)

#Choice of Character
choice_one= "Caesar the Leader"
choice_two= "Maurice the Orangutan"
choice_three= "Hooman"

#Options to choose from
print("Type your character choice: ")
choices= input(choice_one + " " + choice_two + " " + choice_three + " ")

if (choice_one == choices):
    print(choice_one)

elif (choice_two == choices):
    print(choice_two)

elif (choice_three == choices):
    print(choice_three)

else:
    print ("Not a valid input")

#Mission
print ("Here's your mission: The objective is to safely reach the helicopter to go back home to the jungle."
"The following questions determine your fate. Choose wisely.")

#Response to Options
q_yes_1= "Yes"
q_no_1= "No"
q_s_1= input ("Do you want to hide inside the closet?")
q_s_2= input ("Do you want to jump over the guards?")
q_yes_2= "Yes"
q_no_2= "No"


#Options for questions
if (q_s_1 == q_yes_1):
    print("You will be locked in! Good luck trying to escape!")

elif (q_s_1 == q_no_1):
    print("Be cautious")

else:
    print ("Try again.")


if (q_s_2 == q_yes_2):
  	print("Remember your life is in the hands of the guards. Trying to resist will only lead to your demise!")

elif (q_s_2 == q_no_2):
  		print("Keep your eyes peeled! Danger surrounds you!")

else:
  print("Try again.")
