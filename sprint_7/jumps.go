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

	var line string

	// читаем числа n и k
	var n, k int

	scanner.Scan()
	line = scanner.Text()

	nk := strings.Split(line, " ")
	n, _ = strconv.Atoi(nk[0])
	k, _ = strconv.Atoi(nk[1])

	// количество способов добраться до ступеньки с номером n
	dp := make([]int, n+1)

	// до первой ступеньки можно добраться только одним способом
	result := countWays(n, k, &dp)

	fmt.Print(result)
}

const module = 1000000007

func countWays(n, k int, cache *[]int) int {
	if n < 1 {
		return 0
	} else if n == 1 {
		return 1
	} else {
		if (*cache)[n] != 0 {
			return (*cache)[n] % module
		} else {
			for i := 1; i <= k; i++ {
				(*cache)[n] += countWays(n-i, k, cache) % module
			}
			return (*cache)[n] % module
		}
	}
}