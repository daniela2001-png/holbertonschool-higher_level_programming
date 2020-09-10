#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        numerador = 0
        denominador = 0
        for tupla in my_list:
            numerador += (tupla[0] * tupla[1])
            denominador += tupla[1]
        return(numerador / denominador)
    return 0
