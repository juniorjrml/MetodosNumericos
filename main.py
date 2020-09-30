import Modulo1 as m1
exercicios = [2]
if 1 in exercicios:
    # Exercicio solicita para os valores de x = 0.1 e 0.7
    x = 0.7
    taylor = m1.poli_taylor_expandida(x)
    horner = m1.poli_horner(x)
    exp = m1.f_modulo1(x)
    print("Formula de taylor expandida: ", taylor)
    print("formula de horner: ", horner)
    print("Exp: ", exp)
    print("erro entre as formulas", abs(horner-taylor))
    erro_expandida = m1.erro_absoluto(m1.poli_taylor_expandida, m1.f_modulo1, x)
    erro_horner = m1.erro_absoluto(m1.poli_horner, m1.f_modulo1, x)
    print("Erro da forma expandida: ", abs(erro_expandida))
    print("Erro da forma de horner: ", abs(erro_horner))

if 2 in exercicios:
    pass
