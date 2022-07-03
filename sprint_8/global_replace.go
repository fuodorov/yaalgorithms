package main

import (
	"bufio"
	"os"
)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	const maxCapacity = 8 * 1000000
	buffer := make([]byte, maxCapacity)
	scanner.Buffer(buffer, maxCapacity)

	// читаем текст
	scanner.Scan()
	text := scanner.Text()

	// читаем шаблон, вхождения которого будут заменены
	scanner.Scan()
	pattern := scanner.Text()

	// читаем строку, которая будет заменять вхождения шаблона
	scanner.Scan()
	t := scanner.Text()

	// найдём все вхождения шаблона в текст
	var result []int

	s := pattern + "#" + text

	pi := make([]int, len(pattern))
	pi[0] = 0

	pi_prev := 0

	for i := 1; i < len(s); i++ {
		k := pi_prev
		for {
			if k <= 0 || s[k] == s[i] { // пока (k > 0) и (s[k] ≠ s[i])
				break
			}
			k = pi[k-1]
		}
		if s[k] == s[i] {
			k += 1
		}
		// запоминаем только первые len(pattern) значений pi-функции
		if i < len(pattern) {
			pi[i] = k
		}
		// запоминаем последнее значение pi-функции
		pi_prev = k
		// если значение pi-функции равно длине шаблона, то вхождение найдено
		if k == len(pattern) {
			// i - позиция конца вхождения шаблона
			// дважды отнимает от него длину шаблона, чтобы получить позицию начала в строке:
			// - чтобы переместиться на начало найденного шаблона
			// - чтобы не учитывать добавленное в начало pattern#
			result = append(result, i-2*len(pattern))
		}
	}

	// теперь, когда позиции найдены, заменяем их строкой t
	writer := bufio.NewWriter(os.Stdout)

	start := 0
	for i := 0; i < len(result); i++ {
		pos := result[i]

		writer.WriteString(text[start:pos])
		writer.WriteString(t)

		start = pos + len(pattern)
	}

	if start < len(text) {
		writer.WriteString(text[start:len(text)])
	}

	writer.Flush()
}