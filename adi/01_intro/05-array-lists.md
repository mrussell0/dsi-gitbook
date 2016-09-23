## ArrayList Examples

```java
// ArrayList<int>
ArrayList<Integer> guesses = new ArrayList<Integer>();
guesses.add(42);
guesses.add(13);
guesses.add(98);

int amountOfGuesses = guesses.size();

for (int counter = 0; counter < amountOfGuesses; counter++) {
    // guess[0] or guess[counter]
    System.out.println("Guess #" + counter + " is : " + guesses.get(counter));
}

ArrayList<String> students = new ArrayList<String>();
students.add("Mudkip");
students.add("Pikachu");
students.add("Gyrados");

int amountOfStudents = students.size();

for (int inc = 0; inc < amountOfStudents; inc++) {
    System.out.println(students.get(inc));
}
```

#### Challenge

1. Create an ArrayList of friends.
2. Add all of your friends.
3. Log the size of your friends.
3. Then, the robot uprising happens! You survive! Your friends do not. Find out how to remove all of them at once from the ArrayList. Do it.
4. Now, you've found some rocks, frogs, roaches, etc as friends.
5. Create a new ArrayList of NewFriends
6. Loop through all of your new friends
7. And then watch the nuclear holocaust together.
8. (This means use the method from step 4)
9. Log the size of your list.
10. BONUS: You survived. Wow. Create an ArrayList of reasonsToLive. Add a few.
11. Change (or _set_) the first reason to something new.
12. Change the last reason to something new.
13. Log out the first and last reason to live.
