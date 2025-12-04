package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

const (
	INPUT_PATH = "/home/akshat/repos/AoC/2025/D3/input.txt"
)

var (
	totalJoltage int64 = 0
)

func calculateBankJoltage(batteryJoltages *[]int) int64 {
	var bankJoltage = int64(0)
	for _, num := range *batteryJoltages {
		bankJoltage = bankJoltage*10 + int64(num)
	}

	return bankJoltage
}

func getBankJoltage(bank string) (bankJoltage int64, err error) {
	n := len(bank)
	index := -1
	var batteryJoltages []int
	for i := 11; i >= 0; i-- {
		max := 0
		for s := index + 1; s <= n-1-i; s++ {
			battery := string(bank[s])
			if joltage, err := strconv.Atoi(battery); err != nil {
				return 0, fmt.Errorf("Error converting string to int: %v\n", err)
			} else if joltage > max {
				max = joltage
				index = s
			}
		}
		batteryJoltages = append(batteryJoltages, max)
	}

	bankJoltage = calculateBankJoltage(&batteryJoltages)
	return bankJoltage, nil
}

func main() {
	// Open input file
	f, err := os.Open(INPUT_PATH)
	if err != nil {
		log.Fatalf("Error encountered while opening file: %v\n", err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}
		if bankJoltage, err := getBankJoltage(line); err != nil {
			log.Fatalf("Error finding joltage: %v\n", err)
		} else {
			totalJoltage += bankJoltage
		}
	}

	fmt.Printf("Total joltage: %v\n", totalJoltage)

}
