# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Classes

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Describe what classes and objects are
- Describe what object properties and methods are
- Demonstrate and explain instantiation
- Write getter and setter methods for a given class

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
* Recall basic knowledge of TextViews
* Recall basic knowledge of Java data types

---

## Opening: What are classes? (5 minutes)

Objected-oriented programming is a paradigm used in some programming languages that is based on a concept of *classes* and *objects*. We will be discussing what these terms mean and how they are related to each other.

> Check: Ask them to recall basic Java data types. Ask them to explain TextViews.

## Introduction: What are classes? (25 minutes)

Objects are special pieces of data that have properties and functions contained inside of them. We use these objects to divide our code into separate responsibilities. We can then use these objects from other code to execute their responsibility. How the object accomplishes its responsibility is irrelevant to the calling code. This is known as a black box. 

We only have to worry about the input and outputs of the object and let the object itself worry about it self. For example, if we had a ```Calculator``` object and it had a function ```public int findLowestCommonDenominator(int number1, int number2)``` we don't care how it finds our lowest common denominator, just that it returns an int that is correct.

This has an advantage for whomever is implementing the object as well. They can change the internals, perhaps make it more efficient, without breaking compatibility with any code that uses it already.

These objects are first templated using the concept of `classes`. A `class` is a special *type* that can be user-defined to ensure every object of its type contain all the properties and methods of that class. Unlike data types which have intrinsic value - i.e an `int` is a number, `char` are characters - classes have defined values. For example, a __Car__ class could hold the `double` value of __speed__ and also `String` value of __model__.

> Check: In your own words, explain what is an object? What is a class?

#### Instantiation

Creating an object of a class is called instantiation. This means we are creating a new object in memory. This is done by using the `new` keyword and a special type of method called a constructor. Constructor methods can include some parameters we can pass to our new object. They set up the initial state of the object.

Constructors methods fire when an object is instantiated and their only purpose is to help create an instance of a class. In contrast, the purpose of methods is much more general: execute Java code.


## Demo: What are classes? (10 minutes)

>Note: Explain the syntax here about how to create new objects and also the syntax of a class file.

The paradigm of OOP allows programmers to compartmentalize specific bits and pieces of code so that we can reuse this code while also hiding parts of it within the each class. In the __Car__ example, we can create new Cars and give them different model names but have an internal concept of _speed_ that only the Car itself is aware.

Variables and objects defined within an object are known as _member variables_. Java convention dictates that these variables be named in camel case starting with an 'm' denoting that it is a _member variable_

Functions defined within a class are known as _methods_. Java convention dictates that methods also be named in camel case.

``` java
public class Car {
    double mSpeed = 0.0;
    String mModel;
    public Car(String named) {
        mModel = named;
    }
}

// creating a new object of type Car
Car mFirstCar = new Car("DeLorean");
```

> Check: What are methods? How should they be defined and written?

## Guided Practice: What are classes? (10 minutes)

Ok, time for you to write your own class!

> Instructor Note: Use a text editor to do this next part and as you write the class, try to elicit each line of syntax from members of the class.

In your Documents folder, create a new text file with a text editor of your choice.

In this file, create a new class using the syntax your learned above. Your class should be modeling a __Person__ object. Your __Person__ must have a name and age. The __Person__ can also have another __Person__ as its "child". All of these must be set during construction. Don't try to instantiate your __Person__ anywhere.

> Note: sample correct code
``` java
public class Person {
    int mAge;
    String mName;
    Person mChild;
    public Person(String named, int aged, Person parentOf) {
        mName = named;
        mAge = aged;
        mChild = parentOf;
    }
}
```

Save this file as `Person.java` and note that the file must be named the same as the top level class in your file. Save it in your Documents folder.

Now open Terminal on Mac or Command Prompt on Windows then use the command `cd Documents` to get to your Documents folder. Then use `javac Person.java` to compile the file and you should see a _Person.class_ in your Documents folder if your class compiled correctly. If not, then there should be an error in your terminal window, see what its telling you and fix!

> Check: Did anyone hit an error?

In basic Java programs, you need a `static main()` method to be able to run the program, add one to your program with in your __Person__ `class` like this.

```java
public static void main(String [] args) {
}
```

Inside of this method, instantiate a Person object with a child:


```java
    public static void main(String [] args)
	{
		Person person = new Person("Ankur", 27, new Person ("Mint", 2, null));
	}
```

>Instructor Note: Students might have trouble with this because of the `null` needed. Good to pause, explain the next section and let them try again.

### Getters and setters (5 minutes)
In Java, there is a convention used called _getters and setters_. It is not a good idea to make _member variables_ public and so instead methods are defined to expose access.

By definition, getters "get" or return stored information from an instance of a class; setters assign information / data to an instance of a class.

##### Demo: Getters and setters (5 minutes)

In our car, we simply want to allow read access to the mSpeed variable and so we would define a method called `getSpeed()` within our `class`.

```java
public double getSpeed() {
    return mSpeed;
}
```
Java naming convention dictates that getters should start with 'get' and then the name of the variable (minus any leading letters). The only exception is for getters with return type `boolean`, it is convention to name these as `isBoolean()` or `hasBoolean()`. For example our car might have a method: `hasLowFuel()`.

Perhaps we also wanted to add a _member variable_ `mOwner` and wanted to allow public access to change this variable, we would define a setter. The naming convention here is similar to the getter methods but with starting with 'set'

```java
private String mOwner;
public void setOwner(String name) {
    mOwner = name;
}
```

> Check: In your own words, describe the difference between getters and setters.

##### Guided Practice: Getters and Setters (5 minutes)

Take five minutes to finish getting `mAge` from your object.

> Check: Ask students to review their solution with a partner. What issues are people having?

### toString()
Every object in Java has a method called `toString` that returns a String representing
the state of the object. This method is called when the object is printed.

```
Point p1 = new Point(3, 0);
Point p2 = new Point(3, 4);

System.out.println(p1);
System.out.println(p2);
```

If we don't write our own `toString()` method then Java uses a default implementation
of the method and prints out it's own custom String. Here we see a string that tells us
we have a `Point` object at a certain memory location in the Java virutal machine.

```
Point@6d06d69c
Point@7852e922
```

We can overwrite this default behavior to print out much more useful information.

Writing our own `toString()` method makes the program print out way more helpful
information. Here we construct and return our own custom String that includes
the point's `this.x` and `this.y` values:

```
public String toString() {
  return "(" + this.x + "," + this.y + ")";
}  
```

With this new method the program now prints out points as we're used to seeing them.

```
Point p1 = new Point(3, 0);
Point p2 = new Point(3, 4);

System.out.println(p1);
System.out.println(p2);
```

```
(3,0)
(3,4)
```

### Equality

Remember the `.equals()` method we have to use when comparing Strings? Turns out
`.equals()` is another method all objects have! 

```
Point a1 = new Point(7, 7);
Point a2 = new Point(7, 7);
Point bb = new Point(8, 8);

System.out.println("a1 == a1? " + (a1 == a1)); // true
System.out.println("a1 == a2? " + (a1 == a2)); // false
System.out.println("a1 == bb? " + (a1 == bb)); // false

System.out.println("a1.equals(a1)? " + a1.equals(a1)); // true
System.out.println("a1.equals(a2)? " + a1.equals(a2)); // false
System.out.println("a1.equals(bb)? " + a1.equals(bb)); // false  
```

We must define our `.equals()` method that manually compares the `x` and `y`
values of two points to one another. Notice that we accept another Point object
as a parameter here.

```
public boolean equals(Point p2) {
  // consider points equal if and only if their x and y values are the same.
  return this.x == p2.x && this.y == p2.y;
}
```

Consider the differences in results after adding the new `.equals()` method.
Pay special attention to how `a3` refers to `a1` by being set equal to it without
creating it's own new Point object.

```
Point a1 = new Point(7, 7);
Point a2 = new Point(7, 7);
Point a3 = a1; // we say a3 "references" the same Point as a1

System.out.println("a1 == a1? " + (a1 == a1)); // true
System.out.println("a1 == a2? " + (a1 == a2)); // false
System.out.println("a1 == a3? " + (a1 == a3)); // true

System.out.println("a1.equals(a1)? " + a1.equals(a1)); // true
System.out.println("a1.equals(a2)? " + a1.equals(a2)); // true
System.out.println("a1.equals(a3)? " + a1.equals(a3)); // true
```

After adding the new `.equals()` method notice that the code behaves differently.
Our new equals method compares the x and y values of each of these points and reports
they are all the same.

The points a1 and a2 are still not "strictly equal" to each other using the `==`
operator, but now our custom `.equals()` method returns true. Objects will only
ever be strictly equal to each other with the `==` operator if they have a reference
to literally the same object.

Notice that a1 is strictly equal to a3 becuase they both **refer** to the exact same
Point object.

### Practice Writing Classes (20 mins)

Work by yourself to implement the following classes:

#### Rectangle Class
Write a `Rectangle` class with the following methods:
- a constructor that accepts two integers representing `width` a `length`
- an `area` method that returns an int
- a `perimeter` method that returns an int the total perimeter
- an `equals` method that considers rectangles equal if their width and length
  are the same (or if their width/length and length/width are the same!)
- a method `isSquare` that returns true if the width and length are the same.
- a `toString` method that prints out an ASCII representation of the rectangle.

```
Rectangle r = new Rectangle(4, 1);
System.out.println(r);

+----+
|    |
+----+
```

### Anonymous Classes (5 mins)

Java has a feature that allows interfaces to be implemented "on the fly". This is called anonymous classes.

An example of this in Android is the `interface OnClickListener` which is used to respond to clicks on views.

`OnClickListener` only has a single method `void OnClick(View v)` that needs to be implemented. Instead of creating a new class every time we see to assign an `OnClickListener` we can create an _anonymous class_

> Check: In your own words, explain the purpose of an anonymous class.

#### Demo: Anonymous Classes (5 minutes)

```java
button.setOnClickListener(new View.OnClickListener(){
  @Override
  public void onClick(View v) {

  }
});
```

Notice how we implemented this - it doesn't have a definite `class`, other then the generic `Object`. This is why its called an anonymous class. The class has no name to call it by.

#### Guided Practice: Anonymous Classes (10 minutes)

Your turn: Implement `setOnItemClickListener` for a ListView that creates a Toast that says the position clicked on the list.

> Instructor Note: Provide students with a project that has a ListView added to a layout.

### Conclusion (5 minutes)

Throughout much of our work so far in this course, we have seen classes being used, and object being instantiated without understanding the reason behind all of it. Hopefully today's lesson helped clarify the mystery behind the code being automatically generated by Android Studio. In our next lesson, we will be discussing the `extends` keyword you have seen at the top of every Activity, a concept known as subclassing.

### ADDITIONAL RESOURCES
- [Classes & Objects](http://www.javawithus.com/tutorial/class-as-a-reference-data-type)
- [Java Getters vs Setters](http://stackoverflow.com/questions/2036970/how-do-getters-and-setters-work)
