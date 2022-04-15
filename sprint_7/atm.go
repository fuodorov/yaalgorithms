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

	// читаем сумму, которую нужно набрать
	var m int

	scanner.Scan()
	line = scanner.Text()

	m, _ = strconv.Atoi(line)

	// читаем количество монет в банкомате
	var n int

	scanner.Scan()
	line = scanner.Text()

	n, _ = strconv.Atoi(line)

	// читаем достоинства монет
	coins := make([]int, n+1)

	scanner.Scan()
	line = scanner.Text()
	values := strings.Split(line, " ")

	var value int
	for i := 0; i < n; i++ {
		value, _ = strconv.Atoi(values[i])
		coins[i+1] = value
	}

	/*
	 dp[i][j] - число способов набрать сумму j, используя первые i монет
	*/
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
	}

	// базовый случай
	for i := 1; i <= n; i++ {
		dp[i][0] = 1 // вернуть 0 монет можно только одним способом - ничего не возвращать
	}

	// Динамика: dp[s][n] = dp[s][n - max(s)] + dp[s-max[s]][n]
	// https://www.youtube.com/watch?v=GrG1u1xbqhs&ab_channel=EvgeniyMalov
	for i := 1; i <= n; i++ {
		for j := 1; j <= m; j++ {
			if j-coins[i] >= 0 {
				dp[i][j] = dp[i][j-coins[i]] + dp[i-1][j]
			} else {
				dp[i][j] = dp[i-1][j]
			}
		}
	}

	fmt.Print(dp[n][m])
}