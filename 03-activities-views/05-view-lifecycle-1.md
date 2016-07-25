# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Activity Lifecycle (part 1)

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Describe the basic components to the activity lifecycle
- Implement saving state on rotation using Bundles


### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Declare and use Java Lists
- Describe the basics of Android Views

---
<a name="opening"></a>
## Opening (5 mins)

The Activity Lifecycle is a critical concept to understand when designing any Android application, especially those with multiple activities. When you change activities, switch between apps, or even when the system decides to crash, your app and its Views can be stored in memory with little notice. You must understand how the Lifecycle works in order to make your app react appropriately to these events.

> Check: Ask the students to give an anecdotal example of where they think the lifecycle comes into play.


<a name="introduction"></a>
## Introduction: Stages of the Activity Lifecycle (25 mins)

The Activity Lifecycle is split into six distinct states that are triggered in a specific order when your activities are changing. The image below shows the six states and the order they happen in.

<img src="./screenshots/basic-lifecycle.png">
(Image from [Android Developer Reference](http://developer.android.com/training/basics/activity-lifecycle/starting.html))

**Created:** This happens after `onCreate()`, a familiar method by now, is called. At this point, the activity can begin to set up any of the data it needs and can prepare the view for when it is made visible.

**Started:** At this point, the activity is now visible but cannot be interacted with.

**Resumed:** When the activity is Resumed, it is fully running and ready to use. It can be interacted with by the user.

**Paused:** When the activity is paused, it is still visible in the background, but there is another activity covering it. The paused activity cannot be interacted with, and `onResume()` must be called before interacting with it again.

**Stopped:** When the activity is stopped, it is completely hidden from the user. This could be another activity within your app, the user returning to the home screen, or even another app being launched.

**Destroyed:** The activity is released from memory and must be recreated to be used again. Activities can be destroyed by your app or by the system if it needs to reclaim memory.

### Method Callbacks in the Lifecycle

While the image above shows the states of the Lifecycle, it doesn't show why the states change. The image below goes into more detail.

<img src="./screenshots/activity_lifecycle.png">

One important thing to notice is that it clarifies when `onCreate` is called and member variables must be recreated. For instance, the activity is no longer considered visible when you rotate the screen!

`onRestart` is called when the user navigates back to the previous activity and the **app process was not killed**.

When combined, the two images above give a very clear picture on what causes these methods we have seen pop up in our apps to be called.

> Check: Ask the students to identify what view helper methods we have used so far; they should also explain why they would be used in a particular situation; for example, `onCreate`, used to setup Views because the Views aren't visible yet.


<a name="demo"></a>
## Demo: Method Callbacks in the Lifecycle (10 mins)

Imagine we had an app with the following method callbacks:

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
  super.onCreate(savedInstanceState);    setContentView(R.layout.activity_next);
  Log.d(TAG, "onCreate");
}

@Override
protected void onStart() {
    Log.d(TAG,"onStart");
    super.onStart();
}

@Override
protected void onResume() {
    Log.d(TAG,"onResume");
    super.onResume();
}

@Override
protected void onPause() {
    Log.d(TAG,"onPause");
    super.onPause();
}

@Override
protected void onStop() {
    Log.d(TAG,"onStop");
    super.onStop();
}

@Override
protected void onDestroy() {
    Log.d(TAG,"onDestroy");
    super.onDestroy();
}

@Override
protected void onRestart() {
    Log.d(TAG, "onRestart");
    super.onRestart();
}
```

Notice what methods are being used:

```
onCreate
onStart
onResume
onPause
onStop
onDestroy
```


Imagine we started the app, then closed it.

> Check: Ask the students to predict and write out what order the messages from the callback methods would show up if an app was started, another activity was called, and then the second activity was closed, returning the user to the first one.
(onCreate, onStart, onResume, onPause, onCreate, onStart, onResume, onStop, onPause, onRestart, onStart, onResume, onStop, onDestroy)


<a name="introduction"></a>
## Introduction: Saving State with Bundles (20 mins)

Now that we've covered when the Lifecycle callback methods are called, we can put them to use! Overriding these methods allows us to save the state of the activity in case it is removed from memory. If this happens, all member variables (ie loaded data, references to UI elements) will be lost.

There are many ways of saving and restoring the state of the activity, but we will be covering using Bundles for this lesson. In the next lesson, we will implement some of the other techniques. Generally, saving and restoring with bundles is used when you want to be able to restore state (also known as current state or state data) when the app is still active, but it is ok if state is lost when the entire app is closed. The opposite of that is persistent state, which uses persistent data. An example of this is data for application preferences.

A bundle is a data structure that allows you to store data by associating a unique key with the data. Two things:

- The key must be a String
- The values stored can be any type of data including, but not limited to: ints, doubles, Strings, ArrayLists, or any custom class

For example, if we were tracking the number of times a button was clicked in a variable called `mNumClicks`, we could use the following code for storing and retrieving the data:

```java
//storing
exampleBundle.putInt("numberOfClicks",mNumClicks);

//retrieving
mNumClicks = exampleBundle.getInt("numberOfClicks");
```

To save and restore the current state of the activity, we will be using the onSaveInstanceState and onCreate methods. onSaveInstanceState is called before an activity might be killed, giving you the opportunity to save data.

Saving and restoring data should be used carefully. While it is loading data, the UI is paused and cannot be interacted with. If you are loading massive amounts of data, there will be large pauses in your app.


<a name="demo"></a>
## Guided Practice: Saving State with Bundles (10 mins)

 We will make an app that saves and displays the time the app was launched and restores that value when the activity is destroyed and restarted. To do this, we save the time instance variable in `onSaveInstanceState`, and retrieve it in `onCreate`.

 In the [starter code](https://github.com/ga-students/view-life-cycle-1-starter-code), load up the project `SaveActivityCreationTime`.

 We will destroy the activity by rotating the device.

> Check: Ask the students what would happen if we didn't save the data but still tried to restore by checking if the bundle was null (The label would be blank)


<a name="independent-practice"></a>
## Independent Practice: Saving State with Bundles (15 mins)

In this practice you will be creating a simple app that has an `EditText` for your name with a Button to submit it. When you press the button, it prints out the following message in a TextView below "Hello NAME! You will be saved into the bundle! X names have been saved." X is a counter for the number of times the button has been clicked. In the [starter code](https://github.com/ga-students/view-life-cycle-1-starter-code), load the project `HelloNameSaveState`.

> Check: Were students able to successfully solve the problem or complete the task?

<a name="conclusion"></a>
## Conclusion (5 mins)

We learned a lot about the Activity Lifecycle during this lesson and now have the ability to save the basic state of the activity. This is very important in production apps because users don't want to have their Views being reset every time they move between activities. In the next lesson, we will continue covering saving data but using persistent storage.



### ADDITIONAL RESOURCES
- [Starting an Activity](http://developer.android.com/training/basics/activity-lifecycle/starting.html)
- [Pausing and Resuming an Activity](http://developer.android.com/training/basics/activity-lifecycle/pausing.html)
- [Stopping and Restarting an Activity](http://developer.android.com/training/basics/activity-lifecycle/stopping.html)
- [Recreating an Activity](http://developer.android.com/training/basics/activity-lifecycle/recreating.html)
