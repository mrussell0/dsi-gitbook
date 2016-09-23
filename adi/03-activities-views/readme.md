# Activities, Views, & Intents

It is time to dig into Android. We're going to start by learning about Activities, Views, and Intents. These three topics will lay the foundation for building Android apps that are fantastic.

## What you'll learn

We'll cover the following fundamental topics during this section of class:

* Classes, Subclasses, and Object Oriented programming
* Activities and Activity Lifecycle
* Views and Layouts
* Intents
* Event Listeners
* Custom Adapters
* Android Debugging
* Resource file best practices

## Project

You'll demonstrate master of this content with your next project, the Todo List.

# What is an Activity?

The definition of an activity is something that is done for a particular purpose.

Think about the activity that the user is doing on a screen. If you are looking at a screen whose purpose is to log in the user, for example, it should be called the Login Activity. If the activity shows a user's social network profile , it should be called the User Profile Activity.

An Activity is a plain ol' Java class, so you already know how to add it to a project.

Right click on the folder where you want to put the activity, then go to *New* > *Activity*, and then click on the type of base activity you want (usually, *Empty Activity* is what you want if you want to build it from scratch).

Doing this also adds the Activity to the Android Manifest.

> Check: So what is an activity again?

# What is a Manifest?

The dictionary defines a ship's manifest to be "a document giving comprehensive details of a ship and its cargo and other contents, passengers, and crew for the use of customs officers."

The ship, in our case, is the app you are building.

The Android Manifest xml file presents important information about your app to the Android system. If something isn't defined in the manifest, then the system just ignores it.

Notably, the manifest is known for describing the main components of your app; the Activities, Services, Content Providers, etc. It is also the place to define permissions (e.g., giving your app permission to access the internet or to access a device's camera).

Whenever you create a new Activity, if it is not automatically added, it should be added to the manifest. Otherwise, the app will crash.

> Check: How do activities relate to the manifest?

# What are Intents?

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

