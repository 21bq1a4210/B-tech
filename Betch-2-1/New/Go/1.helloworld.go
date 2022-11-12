/*
In Go, every program is part of a package. We define this using the package keyword.
In this example, the program belongs to the main package.
*/
package main

/*import ("fmt") lets us import files included in the fmt package.*/
import (
	"fmt"
)

/* A blank line.
Go ignores white space. Having white spaces in code makes it more readable.*/
/*func main() {} is a function.
Any code inside its curly brackets {} will be executed.*/
func main() {
	/*fmt.Println() is a function made available from the fmt package.
	It is used to output/print text.
	In our example it will output "Hello World!".*/
	fmt.Println("Hello World!")
}
