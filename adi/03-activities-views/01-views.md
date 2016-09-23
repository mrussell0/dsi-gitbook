
## Views

### Objectives

* Define what a Widget is
* Reference views in Java
* Change view properties in Java and XML
* Attach OnClickListeners to views

## Widgets

**Widgets** are the building blocks you use to create a user interface with. If you create a default application in Android Studio, you are presented two widgets for your first layout - `RelativeLayout` and `TextView`. Using the Android SDK, we can configure the appearance and behaviour of widgets. Each widget is an instance of the `View` class (or one of its subclasses, such as `ImageView` or `TextView`).

##### Common Widget Attributes

Let's become familiar with a few common attributes (which are better known as properties of an object) that we'll see.

* `layout_width` with values such as `match_parent` (the content will match the parent's size) and `wrap_content` (only as large as content requires)
* `layout_height` with values such as `match_parent` and `wrap_content`
* `padding` with values measured using `dp`
* `orientation` with values that allow content to be rendered in a `horizontal` or `vertical` fashion
* `text` with any **String** value, such as `Hello world!` or `Hi, grandpa!`



#### Basics - Views vs. Properties vs. Values

Think of a view as a component of the interface: buttons, text boxes, input fields.  All are views!

Every view has a number of properties specific to it. Some examples:

* In **TextView**, you are able to set the view's text, text color, font, etc.

	* In fact there are a number of other views that are "descendants" (or subclasses) of TextView and have the same properties you can set: Button, EditText
	* Notice how views that subclass TextView have all of its properties?

* In **ImageView**, you can set the view's image and how it is scaled within the view.
* In **ProgressBar**, you can set the current progress or if the view is indeterminate (where it spins indefinitely).

*All* views are a *subclass* (or "descendant") of **View.java**. "All views are views." So, exactly how a Button has all of the properties of a TextView, all views have core properties that are provided by the View "class".  We'll go over classes in depth at a later date.

The commonly used properties for all view types are:

* width
* height
* padding
* margins
* background
* alpha (opacity)
* id
* visibility

There are properties and attributes for each view. The Android website has a detailed reference to all of the popular views, properties, and how to change them. It's found here: [http://developer.android.com/develop/index.html](http://developer.android.com/develop/index.html). From there, you can use the search icon on the top right to search any view.

Also, you can just Google it! Usually Googling "Android *TypeOfView*" would have the #1 link lead directly to the view's reference page. Try it: Google "Android TextView".

## Referencing views in Java

Before we change view properties in Java, you have to learn how to reference the views you create.

Things to be aware of before you continue:

* Every view and layout has a java class that matches its XML counterpart.
	* ex., <TextView /> is defined by a Java, TextView.java.
* If you give a view or layout an id, it can then be used in Java for reference.
	* ex, **@+id/textView1** can be referenced in java as **R.id.textView1**.
	* **@+id/** is used in XML layout files, and **R.id** is used in Java.


To interact with views in your layouts, you have to get a reference to that view. Activities provide a helpful method, **findViewById()**.

```java
TextView textView = (TextView) findViewById(R.id.textView1);
```

`findViewById(R.id.textView1)`returns a view that has the id textView1. Notice how I said **"returns a view"** and not "returns a text view". TextViews, Buttons, RelativeLayouts, etc., are all Views (and subclass View.java). So, findViewById() returns a instance of View.

**Views have to be cast** if you want access to that view's specific functionality.

* ex. TextViews allow you to set a view's text, so you have to cast the result of findViewById(): **(TextView) findViewById(R.id.textView1);**

Now that you have a reference to your specific views, you can change the views to your liking!

## Demo: Changing view properties in Java (10 minutes)

Remember how you can set attributes to views in XML? Every attribute defined in XML can also be accessed and changed in Java. Usually, the attribute has a **get** and **set** method that matches the XML attribute. Example:

**XML**

```xml
<TextView
		android:id="@+id/textView1"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Text"
        android:textColor="#000000" />
```

**Java**

```java
TextView textView = (TextView) findViewById(R.id.textView1);

textView.setText("New Text");
textView.setTextColor(Color.BLACK);
```

##### Widgets are written as XML

Each widget is declared as an **XML element**. Each _attribute_ is an property of that widget.

## View Hierarchy

Widgets compose a hierarchy of `View` objects named **view hierarchy**. There will always be a _root_ (or base) element. This will typically be a layout (`LinearLayout`, `RelativeLayout`, `FrameLayout`, or `TableLayout`). These _layouts_ inherit from a subclass of `View` named `ViewGroup`. Widgets are then contained inside of these _groups of views_, or as we know them, `ViewGroup`s.


#### Users Interacting with Views

Every good app has some form of interaction. Usually, that means that the user can click the views on the screen. Examples:

* Tapping the *+* icon in Gmail to compose a new email
* Clicking the *Like* button on a Facebook post
* Clicking someone's profile photo to see more information in LinkedIn

All views are clickable by default. However, clicking a view will not do anything; they don't know what to do. So, in Java, you have to tell them what to do.

To do this, you have to create an OnClickListener and assign it to a view. As it sounds, it's an interface that listens for when the view is clicked. It has only one method, **onClick()**; this is where you put the code you want to run when the view is clicked. Here's how it looks:

```java

    OnClickListener myOnClickListener = new View.OnClickListener() {
    	@Override
    	public void onClick(View v) {
    		// do stuff here
    	}
    });

    Button button = (Button) findViewById(R.id.button1);

    button.setOnClickListener(myOnClickListener);
```

With the above code, we created a new OnClickListener and set it to a button. Now, whenever that button is clicked, it will call the listener's onClick() method and run the code we writ in `// do stuff here`.

--

Note: This is worth repeating. ***All*** views are clickable, not just buttons. You can click a TextView, a ProgressBar, etc. Buttons are special because they are visually clickable; i.e., a button looks pressed when a user touches it and raised when it's not.

#### Putting it all together

Let's assume we have a layout, *activity_blue.xml*, with two views: a TextView and a Button. They have the ids *textView* and *button*, respectively.

When we click the button, it sets the color of the TextView to blue.

Here's how the Activity would look. All of the code is defined in the activity's **onCreate()** method, which is talked about more in detail at a future lesson. Just know that onCreate is called when the activity starts, and that it loads your created layout with setContentView().

```java

    public class BlueTextActivity extends AppCompatActivity {

        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_blue);

            // Create references to the views inside of activity_blue.xml

            Button blueButton = (Button) findViewById(R.id.button);

            // Create the onClickListener for the button

            OnClickListener buttonOnClickListener = new View.OnClickListener() {
                @Override
                public void onClick(View v) {
                    TextView textView = (TextView) findViewById(R.id.textView);
                    textView.setTextColor(Color.BLUE);
                }
            };

		    // Set your onClickListener to the button

            blueButton.setOnClickListener(buttonOnClickListener);
        }
	}
```


## Independent Practice

> ***Note:*** _This can be a pair programming activity or done independently._

Create a Hello World app! I will share the code above to use as a reference.  

The app should do the following:

* Layout with two views: A TextView and a Button
	* The TextView should start off with no text, but have a text size of 30sp
	* The Button should have the text, "Say hello"
* When you click the button, the text in the TextView should say "Hello!"

## Conclusion
* How do you reference a view in Java?
* How does a OnClickListener work?
* How do you change view properties in XML? In Java?
