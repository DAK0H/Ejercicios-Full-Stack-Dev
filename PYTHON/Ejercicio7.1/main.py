'''
Crear un módulo que contenga las operaciones básicas de una calculadora: sumar, restar, multiplicar y dividir.
Este módulo lo importaréis a un archivo python y llamaréis a las funciones creadas. Los resultados tenéis que mostrarlos por consola.
'''

import calculator as op
print(dir(op))

def results():
    result_sum = op.sum(2, 3)
    print(f'Suma: {result_sum}')

    result_subs = op.subs(7, 3)
    print(f'Resta: {result_subs}')

    result_mult = op.mult(2, 3)
    print(f'Multiplicación: {result_mult}')

    result_div = op.div(15, 3)
    print(f'División: {result_div}')

results()






