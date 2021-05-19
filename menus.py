import json
from angajator import Angajator
from stocuri import Stocuri
from productie import Productie

class Menu:
    def meniu_manager(self):
        while True:
            meniu = ["Angajeaza Manager", 'Angajeaza Operator', 'Angajeaza Gestionar', 'Afiseaza Angajatii',
                     "Log Out"]

            for submeniu in range(len(meniu)):
                print(f'{submeniu + 1}.{meniu[submeniu]}')
            optiune = int(input('> ')) - 1
            if meniu[optiune] == 'Log Out':
                print('Logging Out...')
                break
            elif optiune == 0:
                Angajator.angajator_manager(self)
                pass
            elif optiune == 1:
                Angajator.angajator_operator(self)
                pass
            elif optiune == 2:
                Angajator.angajator_gestionar(self)
                pass
            elif optiune == 3:
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
    def meniu_operator(self):
        while True:
            meniu = ['Asambleaza Frigider', 'Asambleaza Microunde', 'Asambleaza aragaz',
                     'Log Out']
            for submeniu in range(len(meniu)):
                print(f'{submeniu + 1}.{meniu[submeniu]}')
            optiune = int(input('> ')) - 1
            if meniu[optiune] == 'Log Out':
                print('Logging Out...')
                break
            elif optiune == 0:
                Productie.productie_frigidere(self)
            elif optiune == 1:
                Productie.productie_cuptor_microunde(self)
            elif optiune == 2:
                Productie.productie_aragaz(self)
    def meniu_gestionar(self):
        while True:
            meniu = ['Verifica Stock', 'Adauga Tevi','Adauga Placi Metal','Adauga Placi Electronice',
                     'Adauga Foi Metal' ,'Adauga Plastic' , 'Log Out']
            for submeniu in range(len(meniu)):
                print(f'{submeniu + 1}.{meniu[submeniu]}')
            optiune = int(input('> ')) - 1
            if meniu[optiune] == 'Log Out':
                print('Logging Out...')
                break
            elif optiune == 0:
                with open("stocuri.json", "r") as s:
                    stoc = json.load(s)
                    print(stoc)
            elif optiune == 1:
                Stocuri.adauga_stoc_tevi(self)
            elif optiune == 2:
                Stocuri.adauga_stoc_placi_metal(self)
            elif optiune == 3:
                Stocuri.adauga_stoc_placi_electronice(self)
            elif optiune == 4:
                Stocuri.adauga_stoc_foi_metal(self)
            elif optiune == 5:
                Stocuri.adauga_stoc_plastic(self)
