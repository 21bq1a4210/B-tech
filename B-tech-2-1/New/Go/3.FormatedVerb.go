package main

import (
	"fmt"
)

/*
VERB	DESCRIPTION
%v		Prints the value in the default format
%#v		Prints the value in Go-syntax format
%T		Prints the type of the value
%%		Prints the % sign
*/
var str = "Sarath"
var i = 10
var f = 3.14
var b = true

func main() {
	fmt.Printf("Value\tGo-syn\tType\n")
	fmt.Printf("%v\t%#v\t%T\n", i, i, i)
	fmt.Printf("%v\t%#v\t%T\n", f, f, f)
	fmt.Printf("%v\t%#v\t%T\n", b, b, b)
	fmt.Printf("%v\t%#v\t%T\n", str, str, str)
}
