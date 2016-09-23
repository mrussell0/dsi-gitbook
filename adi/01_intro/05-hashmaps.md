## HashMaps

```java
//store unique information
//age, hobbies, wpm, howManyLegos
HashMap<String, Integer> counts = new HashMap<String, Integer>();
counts.put("age", 32);
counts.put("hobbies", 4);
counts.put("wpm", 75);
counts.put("legoCount", 921929922);

System.out.println(counts.get("wpm") + " is not very fast");

// moocher, braggart, quiet, party, best man/maid of honour
HashMap<String, String> friends = new HashMap<String, String>();
friends.put("moocher", "Jeremy");
friends.put("braggart", "myself");
friends.put("quiet", "bill");
friends.put("party", "jim");
friends.put("maid of honor", "george");
friends.put("braggart", "asshole");

System.out.println("We are going to party with " + friends.get("braggart") + " and also " + friends.get("party"));
```
