---
title: Array Basics
duration: "1:30"
creator:
    name: Kristen Tonga
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Storing Data in Arrays

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Create and manipulate arrays and Arrays
- Work with for loops to iterate over arrays


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Work with basic data types and assign variables
- Create basic functions

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Gather materials needed for class
- Complete prep work required
- Prepare any specific instructions

---
<a name="opening"></a>

## Opening (5 mins)

So far, we have stored all of the information for our apps in individual variables. That works for a small amount of information, but what if we had to manage larger sets of data? For instance, what if we had credit card transactions in a customer's banking app. Would we want to store every transaction in its own variable, or have a single variable that would hold all of the transactions at once?

>  In pairs, come up with a few more examples of where storing our data in a collection would be beneficial (data situations or example apps) (1-2 minutes)

<a name="introduction"></a>
## Introduction: Basic Arrays (5 mins)

An array is a container object that holds a **fixed** number of values of **a single type**. You've already seen an example in the `main` method.

> Instructor Note: Optional - Draw a picture similar to the one below on the board to visually display each element and corresponding index.

Each item in an array is called an *element*, and each element can be accessed by it's *index*. The index of elements starts at 0. That means visually that:

  INDEX  | 0 | 1 | 2 | 3 | 4
  -------|---|---|---|---|---
| ELEMENT| x | x | x | x | x |
  -------|---|---|---|---|---

> Check: If a fixed size is required, how would we add more space?

## Demo: Creating Arrays (5 mins)

Let's create an Array together:

> Instructor Note:  Explain each piece of syntax here

```java
  class ArrayDemo {
    public static void main(String[] args) {
      //declares an array of integers
      int[] anArray; // note datatype, followed by [] indicating array

      //allocates memory for 10 integers
      anArray = new int[10];

      //assign elements
      anArray[0] = 111;
      anArray[1] = 222; //etc.

      //access elements
      System.out.println("Element at index 0: "+ anArray[0]);
      System.out.println("Element at index 1: "+ anArray[1]); //etc.
      System.out.println("The array has a size of "+anArray.length);
    }
  }
```

> Check: How would I find the index of the last element in the array using the length property?

## Independent Practice: Creating Arrays (10 mins)

**Now you:** Create a String array of *three* of your favorite things. Print the result to the command line.

>Instructor Note: Go over how you would create `String[] favoriteThings;`

> Check: What are the three parts of creating an array? (expect: declare variable, allocate memory, initialize/assign values)

## Demo: Manipulating Arrays (15 mins)

Now that we know what the computer will be doing, let's use the shortened syntax. Arrays can also be created and initialized with one statement. The length of the array is automatically determined by the number of elements between the curly braces.

```java
  class FavoriteThings {
    public static void main(String[] args) {
      // shortened syntax. assign variable, allocate memory, and initialize values all in one
      String[] favoriteThings = {
        "raindrops",
        "roses",
        "whiskers on kittens"
      } // length will be inferred as: 3
    }
  }
```

#### Manipulating Basic Arrays

Let's take a look at some basic things you can do with an array.

Note that indexing (getting/setting the item based on its position in the array) and determining the length of the array have built-in syntax, while some less fundamental operations are performed by using methods on the `Arrays` object. This is similar to the way you can add two numbers together by just writing `a + b` but need to use methods on the `Math` object to do more esoteric things like rounding.

```java
  class ArrayManipulationDemo {
    // initialize array
        int[] primeNumbers = {5,3,11,7,2}; //next 13, 17, 19, 23

      // get the thing at a specified index
        int firstPrime = primeNumbers[0];
        System.out.println( "index 0: " + firstPrime );

      // print it
        System.out.println( Arrays.toString(primeNumbers) );

      // sort it
        Arrays.sort( primeNumbers );
        System.out.println( Arrays.toString(primeNumbers) );

      // get its length
        System.out.println(primeNumbers.length); // it's a constant, not a method -- we'll talk about this later

      // see if value is found in array. Returns -1 if not found.
      // Note: binarySearch() only works if the array is sorted.
        int indexOf11 = Arrays.binarySearch( primeNumbers, 11 );
        System.out.println( "index of 11: " + indexOf11 );

      // CHECK: How to get the value?
        // if(indexOf11 >= 0) {
            System.out.println("looking for 11, found value: " + primeNumbers[indexOf11]);
        // }
  }
```

#### Error Checking
Now what if we searched for an value that was not in the array? Let's see if 10 is a prime number.

> Instructor Note: Add the lines below, leaving out the commented code. Throw the exception, ask the students why it was thrown, and ONLY THEN add in the >=0 check that is commented out below and above.

```java
  int[] primeNumbers = {5,3,11,7,2};

  int indexOf10 = Arrays.binarySearch( primeNumbers, 10 );
  System.out.println( "index of 10: " + indexOf11 );
  // if(indexOf11 >= 0) {
      System.out.println("looking for 10, found value: " + primeNumbers[indexOf11]);
  // }
```

An Exception is thrown when the computer is asked to do something it can't do, like accessing index -1 or 4 in a 4-element array. Exceptions bubble up, and unless caught (which we will talk about in a later lesson) cause the program to quit.

It is important to consider when the results of our actions might throw an exception, and add checks as needed.

> Check:  If an array is 5 elements long, what happens if we look for `myArray[5]`?

## Demo: Problems with Arrays (10 min)

But what if I decide that actually, I want this list to include 4 things instead of 3? For example, let's go back to our favoriteList; I decide I really like chocolate and want it to be the fourth favorite thing.

Follow along, if you want:

```java
  public static void addFourthFav() {
    String[] favoriteThings = {"roses","whiskers on kittens","raindrops"};
    favoriteThings[3] = "chocolate"; // **Check:** why 3 not 4?
    System.out.println( Arrays.toString(favoriteThings) );
  }
```

That throws an out of bounds exception!

Why? As mentioned, arrays are fixed in size. To add chocolate as a fourth item in an array, I would have to create a new array of a larger size, copy the info over, and then initialize the additional elements.

```java
  public static void addFourthFav() {
    String[] favoriteThings = {"roses","whiskers on kittens","raindrops"};
    String[] favoriteThingsLarge = new String[4];

    System.arraycopy(favoriteThings, 0, favoriteThingsLarge, 0, 3);
    favoriteThingsLarge[3] = "chocolate";

    System.out.println( Arrays.toString(favoriteThingsLarge) );
  }
```

Luckily, Java has provided something better: collections.