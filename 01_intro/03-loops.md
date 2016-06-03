## `for` Loops and `[]` Arrays

`for` loops allow us to cycle through (known as _iteration_, or 'we are going to iterate through this array') a list of items. These can be `[]`, `List`, `ArrayList<>`, and more.

> **..soon..**: Some of those _collection_ types are new. We'll introduce them soon. Feel free to check them out if you have free time!

#### Arrays

An `[]` is a _list_ of things. Arrays are required to _specify their length_ when they are created (_instantiated_). We can create arrays in various ways:

```java
String[] myTools =  new String[20];  // I specify myTools is a new String[] with 20 empty items
// now, I'll specify the strings when I create an array of Strings for pizza toppings
// because I place the items inside of the { block }, the array knows it has a length of 3
String[] pizzaToppings = {"Cheese", "Pepperoni", "Black Olives"};
```

#### Listing all App arguments

```java
public static void main(String[] arguments) {
  // counter: starting lap
  // condition: if counter <= arguments.length then... do { block }
  // finally, after the { block } of code, countrer++
  // repeat until condition is met
  for (int counter = 0; counter < arguments.length; counter++) {
     System.out.println(counter + arguments[counter]);
  }
}
```
Now, we need to compile and run it with arguments.

```bash
javac SomeClass.java
java SomeClass here are my arguments
# output below
0 here
1 are
2 my
3 arguments
```

#### Looping through custom String[]

```java
// this is an array of Strings
// aka String[]
// a list of strings
// a collection of strings
String[] friends = {
 "Spoorthi",
 "Jim",
 "Bill",
 "Kevin",
 "Angie"
};

// loop through every item in my []
// list them in terminal
// declare a counter (incrementor)
// condition to evaluate to true
// if true, do { block }
// counter++; repeat
for (int counter = 0; counter < friends.length; counter++) {
   System.out.println("Guess who's about to get slimed?!");
   System.out.println(friends[counter]);
   System.out.println(friends[counter] + " JUST GOT SLIMED!!!!");
} // end for
```
