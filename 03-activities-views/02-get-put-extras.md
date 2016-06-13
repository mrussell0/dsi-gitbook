## Passing Data Between Activities using Extras

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
