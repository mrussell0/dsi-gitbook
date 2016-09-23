---
title: Content Providers & Permissions
duration: "30 min"
creator:
    name: Brad Zimmerman
    city: SEA
---

# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Content Providers
Week 4 | Lesson 4

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Use a content provider to access any global data on a user's phone
- Show the content provider results in the UI

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Understand the code supporting Cursor behavior
- Understand how to iterate through a cursor

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Gather materials needed for class
- Complete Prep work required
- Prepare any specific instructions

---
<a name="opening"></a>
## Opening (5 mins)

What is a content provider? A content provider is a way for Activities to access structured data shared between different applications on the phone. It's basically a way to access data in public databases on your phone that all applications should have access to.

> Check: What databases do you think your phone provides to all activities?

***

<a name="introduction"></a>
## Introduction: Content Providers (15 mins)

There's nothing here that we haven't already learned Content Providers are just databases that exist on the Android phone for all applications to use. All you need to know is where these databases are in the phone's file system, and you will be able to manipulate them the same way you would with a normal database; Let's look at what a few of these are:

```java
  //Contacts => ContactsContract.Contacts.CONTENT_URI
  //Messaging (Usually) => content://sms/
  //Calendar => CalendarContract.Calendars.CONTENT_URI
```

But how do we get the cursor back from the database once we know the address? That's the easy part!

```java
  Cursor cursor = getContentResolver().query(Uri.parse("content://sms/"), null, null, null, null);
```

That's all you have to do! You can now iterate through the user's databases as you please! Or can you...

***

## Demo: Try it out! (10 mins)

Copy and paste the code snippet from the previous paragraph into your code. Add a few lines to iterate through the cursor and run your application.

> Check: What happened when you tried to run your application?

> Check: Why can't every app use these content resolvers to steal information off of your phone?

***

## Demo: Permissions (10 mins)

Android requires permissions before it allows applications to read or write to the databases on your phone.

> Check: Why is this a very very good practice?

Add the following code snippet to your manifest between the <manifest> and <application> tags. Then run your code again.

```java
  <uses-permission android:name="android.permission.READ_SMS"/>
```

Pretty awesome right? Remember every content provider has their own permissions needed to access/write information to the content provider. Check the following link for more information on which permissions you need to access the different content providers

### ADDITIONAL RESOURCES
- [Content Providers](https://developer.android.com/guide/topics/providers/content-providers.html)
