class User:
    def __init__(self, username):
        self.username = username
        self.hoes = []
    def get_username(self):
        return self.username
    def add_hoes(self,thingBEY):
        self.hoes.append(thingBEY)
    def get_hoes(self,hoes):
        blah = " "
        for r in self.friends:
            blah += r.get_username()
        return blah

class Network:
    def __init__(self):
        self.users = []
    def add_user(self, human):
        self.users.append(human)
    def add_another(self, sexybot):
        self.users.append(sexybot)
    def get_users(self):
        return self.users

def main():
    print("Welcome to SexyMeetings.co")
    thing = input("To create an account, press (c) \n")

    if (thing == "c"):
        thing2 = input("CHose a UsR Nme \n")
        human = User(thing2)
        print ("Your new username is", thing2)
        my_network = Network()
        my_network.add_user(human)
        list_users = my_network.get_users()
        sex = True
        while sex == True:
            thing3 = input("To view other users, press (v) \nTo add a hoe, user press (a) \nTo view your friends, press (f) \nTo create another user, press (c)\n")
            if (thing3 == "v"):
                for person in list_users:
                    print ("User:", person.get_username())

            if (thing3 == "a"):
                print("u wanna make hoes w which hoe??? ;)")
                hoe1 = input("HOE1: \n")
                hoe2= input("HOE2: \n")
                isUser = False
                for i in list_users:
                    #PROBLEM HOES
                    if (hoe1 == i.get_username()):
                        isuUser=True
                        for y in list_users:
                            if (hoe2 == y.get_username):
                                isUser3 = True
                                i.add_hoes(y)
                                y.add_hoes(i)
                                print(hoe1, " and", hoe2, " are now friends")
                        if (isUser == False):
                            print("\n One or both of these are not valid")

            if (thing3 == "f"):
                print("WHo u wanna see?")
                thing6 = input("Username:")

                isUser2 = False
                for x in list_users:
                    if (thing6 == x.get_username()):
                        isUser2=True
                        print(thing6 + "'s hoes list is:'")
                        print(x.get_hoes())
                            # print
                    if (ifUser2 == False):
                        print("\n", thing6 + "is not a user")


            if (thing3 == "c"):
                thing5 = input("Chose an new usr\n")
                print("Ur usrnae is", thing5, "\n")
                sexybot = User(thing5)
                my_network.add_another(sexybot)


main ()


# Se
