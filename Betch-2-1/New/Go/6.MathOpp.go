package main

import "fmt"

func main() {
	fmt.Println(1 + 2)
	fmt.Println(1 + 2.2) //no error
	//fmt.Println(2 + int(2.2))
	/*.\6.mathopp.go:8:22:
	cannot convert 2.2 (untyped float constant) to type int*/
}
