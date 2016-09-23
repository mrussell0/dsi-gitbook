## Step by Step: Adding a ListView

#### Ingredients (variables)

_These can be member variables or declared at run time inside whatever method you so choose_.

* ArrayList<T>
* ListView
* ArrayAdapter
* OnItemClickListener

#### Recipe

1. Declare our variables. These are defined in the ingredients list above.
2. Find your ListView using `findViewById()` and assign it to your ListView
3. Populate (or add) data to your ArrayList<T> (this may require instantiation).
4. Add a `list_view_row` layout. The root element **must** be a TextView. Feel free to customize this as you want for now.
5. instantiate our new ArrayAdapter. The first argument is our context (`this` or `MainActivity.this`), the second is our list_view_row layout (`R.layout.your_row_name`); the final argument is our ArrayList (`mArrayList`). **This binds our List of data to our ListView**. Super, big, important deal. Thanks, ArrayAdapter - you da real MVP.
6. instantiate our OnItemClickListener and make sure it is declared as a child of `AdapterView` or things may not work as intended.
7. Override the `onItemClick` method inside of your OnItemClickListener to do things.
8. Attach our OnItemClickListener to our ListView to bind everything together. This uses the ListView.`setAdapter()` method with your ArrayAdapter as an argument.
9. Done. :) Run. yay. party.

## Challenge

* Follow the above instructions to create a new Android app for your favourite food.
* Gotta eat 'em all.
