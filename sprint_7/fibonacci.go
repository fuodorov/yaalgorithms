package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

const module = 1000000007

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var line string

	// читаем число n - порядковый номер числа Фибоначчи
	var n int

	scanner.Scan()
	line = scanner.Text()

	n, _ = strconv.Atoi(line)

	if n == 0 || n == 1 {
		fmt.Print(1)
		return
	}

	// dp[i] = Fi
	dp := make([]int, n+1)

	// базовый случай
	dp[0] = 1
	dp[1] = 1

	for i := 2; i <= n; i++ {
		dp[i] = (dp[i-2] + dp[i-1]) % module
	}

	fmt.Print(dp[n])
}