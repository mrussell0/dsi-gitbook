# Recursion Solutions

## Reverse String Solution
```java
public static String reverse(String ss) {
  if (ss.length() == 0) {
    return "";
  } else if (ss.length() == 1) {
    return ss;
  } else {
    String lastLetter = ss.charAt(ss.length() - 2);
    String beginning = ss.substring(0, ss.length() - 1);
    return lastLetter + reverse(beginning);
  }
}
```

![call stack visualization of reverse](screenshots/call-stack-reverse.png)

## Fibonacci Solution
```java
public static int fib(int n) {
  if (n <= 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else if (n == 2) {
    return 1;
  } else if (n > 2) {
    return fib(n - 1) + fib(n - 2);
  }
}
```

![call stack visualization of fib](screenshots/call-stack-fibonacci.png)
