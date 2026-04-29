# fibonacci + Factorial + Es_primo
import sys
import time
import threading

sys.set_int_max_str_digits(0)

# Primo
def es_primo(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# factorial
def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return fact

# Fibonacci
def fibonacci(num):
    a = 1
    b = 1
    c = 0
    while c < num:
        c = a + b
        a = b
        b = c
    if num == c:
        return True
    else:
        return False

def trabajo(inicio, fin):
    x = inicio
    for x in range (fin):
        if es_primo(x):
                print(x, fibonacci(x), factorial(x))

hilo1 = threading.Thread(target=trabajo, args=(1,5000))
hilo2 = threading.Thread(target=trabajo, args=(5000,10000))

t_inicio = time.time()
hilo1.start()
hilo2.start()

hilo1.join()
hilo2.join()
t_fin = time.time()

print("Tiempo de proceso", t_fin-t_inicio)