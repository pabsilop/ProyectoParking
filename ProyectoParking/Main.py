print('!- BIENVENIDO -!')
print('ELIJA QUE USUARIO QUIERE USAR: ')
print('[1] - CLIENTE NORMAL')
print('[2] - ADMINISTRADOR')

opt = input()

if(opt == '1'):
    print('HA ELEGIDO CLIENTE NORMAL\n')
    print('¿QUÉ QUIERE HACER?')

    print('[1] - DEPOSITAR VEHÍCULO')
    print('[2] - RETIRAR VEHÍCULO')
    print('[3] - DEPOSITAR ABONADOS')
    print('[4] - RETIRAR ABONADOS')

    opt2 = input()
    if(opt2 == '1'):
        print('[1] - DEPOSITAR VEHÍCULO')

    if(opt2 == '2'):
        print('[2] - RETIRAR VEHÍCULO')

    if(opt2 == '3'):
        print('[3] - DEPOSITAR ABONADOS')

    if(opt2 == '4'):
        print('[4] - RETIRAR ABONADOS')

elif(opt == '2'):
    print('INTRODUZCA LA CONTRASEÑA DE ADMINISTRADOR:\n ')
    password = input()

    if(password == '123'):
        print('HA ELEGIDO ADMINISTRADOR\n')
        print('¿QUÉ QUIERE HACER?')

        print('[1] - ESTADO DEL PARKING')
        print('[2] - FACTURACIÓN')
        print('[3] - CONSULTA DE ABONADOS')
        print('[4] - ABONOS')
        print('[5] - CADUCIDAD DE ABONOS')
    else:
        print('\nCONTRASEÑA INCORRECTA')

print('\nNÚMERO NO VÁLIDO')
