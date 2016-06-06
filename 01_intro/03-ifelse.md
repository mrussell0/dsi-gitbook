## If / Else Statements

We can use if/else statements to decide what to do based on a **condition**. Conditions are _evaluated_ as true (or whatever you specify) using an expression. The `if` statement is followed by an _expression_ and then a block of code. The `else` statement immediately follows with a block of code. You may also specify multiple conditions with the `else if` statement; it will also require an expression to evaluate.

#### Basic Example

```java
public class Product {
    // attributes of my product
    private String title = "Backpack";
    private String desc = "Waterproof, badass pack";
    private double price = 79.99;
    // methods (functions) of my product
    public static void main(String[] arguments) {
        String msg = "Welcome to the product app";
        System.out.println(msg);
        //System.out.println(this.toString());
        if (arguments.length > 0) {
            System.out.println("We have arguments");
        }
        logSillyMessage();
        sayYourName();
    }
    // java methods must define the type they return
    // OR they can be VOIDDDDDDDDD
    // and return NOTHING
    public String toString() {
        String data = "Product: " + this.title;
        return data;
    }
    public static void logSillyMessage() {
        System.out.println("spoorthi is a cookie monster");
    }

    public static void sayYourName() {
        System.out.println("James");
    }
}
```


#### With an `else`

```java
if (doWeHaveArguments == true) {
  // if true, let the user know
  // awesome but they are not needed
  System.out.println("Thanks but we don't need arguments");
} else {
  // otherwise let them know thanks
  // for not spamming
  System.out.println("Thanks for not spamming! :)");
}
```

#### Multiple Conditions

```java
// password must be 8+ characters long
// better if 12+ characters long
if (name.length >= 12) {
  // let the user know their pw length is GOOD!
} else if (name.length >= 8) {
  // if not longer than 12 check if 8 or longer
  // catches 8,9,10,11
  // let the user know they met the min length requirement
} else {
  // password length not long enough; tell user
}
```
