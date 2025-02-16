package main

import "fmt"

// Function to demonstrate if-else
func demonstrateIf() {
	x := 10

	if x > 5 {
		fmt.Println("x is greater than 5")
	} else if x == 5 {
		fmt.Println("x is equal to 5")
	} else {
		fmt.Println("x is less than 5")
	}
}

// Function to demonstrate switch
func demonstrateSwitch() {
	day := "Monday"

	switch day {
	case "Monday":
		fmt.Println("Start of the week")
	case "Friday":
		fmt.Println("Weekend is near")
	default:
		fmt.Println("Midweek")
	}

	// Switch without a condition
	x := 10
	switch {
	case x > 10:
		fmt.Println("x is greater than 10")
	case x == 10:
		fmt.Println("x is equal to 10")
	default:
		fmt.Println("x is less than 10")
	}
}

// Function to demonstrate for loops
func demonstrateForLoops() {
	// Traditional for loop
	fmt.Println("Traditional for loop:")
	for i := 0; i < 5; i++ {
		fmt.Println("i:", i)
	}

	// While-like loop
	fmt.Println("While-like loop:")
	j := 0
	for j < 5 {
		fmt.Println("j:", j)
		j++
	}

	// Infinite loop with break
	fmt.Println("Infinite loop with break:")
	k := 0
	for {
		fmt.Println("k:", k)
		k++
		if k == 3 {
			break // Exit the loop
		}
	}

	// Range-based loop
	fmt.Println("Range-based loop:")
	nums := []int{1, 2, 3, 4, 5}
	for index, value := range nums {
		fmt.Printf("Index: %d, Value: %d\n", index, value)
	}
}

// Main function to call all demonstration functions
func main() {
	fmt.Println("Demonstrating if-else:")
	demonstrateIf()

	fmt.Println("\nDemonstrating switch:")
	demonstrateSwitch()

	fmt.Println("\nDemonstrating for loops:")
	demonstrateForLoops()
}
