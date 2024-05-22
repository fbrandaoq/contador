# importa as bibliotecas
import os
import time # biblioteca de tempo

# usuário informa um número
contador = int(input('Informe um número inteiro: '))
os.system('cls')

# conta a partir do número informado até 0
while contador >= 0:
    print(f'Contagem regressiva: {contador}...')
    time.sleep(1)
    os.system('cls')
    contador -= 1

print('BOOM!!!!')

