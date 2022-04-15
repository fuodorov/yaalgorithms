package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Pile struct {
	c, m int
}

func newPile(c, m int) Pile {
	return Pile{c, m}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var line string

	// читаем грузоподъёмность рюкзака
	var M int

	scanner.Scan()
	line = scanner.Text()

	M, _ = strconv.Atoi(line)

	// читаем количество куч с золотым песком
	var n int

	scanner.Scan()
	line = scanner.Text()

	n, _ = strconv.Atoi(line)

	// читаем информацию о кучах с золотым песком
	piles := make([]Pile, n)

	for i := 0; i < n; i++ {
		scanner.Scan()
		row := scanner.Text()
		cm := strings.Split(row, " ")
		c, _ := strconv.Atoi(cm[0])
		m, _ := strconv.Atoi(cm[1])
		piles[i] = newPile(c, m)
	}

	// сортируем кучи по убыванию стоимости килограмма золота
	sort.Slice(piles, func(i, j int) bool {
		pile1 := piles[i]
		pile2 := piles[j]

		c1 := pile1.c
		c2 := pile2.c

		return c1 > c2
	})

	maxSum := 0
	mass := M
	index := 0

	for {
		if mass <= 0 || index >= n {
			break
		}
		pile := piles[index]
		if mass >= pile.m {
			maxSum += pile.m * pile.c
			mass -= pile.m
		} else {
			maxSum += mass * pile.c
			mass = 0
		}
		index++
	}

	fmt.Print(maxSum)
}