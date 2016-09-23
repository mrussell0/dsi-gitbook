---
title: Recursion
type: Homework
duration: "1:00"
creator:
    name: Drew Mahrt
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Recursion

> ***Note:*** _This can be a pair programming activity or done independently._

## Exercise

This homework will help you review recursion, an important concept in many algorithms. Recursion has two key elements:

1. The recursive call (calling a method from within itself)
2. The base case (the check for a condition to stop the recursive calls)

Without a base case, a recursive method would infinitely call itself since there is nothing to stop it.

Here is a simple example of a recursive method:

```java
public void countDown(int n){
  //BASE CASE
  if(n < 0){
    System.out.println("Blastoff!")
    return;
  }

  System.out.println("Count: "+n);
  //RECURSIVE CALL
  countDown(n-1);
}
```

Watch [this video](https://www.youtube.com/watch?v=t4MSwiqfLaY) to gain some more insight on recursion. Make sure you pay special attention to the explanation on how factorial works, but you can ignore the section on binary trees. Once you are done watching the video, open the starter-code and complete the methods in Recursion.java.

If you are having trouble getting started with a specific problem, remember to try starting with the base case, then work your way up.

#### Requirements

- Write code for all 3 of the recursion problems

**Bonus:**

- Write code for the bonus recursion problem

#### Starter code (if needed)

Recursion.java contains empty methods that you need to complete with recursion.

#### Deliverable

A completed Recursion.java file which solves all of the recursion problems.

![Example Image](https://cloud.githubusercontent.com/assets/25366/8370438/dd651c2c-1b7c-11e5-8638-c99e2f6c7c61.png)
