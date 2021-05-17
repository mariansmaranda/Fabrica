import json


class Stocuri:
    def adauga_stoc_tevi(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            data["tevi"] = data["tevi"] + int(input("Adauga tevi\n>"))

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)
        return data["tevi"]
    def adauga_stoc_placi_metal(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            data["placi metal"] = data["placi metal"] + int(input("Adauga placi metal\n>"))

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)
        return

    def adauga_stoc_placi_electronice(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            data["placi electonice"] = data["placi electonice"] + int(input("Adauga placi electronice\n>"))

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)



    def adauga_stoc_foi_metal(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            data["foi metal"] = data["foi metal"] + int(input("Adauga foi metal\n>"))

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)

    def adauga_stoc_plastic(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            data["plastic"] = data["plastic"] + int(input("Adauga plastic\n>"))

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)

# adaugare = Stocuri()
# adauga_tevi = adaugare.adauga_stoc_tevi()