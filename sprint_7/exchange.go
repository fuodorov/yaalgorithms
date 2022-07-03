package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const maxCapacity = 32 * 10000
	buffer := make([]byte, maxCapacity)
	scanner.Buffer(buffer, maxCapacity)

	var line string

	// читаем количество дней
	var n int

	scanner.Scan()
	line = scanner.Text()

	n, _ = strconv.Atoi(line)

	// читаем цены акций (массив)
	prices := make([]int, n)

	scanner.Scan()
	row := scanner.Text()
	values := strings.Split(row, " ")

	var value int
	for i := 0; i < n; i++ {
		value, _ = strconv.Atoi(values[i])
		prices[i] = value
	}

	// находим решение. Стратегия - пока цена следующего дня больше, чем предыдущего,
	// мы будем продавать. Фактически, мы складываем все монотонно увеличивающиеся
	// сегменты на графике акций
	profit := 0
	for i := 1; i < n; i++ {
		if prices[i-1] < prices[i] {
			profit += prices[i] - prices[i-1]
		}
	}
	fmt.Print(profit)
}