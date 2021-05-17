# Mini-Proiect Fabrica
from auth import Auth

while True:
    meniu = ["Login","Shut down!"]
    for submeniu in range(len(meniu)):
        print(f'{submeniu + 1}.{meniu[submeniu]}')
    optiune = int(input('> ')) - 1
    if meniu[optiune] == 'Shut down!':
        print('Shutting Down...')
        break
    elif optiune == 0:
        client = Auth()
        user = client.login()

