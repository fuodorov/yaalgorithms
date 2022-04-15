package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const maxCapacity = 8 * 100000
	buffer := make([]byte, maxCapacity)
	scanner.Buffer(buffer, maxCapacity)

	var line string

	// читаем число строк
	var n int

	scanner.Scan()
	line = scanner.Text()
	n, _ = strconv.Atoi(line)

	// читаем строки
	// сперва наибольший общий префикс - первая строка
	scanner.Scan()
	prefix := scanner.Text()

	for i := 1; i < n; i++ {
		scanner.Scan()
		line = scanner.Text()
		minLen := min(len(prefix), len(line))
		var j int
		for j = 0; j < minLen; j++ {
			if prefix[j] != line[j] {
				break
			}
		}
		prefix = line[0:j]
	}

	fmt.Print(len(prefix))
}

func min(x, y int) int {
	if x < y {
		return x
	} else {
		return y
	}
}