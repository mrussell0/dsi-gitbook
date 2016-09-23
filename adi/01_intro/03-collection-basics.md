---
title: Storing Data in Collections
duration: "1:30"
creator:
    name: Kristen Tonga
    city: NYC
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Storing Data in Collections

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Create and manipulate arrays and ArrayLists
- Work with for loops to iterate over collections


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Work with basic data types and assign variables
- Create basic functions
- Create a basic app, and change TextView, based on a button click

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

## Demo: Collections (15 mins)

Collections will not only will provide us with more convenience methods, allowing us to do more things with the data we have, but will also *automatically increase in size* if we need!

There are many different collection classes that we use just like data types, each of which provides some distinct functionality, but for today, we're going to focus on just one of them.

#### ArrayList

Let's take the array we made of favorite things and convert it into an `ArrayList`.

```java
  public static void main(String[] args) {
    // initialize ArrayList
      ArrayList<String> favoriteThings = new ArrayList<>();
    // add items
      favoriteThings.add("bright copper kettles");
      favoriteThings.add("brown paper packages tied up with strings");
  }
```

Note, the data type of each element is defined in angle brackets `<>`. This data type could be any object type. So, if you'd created a `Person` object, as you may have in the pre-work, you could create an ArrayList of Persons! (i.e. an `ArrayList<Person>`)

If you want to make an ArrayList of a primitive type, you need to use a "boxed" version of that type as the thing in the angle brackets. For example, if you want to store a bunch of `int`s, you would use an `ArrayList<Integer>`.

#### Manipulating a ArrayList

An ArrayList is an object, with methods, which makes it much easier to manipulate than a simple array. Check out the following methods.

```java
  //to print. No need to explicitly convert it to a string first!
  //(because ArrayList has a toString() method, which automatically
  //gets called here)
    System.out.println("favoriteThings = " + favoriteThings);

  //add(item) -- adds to the end of the list
    favoriteThings.add("chocolate");
    System.out.println("favoriteThings = " + favoriteThings);

  //add(index, item) -- adds to the list at specified index and moves all other entries over. Think: what you would have to do with a simple array to do that?
    favoriteThings.add(1, "warm woolen mittens");
    System.out.println("favoriteThings = " + favoriteThings);

  //set(index, item) -- replace the item at the given index with a new one
    favoriteThings.set(0, "tarnished copper kettles");
    System.out.println("favoriteThings = " + favoriteThings);

  //to search for an entry
    int indexOfIceCream = favoriteThings.indexOf("icecream");
    if(indexOfIceCream != -1) {
      String ic = favoriteThings.get(indexOfIceCream);
      System.out.println("ic = " + ic);
    }
    else {
      System.out.println("icecream not found");
    }

 //here's another good one: get number of things in the ArrayList
    favoriteThings.size();
```

> Instructor Note: Add other convenience methods as needed.

> Check: What are advantages of using an ArrayList over an array? Expect students to include: automatic resizing, convenience methods.


## Guided Practice: Iterating Through a List with For Loops (15 mins)
One more thing before we start talking about lists in Android: How do you iterate through a list?

#### The For Loop
Do you remember the syntax used in a for loop? We used it in the Control Flow lesson to print something to the command line a set number of times.

The for loop is also commonly used with arrays and collections to iterate through each of the elements and do something with each entry.

For example, let's create a list of 5 movies and iterate through it, printing each one to the command line.

> Instructor Note: Get movie suggestions from the class. It is also possible to use Android Studio, and display all movie names in a view instead.

```java
  public static void main(String[] args) {
    ArrayList<String> movieList = new ArrayList<>();
    movieList.add(/*student suggestion here*/); //x5
    printMovies(movieList);
  }

  public static void printMovies(ArrayList<String> movies) {
    for (int i = 0; i < movies.size(); i++) {
      System.out.println("where i="+i+" : "+movies.get(i));
    }
  }

```

To review, a for loop has an initialization stage (where i is initialized), a termination condition (which includes the logic for when the loop stops), and an increment stage (that will occur on the completion of each loop).

#### The Enhanced For Loop
There is also another for loop syntax that is especially for arrays and lists. This is sometimes referred to as the **enhanced** for loop. Try it with me:

```java
 for (String movie : movieList) {
  System.out.println("I love "+movie+"!");
 }
```

The enhanced for loop is the form that is recommended by Oracle for arrays and collections.

A normal for loop is still useful sometimes -- it makes it easier to work with the index of each item alongside its value, or to modify the collection while you're iterating over it. But if you just need to do something with each element, the enhanced for loop is cleaner and more efficient.

>Check: Why might you want to iterate through an array?

## Independent Practice (15 mins)

Complete as many of the following challenges as you can in the next 15 minutes. Each challenge should be completed in its own method.

1. Find the size:
  a. Create an array of ints.
  b. Print the length of the array to the command line.

2. Concrete Jungle
  a. Create a ArrayList of New York City wildlife.
  b. Create a function that, given an ArrayList of Strings, prints for each element: "Today, I spotted a /*Thing here*/ in the concrete jungle!"

3. Create a method that, given an array of ints, return the sum of the first 2 elements in the array. If the array length is 1, just return the single element, and return 0 if the array is empty (has length 0).

4. Create an method that, given an ArrayList of words (Strings), turns each word into Pig Latin. The rules of Pig Latin are as follows:
  a. The first consonant is moved it to the end of the word and suffixed with an `ay`.
  b. If a word begins with a vowel you just add `way` to the end.

For example, `pig` becomes `igpay`, `banana` becomes `ananabay`, `twig` becomes `wigtay`, and `aadvark` becomes `aadvarkway`.

> Instructor Note: The example for Pig Latin can be posted online if students do not get to it, as it will probably take too long to do in class.

<a name="conclusion"></a>
## Conclusion (5 mins)

Quick review:
- List some differences between arrays and Array lists

Arrays and ArrayLists are fundamental tools needed by anything that wants to store and manipulate collections of data. Now that you know how to use them, we can start creating apps that use those collections. Excited?



### ADDITIONAL RESOURCES
- [Oracle Java Docs - Arrays](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)
- [Android Docs - ArrayList](http://developer.android.com/reference/java/util/ArrayList.html)
- [Oracle Java Docs - The for Statement](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html)
- [CodingBat - Array-1 examples](http://codingbat.com/java/Array-1)
- [Android Docs - Building Layouts with an Adapter](http://developer.android.com/guide/topics/ui/declaring-layout.html#AdapterViews)
- [Android Docs - Adapter](http://developer.android.com/reference/android/widget/Adapter.html)



<!--
## Add On Lesson
To tackle these Collections Classes, we first need to learn a bit of vocabulary.

Interface | Classes               | Reasons to use it
----------|-----------------------|---------------------------------
List      | ArrayList, LinkedList, Vector, Stack | collection of Objects(most similar to simple array)\ndata is accessed by index
Sets      | HashSet, TreeSet      | unique collection of Objects(like a list, but no duplicates)\ndata is accessed by value
Maps      | HashMap, TreeMap      | set of key/value pairs(similar to a dictionary)\nkeys must be unique\ndata is accessed by using the key


**Student Exercise:** (5 min) Take five minutes to write down a thing that might be either a List, a Map, or a Set. Throw something around the room to get examples from each student -->
