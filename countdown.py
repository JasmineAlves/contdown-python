'''
CONTDOWN - Contador regressivo simples em Python

- divmod() : Função para obtenção dos minutos e segundos
- end="\r" : Permite a impressão contínua do temporizador na mesma linha do terminal
- time.sleep(1) : Atrasa cada iteração do loop em 1 segundo.
'''

import time

t = input("Insira o tempo (em segundos): ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada inválida!")
    quit()

# 0 == false, 1 == true; enquanto t != 0 ele será true
while t:
    # Primeiro retorna os minutos da divisão, após retorna o resto (segundos)
    minutes, seconds = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)

    # Subscreve na mesma linha do terminal a cada segundo que passou
    print(timer, end="\r")
    time.sleep(1)
    t -= 1

print("TEMPO ENCERRADO!")
