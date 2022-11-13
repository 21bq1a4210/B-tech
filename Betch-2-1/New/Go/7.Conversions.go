package main

import "fmt"

func main() {
	var price int = 100
	fmt.Println("Price is", price, "$.")

	var taxRate float64 = 0.08
	//var tax float64 = price * taxRate
	/*
		.\7.Conversions.go:10:20:
		invalid operation:
		price * taxRate (mismatched types int and float64)
	*/
	var tax float64 = float64(price) * taxRate
	fmt.Println("Tax is", tax, "$.")

	//var total float64 = price + tax
	/*
		.\7.Conversions.go:14:22:
		invalid operation:
		price + tax (mismatched types int and float64)
	*/
	var total float64 = float64(price) + tax
	fmt.Println("Total cost is", total, "$.")

	var avaiableFunds int = 120
	fmt.Println(avaiableFunds, "$ available.")
	fmt.Println("within budget?", total <= float64(avaiableFunds))
}

//result
/*
Price is 100 $.
Tax is 8 $.
Total cost is 108 $.
120 $ available.
within budget? true

*/
