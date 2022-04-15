package main

import (
	"bufio"
	"fmt"
	"os"
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

	// находим самый длинный палиндром (лексикографически минимальный),
	// который можно получить из строки путём удаления и перестановки символов

	// т.к. допустимы перестановки, то порядок символов не влияет на решение

	// посчитаем частоту каждого символа во входной строке
	counter := make(map[rune]int)
	for _, symbol := range line {
		count, contains := counter[symbol]
		if !contains {
			counter[symbol] = 1
		} else {
			counter[symbol] = count + 1
		}
	}

	// все символы, имеющие чётную частоту (2n), будут частью ответа, т.к.
	// мы можем поместить n символов в начало палиндрома, а остальные n
	// символов - в конец. Для символов, имеющих нечётную частоту, мы заполним
	// середину палиндрома одним из таких символов, а оставшиеся 2*n символов
	// разделим пополам и добавим в начало и в конец
	var begin, mid, end []rune

	for i := 97; i <= 122; i++ {
		r := rune(i)
		count, contains := counter[r]
		if !contains || count == 0 {
			continue
		}
		// нечётная частота символа
		if count%2 == 1 && len(mid) == 0 {
			mid = []rune{r}
			counter[r] = count - 1
			i--
		} else {
			// чётная частота символа
			for i := 0; i < count/2; i++ {
				begin = append(begin, r)
			}
		}
	}

	// end - это реверс от begin
	for i := len(begin) - 1; i >= 0; i-- {
		end = append(end, begin[i])
	}

	palindrome := string(begin) + string(mid) + string(end)

	fmt.Print(palindrome)
}