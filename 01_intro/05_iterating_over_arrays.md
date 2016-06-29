# Iterating Over Arrays

*After this lesson, you will be able to:*
- Iterate over an array
- find minimum, maximum values in an array
- handle fencepost problems
- tally the most frequently occuring item in an array
- prevent IndexOutOfBounds exceptions

## What is iterating over an array?

Iterating over an array is what we call code that looks at every item in an array.
For loops are the most common way to iterate over an array. We can write for loops
in many different ways in order to find out different things about an array.

Sometimes we'll only need to look at each element in an array one at a time.
sometimes we'll need to look at two elements at a time and compare them to each other.

Some problems, like finding the minimum or maximum element in an array, require
us to store extra information in variables outside of an array as we iterate over
it.

When we're iterating over an array we need to be careful to never access an index
that doesn't exist. Arrays always start at index `0` and and at `a.length - 1`.
No negative number is ever a valid index of an array. Empty arrays have a length
of zero and we can't access any index of an empty array.

Any time we access an index of an array that doesn't exist Java will throw an
`IndexOutOfBounds` exception when the programs run.

We'll show you here a collection of the most common ways to iterate over an array.

## Looking at one element at a time

This is the simplest way of iterating over an array. We write a for loop
that starts at `0` and goes while the value of `i` is less than the length
of the array.

Notice that this for loop correctly won't print anything out for an empty array.

```java
for (int i = 0; i < a.length; i++) {
  System.out.println(a[i]);
}
```

## Fencepost Problems

Sometimes we need to do special things at the beginning or end of when we're
iterating over an array.

Imagine a fence. A fence looks like this: `|=|=|=|=|'. This fence has five
fence posts and four, uh, pieces of fence.

There's a discrepency there! If we were writing a for loop to build a fence should
it run five times to place each fence post, or should it run four times to place
each piece of fence?

Consider this psuedo code that tries to place four pieces of fence:

```java
for (int i = 0; i < 4; i++) {
  placeFence();
  placePost();
}
```

The output of this code would build a fence like this: `=|=|=|=|`. There are
correctly four pieces of fence, but we're missing a fence post at the beginning!

If we switch the order of calling the `placeFence` and `placePost` methods then
we end up missing a fence post at the end of the fence.

```java
for (int i = 0; i < 4; i++) {
  placePost();
  placeFence();
}
```

This code produces a fence like this: `|=|=|=|=` without the last fence post at
the end.

The proper way to deal with a "fence post" scenario is to place one post before
or after the for loop.


```java
placePost();
for (int i = 0; i < 4; i++) {
  placeFence();
  placePost();
}
```

This code properly produces a fence with posts on each end, and fence pieces
between each post, like this: `|=|=|=|=|`.

### A Classic Fence Post Problem

Write a function called `printArray` that accepts an array of integers and prints
out each of the integers with a comma between each item. If the array is empty,
the function should print nothing. If there is only one item
in the array the function should just print the one item without any commas, like
this `42`. An array with more items should be printed like this: `42,12,97,8'.

Try to code this on your own before looking at the solution.

```java
public static void printArray(int[] a) {
  // Deal with the fence post by printing the first item in the array
  // without a comma and only when we're it is a non-empty array!
  if (a.length > 0) {
    System.out.print(a[0]);
  }

  // Deal with each piece of the fence by printing a comma, then the
  // value of the array at each index. Start the for loop at `i = 1`
  // to account for the fact that the first item was already printed.
  for (int i = 1; i < a.length; i++) {
    System.out.print("," + a[i]);
  }

  // Include an empty println statement at the end to make the output
  // produce a newline character at the end.
  System.out.println();
}
```

You may find it more natural to deal with the fence post after the for loop.
You can do this too.

```java
public static void printArray(int[] a) {
  // Don't print anything when the array is empty. Simply return to exit
  // the function.
  if (a.length === 0) {
    return;
  }

  // Start i at zero and print each element in the array followed by a comma.
  // Set the for loop to end before `a.length - 1` to leave one element left
  // for the fence post at the end after the for loop.
  for (int i = 0; i < a.length - 1; i++) {
    System.out.print(a[i] + ",");
  }

  // Print the final element at the end of the list without a comma.
  System.out.println(a[a.length - 1]);
}
```

## One-Way Gates

Write a function called `max` that accepts an array of integers and returns the
largest value in the array.

This problem requires us to create varaibles to store extra information outside
the for loop. We'll use if statements inside the for loop to update these variables
when certain conditions are met.

```java
public static void max(int[] a) {
  int largest = 0;

  for (int i = 0; i < a.length; i++) {
    if (a[i] > largest) {
      largest = a[i];
    }
  }

  return largest;
}
```

Notice that we initialize `largest` outside of the for loop and return it at the
end of the function. We compare each value in the array to the value and rewrite
the value of `largest` if we ever see something in the array larger than it.

Think of this as a one-way valve that only ever goes up.

## Backwards For Loops

It's totally possible to run a for loop backwards. We need to do three things:

1. Instead of starting i at zero
simply start it at `int i = a.length - 1`. We have to subtract one from the length
of the array to access the index of the last element to account for zero-based
indexing.
2. Change the test condition to run the for loop while `i >= 0`
3. Change the step instruction to `i--`

```java
for (int i = a.length - 1; i >= 0; i--) {
  System.out.println(a[i]);
}
```

## Double For Loops / Nested For Loops

Sometimes it's useful to nest a for loop inside a for loop. This code tests to
see if an array contains unique elements by comparing each item in the array
to every other item. 

Use another variable name other than `i` for the second for loop. `i, j, k, n`
are common for loop variable names.

```java
for (int i = 0; i < a.length; i++) {
  for (int j = 0; j < a.length; j++) {
    if (j != i) {
      if (a[i] == a[j]) {
        return false;
      }
    }
  }
  
  return true;
}
```

## Mousetrap
A mousetrap (these are made up names) is something that snaps closed once
an never opens again. 

```java
public static boolean isUnique(int[] a)  {
  boolean isUnique = true;

  for (int i = 0; i < a.length; i++) {
    for (int j = 0; j < a.length; j++) {
      if (j != i) {
        if (a[i] == a[j]) {
          isUnique = false;
        }
      }
    }
  }

  return isUnique;
}
```

## Item Tally

Write a function called `election` that accepts an array of Strings
representing candidate
in an array. You may assume the array is sorted.

["bush", "bush", "bush", "hedge", "hedge", "hedge", "hedge", "tree", "tree"];

public static String election(String[] a) {
  if (a.length == 0) {
    return null;
  }

  String winner = a[0];
  int mostVotes = 1;

  String item = a[0];
  int tally = 1;

  for (int i = 0; i < a.length; i++) {
    // tally up votes for the current candidate
    if (a[i].equals(item)) {
      tally++;
    } else {
      if (tally > mostVotes) {
        mostVotes = tally;
        winner = item;
      }

      tally = 1;
      item = a[i];
    }

  }

  return winner;
}

## Building Up Strings

Write a function that accepts a string and returns a compressed version of the
string encoding the 

compress("aaaaabbbabbbaaabbbbbaaa") // returns "5a3b1a3b3a5b3a"

public static String compress(String text) {
  String result = "";
  for () {
    result += count + letter
  }
}
