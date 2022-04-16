package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const maxCapacity = 8 * 100000
	buffer := make([]byte, maxCapacity)
	scanner.Buffer(buffer, maxCapacity)

	var line string

	// читаем входную строку
	scanner.Scan()
	line = scanner.Text()

	// делим строку на слова
	words := strings.Split(line, " ")

	// выводим слова в обратном порядке
	for i := len(words) - 1; i > 0; i-- {
		fmt.Printf("%s ", words[i])
	}
	fmt.Print(words[0])
}