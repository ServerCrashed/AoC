package main

import (
	// "bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

const (
	// Starting position of the dial
	INITIAL_POSITION = 50
	INPUT_PATH       = "/home/akshat/repos/AoC/2025/D1/input.txt"
)

var (
	// Keeps track of the number of times the dial comes to rest at 0
	counter = 0
)

type dial struct {
	position int
}

// Parses the intruction, and returns the direction and magnitude of the rotation
func parse(s string) (int, int) {
	direction := 0

	if s[0] == 'L' {
		direction = -1
	} else {
		direction = 1
	}

	num, err := strconv.Atoi(s[1:])
	if err != nil {
		log.Println(fmt.Errorf("Failed to convert string to integer: %v", err))
	}

	return direction, num
}

func (d *dial) rotate(s string) bool {
	direction, magnitude := parse(s)
	change := direction * magnitude
	d.position = (d.position + change) % 100
	if d.position == 0 {
		return true
	} else {
		return false
	}
}

func main() {
	d := dial{INITIAL_POSITION}

	//open file to read
	f, err := os.Open(INPUT_PATH)
	if err != nil {
		log.Fatalf("Error encountered while opening file: %v", err)
	}
	defer f.Close()

	//for each line, do a rotate, and increment counter if the condition is satisfied

	// Method 1
	// scanner := bufio.NewScanner(f)
	// for scanner.Scan() {
	// 	line := scanner.Text()
	// 	whetherZero := d.rotate(line)
	// 	if whetherZero {
	// 		counter += 1
	// 	}
	// }

	// Method 2
	data, err := os.ReadFile(INPUT_PATH)
	if err != nil {
		panic(err)
	}

	lines := strings.Split(string(data), "\n")
	for _, line := range lines {
		if line == "" {
			continue
		}
		whetherZero := d.rotate(line)
		if whetherZero {
			counter += 1
		}
	}

	// close file, and print the count
	fmt.Printf("Password: %v\n", counter)
}
