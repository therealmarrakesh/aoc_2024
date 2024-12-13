package main

import (
	"fmt"
	"strconv"
	"time"
)

func hasEvenDigits(i int) bool {
	switch {
	case i < 10:
		return false
	case i < 100:
		return true
	case i < 1000:
		return false
	case i < 10000:
		return true
	case i < 100000:
		return false
	case i < 1000000:
		return true
	default:
		count := 0
		for i > 0 {
			i /= 10
			count++
		}
		return count%2 == 0
	}
}

func splitNumber(number int) (int, int) {
	numStr := strconv.Itoa(number)
	half := len(numStr) / 2
	sNew1, sNew2 := numStr[:half], numStr[half:]
	new1, _ := strconv.Atoi(sNew1)
	new2, _ := strconv.Atoi(sNew2)
	return new1, new2
}

func processNumbers(freqMap map[int]int) map[int]int {
	newMap := make(map[int]int)

	for number, count := range freqMap {
		if number == 0 {
			newMap[1] += count
		} else if hasEvenDigits(number) {
			new1, new2 := splitNumber(number)
			newMap[new1] += count
			newMap[new2] += count
		} else {
			newMap[number*2024] += count
		}
	}

	return newMap
}

func iterateNumberMap(freqMap map[int]int, iterations int) map[int]int {
	for i := 1; i <= iterations; i++ {
		fmt.Printf("The current iteration is: %d\r", i)
		freqMap = processNumbers(freqMap)
	}
	return freqMap
}

func sumFreq(freqMap map[int]int) int {
	totalCount := 0
	for _, count := range freqMap {
		totalCount += count
	}
	return totalCount
}

func main() {
	iterations := 75
	// Insert input here
	freqMap := map[int]int{0: 1}
	//
	start := time.Now()
	finalMap := iterateNumberMap(freqMap, iterations)
	elapsed := time.Since(start)
	fmt.Printf("\nThe number of items is: %d after iterating %d times! Took %v milliseconds!", sumFreq(finalMap), iterations, elapsed.Milliseconds())
}
