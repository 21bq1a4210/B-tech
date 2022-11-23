package main

import (
	"fmt"
)

var a string // \n
var b int    // 0
var c bool   //false
var s string
var i1, i2, i3 = 1, 2, 3

const (
	A int = 1
	B     = 3.14
	C     = "Hi!"
)

func main() {
	var name = "Sarath"
	var roll = 4210
	var bo = true
	var f = 8.81

	fmt.Println("Name:", name)    //, <-> + same type
	fmt.Println("ROll.no:", roll) //, </-> + cuz diff type
	fmt.Println("SGPA:", f)
	fmt.Println("Bool:", bo)
	fmt.Println("Sum:", i1+i2+i3)

	fmt.Println("Constants:", A, B, C)

	s = "End"
	fmt.Println(b)
	fmt.Println(a)
	fmt.Println(c)
	fmt.Println(s)
}
