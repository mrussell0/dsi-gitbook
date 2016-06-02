## Conditional Logic

#### Data Types

Java has a lot of built-in data types. Let's review some of the more common ones that new developers will encounter.

```java
// data types!
// flash card time!
// one side: use case
// back side: variable type

// type || the name = assignment || a value
char capitolS = 'S'; // a single character
String myMessage = "Hello, you may buy all the booze.";
int funTimes = -42; // positive or negative whole value
boolean canBuyBooze = true; // true or false
float pi = 3.14; // floating point value
double radiusOfPie = 33.090909; // value with precise decimal points
String[] listOfThings; // array of Strings, arrays []
// array == collection == list == etc
```

> **Hint:** If you forget any of these data types, refer to the flash cards you created in class yesterday. Practice memorizing them! Memorization of these types will help you early on in your career,

#### Expressions and Logic

In programming, we are able to use expressions to decide if a _statement_ is true or false. Let's look at how this might work:

```java
if (true) {
  System.out.println("YES");
} else {
  System.out.println("no");
}
```

Let's break this logical statement down and identify each part:

```java
if (expression) {
  // something occurs inside of this block of code
  // a block of code is inside of { and  }
  // this particular block is scoped (owned) by the expression
  // if it meets the specified condition
} else {
  // another block of code! this is owned by the expression
  // if it does not evaluate!
}
```

#### In-Class Example

We built an age-check application to see if someone can buy alcohol.

```java
public class App {
    // starting point!
    public static void main(String[] args) {
        System.out.println("Can I haz booze?");

        String userInput = args[0];
        System.out.println("Our user input: " + userInput);

        int usersAge = Integer.parseInt(userInput);

        if (usersAge >= 21) {
            System.out.println("You may haz all teh booze");
        } else {
            System.out.println("You gotta GTFO, kid");
        }
    }
}
```
