import threading
import time

def es_primo(num):
    for i in range(2, (num // 2) + 1):
        if num % i == 0:
            return False
    return True

def numeros_primos(inicio, fin):
    for i in range(inicio, fin):
        if es_primo(i):
            print("El numero", i, "es primo")

def main():
    inicio_tiempo = time.time()

    hilo1 = threading.Thread(target=numeros_primos, args=(1, 33333))
    hilo2 = threading.Thread(target=numeros_primos, args=(33333, 66666))
    hilo3 = threading.Thread(target=numeros_primos, args=(66666, 100000))

    hilo1.start()
    hilo2.start()
    hilo3.start()

    hilo1.join()
    hilo2.join()
    hilo3.join()

    fin_tiempo = time.time()
    print("Tiempo:", fin_tiempo - inicio_tiempo)

if __name__ == "__main__":
    main()