## Intent to go to another Activity

```java
Button btnNext = (Button) findViewById(R.id.btn_next);
Intent mIntentToParty = new Intent(MainActivity.this, SecondActivity.class);

View.OnClickListener listener = new View.OnClickListener() {
   @Override
   public void onClick(View v) {
       Log.i("MAIN", "Click btn_next");
       startActivity(mIntentToParty);
   }
};

btnNext.setOnClickListener(listener);
```
#### Example

```java
public class SecondActivity extends AppCompatActivity {

    private Intent mIntentToBeLame;
    private Intent mIntentToLogin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_second);

        Button btnBack = (Button) findViewById(R.id.btn_back);
        Button btnLogin = (Button) findViewById(R.id.btn_sketch);
        mIntentToBeLame = new Intent(SecondActivity.this, MainActivity.class);
        mIntentToLogin = new Intent(SecondActivity.this, LoginActivity.class);

        View.OnClickListener listener = new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                Log.i("SECOND", "click btn_back");
                startActivity(mIntentToBeLame);
            }
        };

        View.OnClickListener sketchyLoginListener = new View.OnClickListener() {
          @Override
            public void onClick(View v) {
              startActivity(mIntentToLogin);
          }
        };

        btnBack.setOnClickListener(listener);
        btnLogin.setOnClickListener(sketchyLoginListener);
    }
}
```
