package main

import (
	"fmt"
	"time"
	"sync"
)

func es_primo(num int) bool {
	for i := 2; i < (num/2)+1; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func numeros_primos(inicio,fin int, wg *sync.WaitGroup) {
	defer wg.Done()
	for i := inicio; i < fin; i++ {
		if es_primo(i){
			fmt.Println(" El numero", i, "es primo")
		}
	}
}

func main() {
    var wg sync.WaitGroup
    inicio := time.Now()

    wg.Add(1)
    go numeros_primos(1, 100000, &wg)

    wg.Wait()
    fin := time.Now()
    fmt.Printf("Tiempo: %v\n", fin.Sub(inicio))
}