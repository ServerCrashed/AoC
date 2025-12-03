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

func findBankJoltage(bank string) (bankJoltage int, err error) {
	n := len(bank)
	// index1 is the index where battery num1 exists
	num1, num2, index1 := 0, 0, 0

	// For num1; iterating until the second last battery
	for i := 0; i < n-1; i++ {
		battery := string(bank[i])
		if joltage, err := strconv.Atoi(battery); err != nil {
			return 0, fmt.Errorf("Error converting string to int: %v\n", err)
		} else if joltage > num1 {
			num1 = joltage
			index1 = i
		}
	}

	// For num2; interating from index1 + 1 until the end of the bank
	for i := index1 + 1; i < n; i++ {
		battery := string(bank[i])
		if joltage, err := strconv.Atoi(battery); err != nil {
			return 0, fmt.Errorf("Error converting string to int: %v\n", err)
		} else if joltage > num2 {
			num2 = joltage
		}
	}

	bankJoltage = num1*10 + num2
	return bankJoltage, nil
}

func main() {
	totalJoltage := 0

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
		if bankJoltage, err := findBankJoltage(line); err != nil {
			log.Fatalf("Error finding joltage: %v\n", err)
		} else {
			totalJoltage += bankJoltage
		}
	}

	fmt.Printf("Total joltage: %v\n", totalJoltage)

}
