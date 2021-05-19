import json

class Productie:
    def productie_frigidere(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            if data["tevi"] >= 20 and data["placi metal"] >= 5:
                data["tevi"] = data["tevi"] - 20
                data["placi metal"] = data["placi metal"] - 5
                with open('produse.json.', "r") as g:
                    date = json.load(g)
                    date["frigidere"] = date["frigidere"] + 1
                with open('produse.json', 'w') as g:
                    json.dump(date, g, indent=2)
            else:
                stock_insuficient = "Nu sunt destule materiale in stoc!\nCere unui gestionar sa adauge materiale!"
                return print(f"\n{stock_insuficient}\n ")

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)
        print("Ai asamblat frigider")
        print()
    def productie_cuptor_microunde(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            if data["placi electronice"] >= 10 and data["plastic"] >= 20 and data["foi metal"] >=6:
                data["placi electronice"] = data["placi electronice"] - 10
                data["plastic"] = data["plastic"] - 20
                data["foi metal"] = data["foi metal"] - 6
                with open('produse.json.', "r") as g:
                    date = json.load(g)
                    date["cuptoare cu microunde"] = date["cuptoare cu microunde"] + 1
                with open('produse.json', 'w') as g:
                    json.dump(date, g, indent=2)
            else:
                stock_insuficient = "Nu sunt destule materiale in stoc!\nCere unui gestionar sa adauge materiale!"
                return print(f"\n{stock_insuficient}\n ")

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)

        print("Ai asamblat cuptor cu microunde")
        print()

    def productie_aragaz(self):
        with open('stocuri.json.', "r") as f:
            data = json.load(f)
            if data["tevi"] >= 10 and data["placi metal"] >= 2 and data["foi metal"] >= 5:
                data["tevi"] = data["tevi"] - 20
                data["placi metal"] = data["placi metal"] - 2
                data["foi metal"] = data["foi metal"] - 5
                with open('produse.json.', "r") as g:
                    date = json.load(g)
                    date["frigidere"] = date["frigidere"] + 1
                with open('produse.json', 'w') as g:
                    json.dump(date, g, indent=2)
            else:
                stock_insuficient = "Nu sunt destule materiale in stoc!\nCere unui gestionar sa adauge materiale!"
                return print(f"\n{stock_insuficient}\n ")

        with open('stocuri.json', 'w') as f:
            json.dump(data, f, indent=2)
        print("Ai asamblat aragaz")
        print()
