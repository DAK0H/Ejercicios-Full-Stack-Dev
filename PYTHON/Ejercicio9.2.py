'''En este segundo ejercicio, tenéis que crear una aplicación que obtendrá los elementos 
impares de una lista pasada por parámetro con filter y realizará una suma de todos estos 
elementos obtenidos mediante reduce.'''

from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd_numbers = filter(lambda x: x%2, numbers)
sum_odd = reduce(lambda x,y: x+y, list(odd_numbers))
print(sum_odd)