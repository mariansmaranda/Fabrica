import json

class Angajator:

    def angajator_manager(self):
        with open("users.json") as json_file:
            data = json.load(json_file)
            temp = data["manageri"]
            y = {
                "ID": input("ID Manager nou\n> ").lower(),
                "nume": input("Nume manager nou\n> ").capitalize(),
                "prenume" : input("Prenume Manager nou\n> ").capitalize(),
                "password": "qwe",
                "CNP": input("CNP Manager nou\n> "),
                "telefon": input('Telefon Manager nou\n> '),
                "oras": input("Oras Manager nou\n> ").capitalize()
                }
            temp.append(y)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)

    def angajator_operator(self):
        with open("users.json") as json_file:
            data = json.load(json_file)
            temp = data["operatori"]
            y = {
                "ID": input("ID Operator nou\n> ".lower()),
                "nume": input("Nume Operator nou\n> "),
                "prenume" : input("Prenume Operator nou\n> "),
                "password": "qwe",
                "CNP": input("CNP Operator nou\n> "),
                "telefon": input('Telefon Operator nou\n> '),
                "oras": input("Oras Operator nou\n> ")
                }
            temp.append(y)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)

    def angajator_gestionar(self):
        with open("users.json") as json_file:
            data = json.load(json_file)
            temp = data["gestionari"]
            y = {
                "ID": input("ID Gestionar nou\n> ").lower(),
                "nume": input("Nume Gestionar nou\n> "),
                "prenume" : input("Prenume Gestionar nou\n> "),
                "password": "qwe",
                "CNP": input("CNP Gestionar nou\n> "),
                "telefon": input('Telefon Gestionar nou\n> '),
                "oras": input("Oras Gestionar nou\n> ")
                }
            temp.append(y)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)
