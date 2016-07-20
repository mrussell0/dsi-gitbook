# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Singletons - The Case Against

### Objectives
*After this lesson, students will be able to:*

* Identify why a Singleton design pattern is not usually a desireable choice 
* Show alternatives to this design pattern and explain why they are preferable

### Preparation
*Before this lesson, students should already be able to:*

- Use a singleton design patter


## Introduction: Singeton Metaphor (15 minutes)

#### Can you cook in your bathroom?

This might be a silly question, but of course you can. You can take a tiny stove into your bathroom, put it down in front of you, and make an omelette. 

#### Should you cook in your bathroom?

Probably not. You already have a place for cooking. Go to the kitchen an do your cooking there. The bathroom is where you do your bathroom things.

You don't have one room in your house for every single activity that you want to do. It would be weird if you had a toilet right in the middle of your kitchen.

Just look around you. Even businesses have a singular function. A bank does bank things. A grocery store does grocery store things. If a grocery store needs to make a transaction with a customer's bank, they let the bank know and the bank handles it. The bank then notifies the grocery store that the customer has paid and the grocery store gets the customer's money. These two processes separate their functionality into different services, because they are both made to do two different things. 

#### What does this even have to do with a singleton pattern?

A singleton pattern is one class that holds all the values you want to have all your other activities access. This is the equivalent of 