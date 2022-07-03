package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Time struct {
	hour, min int
}

func newTime(hour, min int) Time {
	return Time{hour, min}
}

func cmp(t1, t2 Time) int {
	if t1.hour < t2.hour {
		return -1
	} else if t1.hour > t2.hour {
		return 1
	} else {
		if t1.min < t2.min {
			return -1
		} else if t1.min > t2.min {
			return 1
		} else {
			return 0
		}
	}
}

func (time *Time) toString() string {
	hour := time.hour
	min := time.min
	if min != 0 {
		h := strconv.Itoa(hour)
		m := strconv.Itoa(min)
		return h + "." + m
	} else {
		h := strconv.Itoa(hour)
		return h
	}
}

type Class struct {
	start, finish Time
}

func convertToTime(time string) Time {
	if strings.Contains(time, ".") {
		hourMin := strings.Split(time, ".")
		hour, _ := strconv.Atoi(hourMin[0])
		min, _ := strconv.Atoi(hourMin[1])
		return newTime(hour, min)
	} else {
		hour, _ := strconv.Atoi(time)
		return newTime(hour, 0)
	}
}

func newClass(start, finish string) Class {
	return Class{convertToTime(start), convertToTime(finish)}
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)

	var line string

	// читаем количество занятий
	var n int

	scanner.Scan()
	line = scanner.Text()

	n, _ = strconv.Atoi(line)

	// читаем время начала и конца занятий
	classes := make([]Class, n)

	for i := 0; i < n; i++ {
		scanner.Scan()
		row := scanner.Text()
		startFinish := strings.Split(row, " ")
		classes[i] = newClass(startFinish[0], startFinish[1])
	}

	// сортируем занятия по возрастанию времени конца, а если оно совпадает,
	// то по возрастанию времени начала
	sort.Slice(classes, func(i, j int) bool {
		class1 := classes[i]
		class2 := classes[j]

		finish1 := class1.finish
		finish2 := class2.finish

		cmpFinish := cmp(finish1, finish2)

		if cmpFinish < 0 {
			return true
		} else if cmpFinish > 0 {
			return false
		} else {
			start1 := class1.start
			start2 := class2.start
			if cmp(start1, start2) < 0 {
				return true
			} else {
				return false
			}
		}
	})

	// выбираем очередное занятие с самым ранним временем конца, которое
	// не пересекается с уже выбранным занятием
	var lastEnd Time
	var solution []Class

	solution = append(solution, classes[0])
	lastEnd = classes[0].finish

	for i := 1; i < n; i++ {
		class := classes[i]
		if cmp(class.start, lastEnd) >= 0 {
			solution = append(solution, class)
			lastEnd = class.finish
		}
	}

	// печатаем оптимальное расписание
	fmt.Println(len(solution))
	printArray(solution)
}

func printArray(array []Class) {
	if len(array) == 0 {
		return
	}
	for i := 0; i < len(array)-1; i++ {
		class := array[i]
		start := class.start
		finish := class.finish
		fmt.Printf("%s %s\n", start.toString(), finish.toString())
	}
	class := array[len(array)-1]
	start := class.start
	finish := class.finish
	fmt.Printf("%s %s\n", start.toString(), finish.toString())
}