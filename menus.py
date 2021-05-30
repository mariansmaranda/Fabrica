import json
from angajator import Angajator
from stocuri import Stocuri
from productie import Productie

class Menu:
    def meniu_manager(self):
        while True:
            meniu = ["1.Angajeaza Manager", '2.Angajeaza Operator', '3.Angajeaza Gestionar', '4.Afiseaza Angajatii',
                     "5.Log Out"]

            for submeniu in meniu:
                print(submeniu)
            optiune = input('> ')
            if optiune == '5':
                print('Logging Out...')
                break
            elif optiune == "1":
                Angajator.angajator_manager(self)
                pass
            elif optiune == "2":
                Angajator.angajator_operator(self)
                pass
            elif optiune == "3":
                Angajator.angajator_gestionar(self)
                pass
            elif optiune == "4":
                with open("users.json", "r") as u:
                    angajati = json.load(u)
                    print("Manageri")
                    print(20 * "=")
                    for i in angajati["manageri"]:
                        j = f'{i["nume"]} {i["prenume"]}'
                        print(j)
                    print(20 * "=")
                    print()
                    print("Operatori")
                    print(20 * "=")
                    for k in angajati["operatori"]:
                        l = f'{k["nume"]} {k["prenume"]}'
                        print(l)
                    print(20*"=")
                    print()
                    print("Gestionari")
                    print(20 * "=")
                    for m in angajati["gestionari"]:
                        n = f'{m["nume"]} {m["prenume"]}'
                        print(n)
                    print(20 * "=")
                    print()
                pass
            else:
                print()
                print("Alege una din optiunile afisate!")
                print()

    def meniu_operator(self):
        while True:
            meniu = ['1.Asambleaza Frigider', '2.Asambleaza Microunde', '3.Asambleaza aragaz',
                     '4.Log Out']
            for submeniu in meniu:
                print(submeniu)
            optiune = input('> ')
            if optiune == '4':
                print('Logging Out...')
                break
            elif optiune == "1":
                Productie.productie_frigidere(self)
            elif optiune == "2":
                Productie.productie_cuptor_microunde(self)
            elif optiune == "3":
                Productie.productie_aragaz(self)
            else:
                print()
                print("Alege una din optiunile afisate!")
                print()

    def meniu_gestionar(self):
        while True:
            meniu = ['1.Verifica Stock', '2.Adauga Tevi','3.Adauga Placi Metal','4.Adauga Placi Electronice',
                     '5.Adauga Foi Metal' ,'6.Adauga Plastic' , '7.Log Out']
            for submeniu in meniu:
                print(submeniu)
            optiune = input('> ')
            if optiune == '7':
                print('Logging Out...')
                break
            elif optiune == "1":
                with open("stocuri.json", "r") as s:
                    stoc = json.load(s)
                    print(stoc)
            elif optiune == "2":
                Stocuri.adauga_stoc_tevi(self)
            elif optiune == "3":
                Stocuri.adauga_stoc_placi_metal(self)
            elif optiune == "4":
                Stocuri.adauga_stoc_placi_electronice(self)
            elif optiune == "5":
                Stocuri.adauga_stoc_foi_metal(self)
            elif optiune == "6":
                Stocuri.adauga_stoc_plastic(self)
            else:
                print()
                print("Alege una din optiunile afisate!")
                print()
