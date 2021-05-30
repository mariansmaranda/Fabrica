# Mini-Proiect Fabrica
from auth import Auth

while True:
    meniu = ["1.Login","2.Shut down!"]
    for submeniu in meniu:
        print(submeniu)
    optiune = input('> ')
    if optiune == '2':
        print('Shutting Down...')
        break
    elif optiune == "1":
        client = Auth()
        user = client.login()
    else:
        print()
        print("Alege una din optiunile afisate!")
        print()

