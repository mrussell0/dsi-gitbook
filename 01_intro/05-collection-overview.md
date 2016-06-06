## Collection Overview

Below is a table that represents various data structures in Java and reasons to use them. These can be used in your project by importing `java.util.*`. If you do not add the `util` library, you will be given an `error: cannot find symbol` when compiling.

```java
import java.util.*; // add to top of file
```

Interface | Classes               | Reasons to use it
----------|-----------------------|---------------------------------
List      | ArrayList, LinkedList, Vector, Stack | collection of Objects(most similar to simple array). Data is accessed by index
Sets      | HashSet, TreeSet      | unique collection of Objects(like a list, but no duplicates). Data is accessed by value
Maps      | HashMap, TreeMap      | set of key/value pairs(similar to a dictionary). Keys must be unique; data is accessed by using the key


#### ArrayList

Like an `[]` but without a set length.

##### Example

```java
ArrayList<String> favoriteThings = new ArrayList<String>();
favoriteThings.add("jaws");
favoriteThings.add("popcorn");
for (int i = 0; i < favoriteThings.size(); i++) {
  System.out.println("where i=" +i+ " : " + favoriteThings.get(i));
}
```

#### HashMap

Can be thought of as a dictionary of values. They are stored as a *key* with an associated *value*.
`key : value`
`age : 32`
`likesPizza: true`

##### Example


```java
HashMap<String, Integer> ages = new HashMap<String, Integer>();
ages.put("James", 32);
ages.put("Spoorthi", 22);
ages.put("Lichard", 29);
System.out.println("James is " + ages.get("James") + " years old");
System.out.println("There are " + ages.size() + " items stored as key:value in this HashMap");
```
