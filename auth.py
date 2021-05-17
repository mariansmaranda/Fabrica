from menus import Menu
import json

class Auth:
    users_file = open("users.json", "r")
    users_dict = json.load(users_file)

    def login(self):
        while True:
            global user
            user = input("User\n>").lower()
            if user in self.users_dict["manageri"][0]["ID"]:
                password = input("Password:\n>")
                if password == self.users_dict["manageri"][0]["password"]:
                    global functie
                    functie = self.users_dict["manageri"][0]["rol"]
                    print("Logged as Manager")
                    Menu.meniu_manager(self)
                    return user
                else:
                    print("Password incorrect")
            elif user in self.users_dict["operatori"][0]["ID"]:
                password = input("Password:\n>")
                if password == self.users_dict["operatori"][0]["password"]:
                    functie = self.users_dict["operatori"][0]["rol"]
                    print("Logged as Operator")
                    Menu.meniu_operator(self)
                    return user
                else:
                    print("Password incorrect")
            elif user in self.users_dict["gestionari"][0]["ID"]:
                password = input("Password:\n>")
                if password == self.users_dict["gestionari"][0]["password"]:
                    functie = self.users_dict["gestionari"][0]["rol"]
                    print("Logged as Gestionar")
                    Menu.meniu_gestionar(self)
                    return user
                else:
                    print("Password incorrect")
            else:
                print("User not found")