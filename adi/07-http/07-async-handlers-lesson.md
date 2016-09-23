---
title: Async Tasks and Handlers
type: Lesson
duration: "45 min"
creator:
    name: Brad Zimmerman
    city: SEA
---



# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Async Task, Handlers, Loaders

### LEARNING OBJECTIVES
*After this lesson, you will be able to:*
- Implement Async Tasks in an application
- Implement Handlers in an application

### STUDENT PRE-WORK
*Before this lesson, you should already be able to:*
- Explain an activities lifecycle
- Know the basic concept behind threading in software

### INSTRUCTOR PREP
*Before this lesson, instructors will need to:*
- Know about Android? Seriously, why is this section here?

---

<a name = "opening"></a>
## Opening (5 min)

We already have some background in consuming an API's data, but we need to go over what to do when an API requires you to make authenticated requests. Often times when dealing with third-party API's (Google, Twitter, etc.) access to certain data are contingent upon being authenticated by the third-party's server.

> Check: What does this mean, in laymen's terms?

What this means is that for every time we use the API, it wants to know who we are, and more specifically, that we have the authority to interact with their endpoints. This process of authenticating with a third-party API is known as OAuth (Open Authorization). For today's lesson we will gain an understanding of how OAuth works, as well as other related API authentication concepts by building an app which shows user's Instagram photos posted in the vicinity of their current location.

---

<a name = "introduction"></a>
## Introduction: Handlers (15 min)

A Handler object registers itself with the thread in which it is created. It provides a channel to send data to this thread. For example, if you create a new Handler instance in the onCreate() method of your activity, it can be used to post data to the main thread. The data which can be posted via the Handler class can be an instance of the Message or the Runnable class. A Handler is particular useful if you have want to post multiple times data to the main thread or update UI elements.

To create a handler, simply use the following code:

```java
  private final Handler myHandler = new Handler() {
      public void handleMessage(Message msg) {}
      }
  }
```

But that handler is kind of boring. It doesn't do anything! Let's add some parsing to make the handler do different things depending on the input we send to it.

```java
  private final Handler myHandler = new Handler() {
      public void handleMessage(Message msg) {
          final int what = msg.what;
          switch(what) {
            case DO_UPDATE_TEXT: doUpdate(); break;
            case DO_THAT: doThat(); break;
          }
      }
  }
```

To send the handler a message, we just need to add the line:

```java
  myHandler.sendEmptyMessage(DO_UPDATE_TEXT);
```

And that's it! Say you want to send some data to a handler. You just add the data to the message, much like an intent.

```java
  Message m = new Message();
  Bundle b = new Bundle();
  b.putInt("what", 5); // for example
  m.setData(b);
  myHandler.sendMessage(m);
```

Then pull it out in the handleMessage method like so:

```java
  private final Handler myHandler = new Handler() {
    @Override
    public void handleMessage(Message msg) {
      int sentInt = msg.getData().getInt("what");
    }
  }
```

But why the hell do we even need handlers? It looks like we are just sending data to ourselves. Unless there's a very specific reason we need them...

<a name = "introduction"></a>
## Introduction: ASyncTasks (15 min)

The AsyncTask class allows to run instructions in the background and to synchronize again with the main thread. It also reporting progress of the running tasks. AsyncTasks should be used for short background operations which need to update the user interface.

The Async task has only four methods, they are as follows:

 - onPreExecute(): invoked on the UI thread before the task is executed. This step is normally used to setup the task, for instance by showing a progress bar in the user interface.

 - doInBackground(Params...): invoked on the background thread immediately after onPreExecute() finishes executing. This step is used to perform background computation that can take a long time. The parameters of the asynchronous task are passed to this step. The result of the computation must be returned by this step and will be passed back to the last step. This step can also use publishProgress(Progress...) to publish one or more units of progress. These values are published on the UI thread, in the onProgressUpdate(Progress...) step.

 - onProgressUpdate(Progress...): invoked on the UI thread after a call to publishProgress(Progress...). The timing of the execution is undefined. This method is used to display any form of progress in the user interface while the background computation is still executing. For instance, it can be used to animate a progress bar or show logs in a text field.

 - onPostExecute(Result): invoked on the UI thread after the background computation finishes. The result of the background computation is passed to this step as a parameter.

 The Async task takes in three values: AsyncTask <TypeOfVarArgParams , ProgressValue , ResultValue>. Here is what they do:

 - TypeOfVarArgParams: The input values for the doInBackground() method
 - ProgressValue: The type of the progress units published during the background computation
 - ResultValue: The input values returned from the doInBackground() method. Also the input for onPostExecute (obviously).

 So how do we use it?

```java
//Notice how the second and third variables are types. All of the values send through on execute() are put into the URL array
private class DownloadFilesTask extends AsyncTask<URL, Integer, Long> {

  //"URL... urls" is a fancy way to send an array into a function. That's all URL is. A function. Super confusing, I know.
  protected Long doInBackground(URL... urls) {
      int count = urls.length;
      long totalSize = 0;
      for (int i = 0; i < count; i++) {
          totalSize += Downloader.downloadFile(urls[i]);
          publishProgress((int) ((i / (float) count) * 100));
          // Escape early if cancel() is called
          if (isCancelled()) break;
      }
      return totalSize;
  }

  //This function is called when publishProgress() is called
  protected void onProgressUpdate(Integer... progress) {
      setProgressPercent(progress[0]);
  }

  protected void onPostExecute(Long result) {
      //The result here is the value returned from doInBackground
      showDialog("Downloaded " + result + " bytes");
  }
}
```

```java
//The three values here are sent directly into the URL array in doInBackground()
new DownloadFilesTask().execute(url1, url2, url3);
```



<a name = "conclusion"></a>
## Conclusion (5 min)

- Why do we use AsyncTasks?
- Why do we use Handlers?
