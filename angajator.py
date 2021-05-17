import json

class Angajator:

    def angajator_manager(self):
        with open("users.json") as json_file:
            data = json.load(json_file)
            temp = data["manageri"]
            y = {
                "ID": input("ID Manager nou\n> "),
                "nume": input("Nume manager nou\n> "),
                "prenume" : input("Prenume Manager nou\n> "),
                "parola": input("Parola Manager nou\n> "),
                "rol": "manager",
                "CNP": input("CNP Manager nou\n> "),
                "telefon": input('Telefon Manager nou\n> '),
                "oras": input("Oras Manager nou\n> ")
                }
            temp.append(y)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)

    def angajator_operator(self):
        with open("users.json") as json_file:
            data = json.load(json_file)
            temp = data["operatori"]
            y = {
                "ID": input("ID Operator nou\n> "),
                "nume": input("Nume Operator nou\n> "),
                "prenume" : input("Prenume Operator nou\n> "),
                "parola": input("Parola Operator nou\n> "),
                "rol": "operator",
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
                "ID": input("ID Gestionar nou\n> "),
                "nume": input("Nume Gestionar nou\n> "),
                "prenume" : input("Prenume Gestionar nou\n> "),
                "parola": input("Parola Gestionar nou\n> "),
                "rol": "gestionar",
                "CNP": input("CNP Gestionar nou\n> "),
                "telefon": input('Telefon Gestionar nou\n> '),
                "oras": input("Oras Gestionar nou\n> ")
                }
            temp.append(y)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)
