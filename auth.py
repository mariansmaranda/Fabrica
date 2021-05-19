from menus import Menu
import json

class Auth:
    users_file = open("users.json", "r")
    users_dict = json.load(users_file)

    def login(self):
        while True:
            global user
            user = input("User\n>").lower()
            for i in self.users_dict["manageri"]:
                if user in i["ID"]:
                    password = input("Password:\n>").lower()
                    if password in i["password"]:
                        print("Logged as Manager")
                        Menu.meniu_manager(self)
                    else:
                        print("parola incorecta")
                    return user
            for j in self.users_dict["operatori"]:
                if user in j["ID"]:
                    password = input("Password:\n>").lower()
                    if password in j["password"]:
                        print("Logged as Operator")
                        Menu.meniu_operator(self)
                    else:
                        print("parola incorecta")
                    return user
            for k in self.users_dict["gestionari"]:
                if user in k["ID"]:
                    password = input("Password:\n>").lower()
                    if password in k["password"]:
                        print("Logged as Gestionar")
                        Menu.meniu_gestionar(self)
                    else:
                        print("parola incorecta")
                    return user

            else:
                print("User not found")