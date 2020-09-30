import math

def f_modulo1(x):
    return math.exp(x)

def fat(x):
    if x > 1:
        return x * fat(x-1)
    else:
        return 1

def poli_taylor_expandida(x):
    acumulador = 1
    for n in range(1, 6):
        acumulador += pow(x, n)/fat(n)
    return acumulador

def poli_horner(x):
    acumulador = 1
    for n in range(5, 0, -1):
        acumulador *= (1 + (1/n)*x)
    return acumulador

def erro_absoluto(p,f,x):
    return abs(p(x)-f(x))


def erro_r(f, x):
    return abs(f(x))

def erro_x(x, x_old):
    return abs(x - x_old)

def novo_x(intervalo):
    return (intervalo[0] + intervalo[1])/2

def novo_intervalo(f, intervalo, x):
    if f(intervalo[0]) * f(x) < 0:
        return [intervalo[0], x]
    else:
        return [x, intervalo[1]]


def metodo_bisseccao(f,intervalo,b):
    if f(intervalo[0] * intervalo[1] > 0):
        print("Pare! Inicie com outro intervalo de busca!")
        return None

    x = novo_x(intervalo)
    if f(x) == 0:
        return [0, x, 0, 0]

    n = 1
    x_old = x
    intervalo = novo_intervalo(f, intervalo, x)

    while(e_r <= b and e_x <= b):
        if f(x) == 0:
            return [n, x, 0, 0]
        n += 1
        x_old = x
        intervalo = novo_intervalo(f, intervalo, x)
        x = novo_x(intervalo)
        e_r = erro_r(f, x)
        e_x = erro_x(x, x_old)

    return [n, x, e_r, e_x]