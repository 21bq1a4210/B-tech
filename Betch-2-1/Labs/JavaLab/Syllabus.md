Course Objectives:
1. To write programs using abstract classes.
2. To write programs for solving real world problems using java collection frame 
work.
3. To write multithreaded programs.
4. To design GUI application using swing controls.
5. To introduce java compiler and eclipse platform
6. To impart hands on experience with java programming.
Note: 
Mandatory to follow test driven development with Eclipse IDE empowered JUnit testing framework 
and code coverage plugin.
The list suggests the minimum program set. Hence, the concerned staff is requested to add more 
problems to the list as needed.

List of Experiments

1. Create a class called Invoice that a hardware store might use to represent an invoice for an 
item sold at the store. An Invoice should include four pieces of information as instance 
variables-a part number (type String),a part description(type String),a quantity of the item 
being purchased (type int) and a price per item (double). Your class should have a constructor 
that initializes the four instance variables. Provide a set and a get method for each instance 
variable. In addition, provide a method named getInvoiceAmount() that calculates the invoice 
amount (i.e., multiplies the quantity by the price per item), then returns the amount as a double 
value. If the quantity is not positive, it should be set to 0. If the price per item is not positive, 
it should be set to 0.0. Write a test application named InvoiceTest that demonstrates class 
Invoice’s capabilities. [CO1]

2. Develop a Java application to generate Electricity bill. Create a class with the following 
members: Consumer no., consumer name, previous month reading, current month reading, 
and type of EB connection (i.e. domestic or commercial). Compute the bill amount using the 
following tariff. [CO1]
If the type of the EB connection is domestic, calculate the amount to be paid as follows:
1. First 100 units - Rs. 1 per unit
2. 101-200units - Rs. 2.50 per unit
3. 201 -500 units - Rs. 4 per unit
4. >501 units - Rs. 6 per unit
If the type of the EB connection is commercial, calculate the amount to be paid as follows:
5. First 100 units - Rs. 2 per unit
6. 101-200units - Rs. 4.50 per unit
7. 201 -500 units - Rs. 6 per unit
8. >501 units - Rs. 7 per unit

3. Create class Savings Account. Use a static variable annual Interest Rate to store the annual 
interest rate for all account holders. Each object of the class contains a private instance 
variable savings Balance indicating the amount the saver currently has on deposit. Provide 
method calculate Monthly Interest to calculate the monthly interest by multiplying the savings
Balance by annual Interest Rate divided by 12 this interest should be added to savings 
Balance. Provide a static method modify Interest Rate that sets the annual Interest Rate to a 
new value. Write a program to test class Savings Account. Instantiate two savings Account 
objects, saver1 and saver2, with balances of $2000.00 and $3000.00, respectively. Set annual
Concentration Rate to 4%, then calculate the monthly interest and print the new balances for 
both savers. Then set the annual Interest Rate to 5%, calculate the next month’s interest and 
print the new balances for both savers. [CO1]

4. Create a class called Book to represent a book. A Book should include four pieces of 
information as instance variables-a book name, an ISBN number, an author name and a 
publisher. Your class should have a constructor that initializes the four instance variables. 
Provide a mutator method and accessor method (query method) for each instance variable. In 
addition, provide a method named get Book Info that returns the description of the book as a 
String (the description should include all the information about the book). You should use 
this keyword in member methods and constructor. Write a test application named Book Test 
to create an array of object for 30 elements for class Book to demonstrate the class Book's 
capabilities. [CO1].

5. Write a JAVA program to search for an element in a given list of elements using binary search 
mechanism. [CO1]

6. Write a Java program that implements Merge sort algorithm for sorting and also shows the 
number of interchanges occurred for the given set of integers. [CO1]

7. Write a java program to make rolling a pair of dice 10,000 times and counts the number of 
times doubles of are rolled for each different pair of doubles. Hint: Math.random() [CO1].

8. Develop a java application with Employee class with Emp_name, Emp_id, Address, Mail_id, 
Mobile_no as members. Inherit the classes, Programmer, Assistant Professor, Associate 
Professor and Professor from employee class. Add Basic Pay (BP) as the member of all the 
inherited classes with 97% of BP as DA, 10 % of BP as HRA, 12% of BP as PF, 0.1% of BP 
for staff club fund. Generate pay slips for the employees with their gross and net salary. [CO1]

9. Write a Java Program to create an abstract class named Shape that contains two integers and 
an empty method named print Area(). Provide three classes named Rectangle, Triangle and 
Circle such that each one of the classes extends the class Shape. Each one of the classes 
contains only the method print Area () that prints the area of the given shape.[CO2]

10. Develop a java application to implement currency converter (Dollar to INR, EURO to
INR,Yento INR and vice versa), distance converter (meter to KM, miles to KM and vice 
versa), time converter (hours to minutes, seconds and vice versa) using packages. [CO1]

11. Write a Java Program to Handle Arithmetic Exceptions and Input Mis Match Exceptions. 
[CO1]

12. Write a multi-threaded Java program to print all numbers below 100,000 that are both prime 
and Fibonacci number (some examples are 2, 3, 5, 13, etc.). Design a thread that generates 
prime numbers below 100,000 and writes them into a pipe. Design another thread that 
generates Fibonacci numbers and writes them to another pipe. The main thread should read 
both the pipes to identify numbers common to both. [CO3].

13. Write a java program that implements a multi-threaded application that has three threads. First 
thread generates a random integer every 1 second and if the value is even, second thread 
computes the square of the number and prints. If the value is odd, the third thread will print 
the value of cube of thenumber. [CO3].

14. Write a Java program that correctly implements the producer – consumer problem using the 
concept of inter-thread communication. [CO3].

15. Write a Java program that reads a file name from the user, displays information about whether 
the file exists, whether the file is readable, or writable, the type of file and the length of the 
file inbytes. [CO1].

16. Write a Java program to build a Calculator in Swings/ [CO4]

17. Write a Java program to implement JMenu to draw all basic shapes using Graphics. [CO4]

18.Write a Java program to implement JTable and JTree. [CO4]

19. Write a Java program to implement JTabbedPane. [CO4]

20. Write a Java Program that implements a simple client/server application. The client sends data 
to a server. The server receives the data, uses it to produce a result and then sends the result 
back to the client. The client displays the result on the console. For ex: The data sent from the 
client is the radius of a circle and the result produced by the server is the area of the circle. 
[CO3]

Course Outcomes: at the end of the lab, the student will be able to
CO1: Develop programs for solving real world problems using java collection frame work.
CO2: Develop and apply multithreaded programs in network applications.
CO3: Develop GUI programs using swing controls in Java.