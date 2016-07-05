## Passing Data Between Activities using Extras

We can pass data between different activities when their started and when they
end. We start activities by creating `intents`. We can "put extra" information
in an intent that starts a new activity. 

Gmail has at least two Activities. Let's imagine there is a `ViewInbox` activity
and a `ReadEmail` activity. When someone clicks on an email in the inbox the
`ViewInbox` activity, the activity needs to create a new intent to start a 
`ReadEmail` activity. Simply starting the `ReadEmail` activity isn't enough.
The `ReadEmail` activity needs to know what email it's supposed to display.
The `ViewInbox` activity puts extra information in the intent that specifies
which email should be displayed.

Here's some simple examples of how to put extra information in an intent,
and how to get it out.

#### Put Extras

```java
Intent mIntentToBeLame = new Intent(SecondActivity.this, MainActivity.class);
String message = "hey main, plz learn 2 be chill and not call the RA next time";
mIntentToBeLame.putExtra("MSG", message);
```


#### Get Extras

###### Example

```java
Intent prevActivity = getIntent();
String name = prevActivity.getStringExtra("NAME");
int age = prevActivity.getIntExtra("AGE", 0);
```

###### Methods

Extras can store lots of types of information. Here's all the different
methods associated with getting extra information out of an intent.

```java
getBooleanArrayExtra(String name)
getBooleanExtra(String name, boolean defaultValue)
getBundleExtra(String name)
getByteArrayExtra(String name)
getByteExtra(String name, byte defaultValue)
getCharArrayExtra(String name)
getCharExtra(String name, char defaultValue)
getCharSequenceArrayExtra(String name)
getCharSequenceArrayListExtra(String name)
getCharSequenceExtra(String name)
getDataString()
getDoubleArrayExtra(String name)
getDoubleExtra(String name, double defaultValue)
getExtras()
getFloatArrayExtra(String name)
float	getFloatExtra(String name, float defaultValue)
getIntArrayExtra(String name)
getIntExtra(String name, int defaultValue)
getIntegerArrayListExtra(String name)
getLongArrayExtra(String name)
getLongExtra(String name, long defaultValue)
getSerializableExtra(String name)
getShortArrayExtra(String name)
getShortExtra(String name, short defaultValue)
getStringArrayExtra(String name)
getStringArrayListExtra(String name)
getStringExtra(String name)
```

## Introduction: What are Intents? (10 mins)

Intent, as defined in the dictionary, means: purpose, goal, objective. *Something intends to do some goal*.

This translates to your app and activities; every activity has a goal.

For example, a `ComposeEmailActivity` allows the user to compose and send an email. If you click a "compose new email" button, you are actively saying "I intend to compose an email".

This is the idea behind Intents in Android. Intents are messages you send between app components, like Activities, usually with the intent of doing something.

> Check: So, imagine you are in your app's `EmailListActivity`, and you click on one of your emails. In plain ol' English, could you describe what is happening between the user and the EmailListActivity? Take 10 seconds to think about it.

The following "dialogue" is happening:

- EmailListActivity: "Hey, you clicked one of your emails. What's up?"
- You: "I intend on reading that email. Is that okay?"
- EmailListActivity: "Yeah, sure! I'll start the ReadEmailActivity now."
- You: "Thank you."

So, how does this look in code?

```java

	Intent intent = new Intent(EmailListActivity.this, ReadEmailActivity.class);
	startActivity(Intent);

```

You create a new Intent object, and you pass it two parameters: The activity you are currently in, and the class of the activity you intend to start. The code snippet above could be read as, *From the Email List Activity, please start the Read Email Activity*.

The method, `startActivity()`, starts the intended activity immediately.

> Check: What two parameters should you pass your Intent objects?

## Demo: Starting an activity with an Intent (10 mins)

Using the code from the previous demo, add a button to the app's main activity. Set an `onClickListener` to that button and have the listener start one of the other activities. Run the app in a virtual device, and click on the button to start the new activity. Feel free to codealong, if you'd like!

Note: A complete example of this is found in the [solution code folder](solution-code).

## Introduction: Sending data from one Activity to another Activity (10 mins)

Intents are how Activities communicate with each other. In the previous example, we started an activity to read an email by clicking an email in the list. However, how does the ReadEmailActivity know what email to show?

> Check: Take 30 seconds to talk with the person next to you about this question.

When you start a new activity, it is shown with the default settings that you give it. However, some activities need to receive a bit more information. This info is sent from the original activity to the one you are starting.

When creating new intents, you can also give it *extra* data. Here's an example:

```java

	Intent intent = new Intent(EmailListActivity.this, ReadEmailActivity.class);
	intent.putExtra("ID", 123);
	intent.putExtra("SENDER", "John Smith");
	startActivity(Intent);

```

> Check: Take 20 seconds to study the code and come up with an explanation, in English, about what's happening. Be ready to share!

The Intent class has a handful of helper methods you can call to get and store extra data. The main one is `putExtra()`, which takes two parameters: a String that gives the data a name, and the data itself.

With `Intent.putExtra()`, you can put data inside the intent (including Strings, numbers, booleans, certain objects).

Once you start a new activity, you can retrieve the Intent and get the sent data, as follows:

```java

	// get the intent that started this activity
	Intent intent = getIntent();

	// get the data from the intent
	int id = intent.getIntExtra("ID", 0);
	String sender = intent.getStringExtra("SENDER");

```

Again, the Intent class has a handful of getters for extra data, usually formatted like *get_____Extra*. Examples, `getIntExtra()`, `getStringExtra()`, `getBooleanExtra()`, etc.

**Note**: You should only send data if you need to do so. If the activity you are starting doesn't need extra data, you don't have to set it.

## Guided Practice: Sending Data between Activities (15 mins)

> Instructor Note: Show the class that getting data without setting it or with a type in the extra id would cause incorrect or null data. Then, after you introduce this exercise, be sure to stop the class after each step and reveal the answer.

With the person next to you, go ahead and start a new Android project with a empty main activity. Do the following:

- Add a new Activity, and call it `EchoActivity`.
- Take 2 minutes and do this: In `MainActivity`, add an `EditText` and a Button. In the `EchoActivity`, it will just have a `TextView`.
- Take 2 minutes and do this: In Java, set an `onClickListener` to the button and make it start the `EchoActivity`. The value of the `EditText` is passed in the intent.
- Take 2 minutes and do this: In the `EchoActivity`, the value is plucked from the intent and put in the TextView.

#### Independent Practice: Add two numbers (15 mins)

> This should be done as a pair programming exercise.

Now, with the person next to you, without stopping every two minutes, do the following:

* Create a new project, with a blank main Activity
* Create a new activity, call it SolutionActivity
* In the main activity, put two EditTexts and one button in the layout. The button's text will say "Add"
* In the solution activity, just have one TextView
* When the button is pressed, it takes the two values and sends them to the solution activity, where the sum of the two numbers are shown.

## Demo: Passing data back in the result (20 mins)

Passing data works in both directions, and you can receive data when returning from an Activity you previously started. For example, if you start SecondActivity from MainActivity, you can get data back from SecondActivity when it closes.

Returning data from an Activity only requires a few additions to your code.

This can be broken down into changes in your calling Activity (the one you are starting the second activity from), and changes in your secondary Activity.

Open the Starter-Code and follow along, if you'd like.

#### Second Activity

First, let's look at the second Activity, or the one you are passing the data back from. In this Activity, we press a button, and it passes the values from the two EditTexts back to the Main Activity.

> Check: How do you think we are going to pass data from the second activity to the first when clicking the button? Share out!

Just like when we're starting an Activity, we also pass data back using an Intent.

```java
mButton.setOnClickListener(new View.OnClickListener() {
@Override
public void onClick(View v) {
    Intent resultIntent = new Intent();
    resultIntent.putExtra("first",mFirstNameText.getText().toString());
    resultIntent.putExtra("last",mLastNameText.getText().toString());

    setResult(RESULT_OK,resultIntent);
    finish();
}
});
```

First we create an intent, then put the two Strings in as extras. The next two lines of code are new, though.

- **setResult**: This method takes two parameters. The first is a value that lets our first Activity know that everything went well, and that this Activity finished correctly. The second parameter is simply an Intent holding the data we want to pass back.
- **finish**: This method closes the current Activity and returns to the previous one.

#### Main Activity

Now that we've finished the Second Activity, let's return to the Main Activity. We have two steps to complete.

> Check: What are they? You know this by now.

We need to start the Second Activity and get the results from the Second Activity.

Starting the Activity is almost identical to how we previously did it, with one exception:

```java
Intent intent = new Intent(MainActivity.this,SecondActivity.class);
startActivityForResult(intent,NAME_REQUEST);
```

Notice the `startActivityForResult` method. The first parameter is a normal Intent, but the second is a variable telling the system what we are asking for (we will use this in a minute). We need to add that variable at the top of the Activity.

```java
private static final int NAME_REQUEST = 20;
```

You can assign any integer value that is **greater than 0**.

Next, we have to get the results from the Second Activity. Whenever you return from an Activity that is expecting results, the `onActivityResult` is automatically called.

> Check: Give the students 2 minutes to discuss what data they think will be returned to us based on what was passed into the second activity and what was returned in the result after pressing the button.

```java
protected void onActivityResult(int requestCode, int resultCode, Intent data) {
	// Check what request we're responding to...
	if (requestCode == NAME_REQUEST) {
	    // Make sure the request was successful...
	    if (resultCode == RESULT_OK) {
	        String firstName = data.getStringExtra("first");
	        String lastName = data.getStringExtra("last");
	        mText.setText(firstName+" "+lastName);
	    }
	}
}
```

The first parameter is the static variable we passed in when starting the activity, in our case `NAME_REQUEST`. The second parameter is the result status, in our case `RESULT_OK`. The final parameter is the Intent we passed back containing the data.

Since we could be starting different Activities from our Main Activity, we first have to check that our result is coming from the `NAME_REQUEST` activity, then we have to check to make sure the results are valid. After that, we can retrieve the data like normal and use it however we want.

> Check: What are the key differences between how we started activities before and what we just did?

## Independent Practice: startActivityForResult (10 mins)

**Do this activity with a partner**

This practice is going to be similar to the previous one but reversed: instead of passing values from the first activity to the second, we are going to give the user two options in the main activity, add and subtract.

If the user chooses add, they are taken to a different activity with two EditTexts where they type 2 numbers, and the sum is returned in the result of the main activity where it is displayed.

If the user chooses subtract, the same steps occur, except the difference is returned to the main activity.

> Check: Let's take 2 minutes to review the answer. Were all students able to complete the activity successfully? If not, where did you get stuck?

#### Conclusion (5 mins)

- What is an activity?
- What is an intent?
- How do we start an activity?
- How do we send data from one activity to another?
- How do we receive data when returning from an activity?

## Additional Resources

* Android Developer | Starting Activities - http://developer.android.com/guide/components/activities.html#StartingAnActivity
* Android Developer | Intents - http://developer.android.com/guide/components/intents-filters.html
