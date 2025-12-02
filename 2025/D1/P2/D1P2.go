package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
)

const (
	INITIAL_POSITION = 50
	INPUT_PATH       = "/home/akshat/repos/AoC/2025/D1/input.txt"
)

var (
	counter = 0
)

type dial struct {
	position int
}

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

func (d *dial) rotate(s string) {
	direction, magnitude := parse(s)

	fullCircles := magnitude / 100
	counter += fullCircles

	remainder := magnitude % 100
	for range remainder {
		d.position = (d.position + direction + 100) % 100
		if d.position == 0 {
			counter++
		}
	}
}

func main() {
	d := dial{INITIAL_POSITION}

	f, err := os.Open(INPUT_PATH)
	if err != nil {
		log.Fatalf("Error encountered while opening file: %v", err)
	}
	defer f.Close()

	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}
		d.rotate(line)
	}
	if err := scanner.Err(); err != nil {
		log.Fatalf("Error reading input: %v", err)
	}

	fmt.Printf("Password: %v\n", counter)
}
