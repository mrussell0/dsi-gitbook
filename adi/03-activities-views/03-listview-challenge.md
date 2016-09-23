## ListView Challenge: Fix This Code

Create a new project. Build an activity that contains a ListView with two types of interaction. Pressing the FloatingActionButton should add a new list item containing whatever text the student wants. If the student long-presses on a specific list item, that item should be deleted. Basic code for the FloatingActionButton and long click detection will be provided below as starter code that you can copy/paste or type in by hand. _Don't forget to add a layout for your rows!_

#### Starter Code

```java
public class MainActivity extends AppCompatActivity {
    ArrayList<String> mStringList;
    ArrayAdapter<String> mAdapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //Instantiate your LinkedList
        mStringList =

        //Instantiate your adapter
        mAdapter =

        //Get your ListView and set the adapter
        ListView listView =

        //Complete the FloatingActionButton onClick method to add a list item
        FloatingActionButton fab = (FloatingActionButton)findViewById(R.id.fab);
        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {

            }
        });

        //Complete the ListView onItemLongClick code to remove list items
        listView.setOnItemLongClickListener(new AdapterView.OnItemLongClickListener() {
            @Override
            public boolean onItemLongClick(AdapterView<?> parent, View view, int position, long id) {
                return true;
            }
        });

    }
}
```
