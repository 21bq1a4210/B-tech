package main

import "fmt"

var shape string
var length, width, depth float64
var cost float64

func main() {
	shape = "cube"
	length, width, depth = 10.0, 11.1, 22.2
	var area = length * width * depth
	cost = 1.05
	fmt.Println("Shape:", shape)
	fmt.Println("Dim (m):", length, depth, width)
	fmt.Println("Area (m)^2:", area)
	fmt.Printf("Cost per m:%v/-\n", cost)
	fmt.Printf("Total cost:%v/-", cost*area)
}
