package main

import "fmt"

func main() {
	var ch = 'A'
	fmt.Println(ch + 10)
	ch += 10
	fmt.Println(string(ch))
}
