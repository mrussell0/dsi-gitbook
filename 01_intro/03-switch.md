## Switch Statements

Switch statements are great for times when you need to check for a variety of conditions. Instead of writing out complex `if else` statements, you can see if a value or expression match specific _cases_. Multiple values (or cases) can run the same block of code. The following example shows us checking for the user to accept or decline with a `y`, `Y`, `YES`, `yes`, `oui`, `n`, or `N` value. Otherwise it lets them know they didn't enter a proper value.

```java
public static void main(String[] args) {
  String userInput = args[0]; // get the first argument for the user
  // we expect y, Y, YES, oui, n, n
  // userInput should equal y, n, Y, N
  // switch accepts a variable argument and has different options (cases)
  // match and then run code until a break statement is read
  switch(userInput) {
      case "Y": // single
      case "y": // or multiple cases
      case "yes": // can run the same block of code
      case "YES": // all of these (y, Y, yes, YES, oui)
      case "oui": // run the next line of code
          System.out.println("ok, thank you");
          break; // STOP
      case "N": // same for N and n
      case "n": // they run this...
          System.out.println("ok y not?");
          break; // STOP
      default:  // if no other conditions are met... default!
          System.out.println("We could not interpret your input??????");
          break;
}
```
