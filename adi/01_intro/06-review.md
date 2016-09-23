## Review

We've spent the day reviewing everything we have learned over the week.

#### Chat History with ArrayList

```java
String[] users = new String[2];
users[0] = "Lichard";
users[1] = "Omily";

ArrayList<String> chatHistory = new ArrayList<String>();
chatHistory.add(users[0] + ": hey omily derpa derpa doo");
chatHistory.remove(0);
chatHistory.add(users[1] + ": i saw that");
chatHistory.add(users[1] + ": mr derpa derpa doo");
chatHistory.add(users[1] + ": u mad bro?");
chatHistory.clear();
chatHistory.add(users[0] + ": hey um... whats up?");
int chatSize = chatHistory.size(); // int
boolean isOmilyInChat = chatHistory.contains(users[1])
```

#### Looping with an []

```java
String[] places = new String[4];
places[0] = "local 22";
places[1] = "rock bottom";
places[2] = "fado";
places[3] = "bed";

for (int i = 0; i < places.length; i++) {
    String place = places[i];
    System.out.println(place);
}
```
