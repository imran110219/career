package main

import "fmt"

func main() {
	// Variable declaration
	var name string = "Go"
	var version float64 = 1.21
	isAwesome := true // Shorthand declaration

	// Zero values
	var count int
	var message string

	// Printing variables
	fmt.Println("Language:", name)
	fmt.Println("Version:", version)
	fmt.Println("Is Awesome?", isAwesome)
	fmt.Println("Count (zero value):", count)
	fmt.Println("Message (zero value):", message)

	// Type inference
	x := 42          // int
	y := 3.14        // float64
	z := "Hello, Go" // string

	fmt.Printf("x: %v, y: %v, z: %v\n", x, y, z)
}
