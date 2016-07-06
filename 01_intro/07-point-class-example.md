# Point Class

Here's a file defining a point class and a main program that runs and interacts with
the point class.

The point class demonstrates the following properties:
- it has private `x` and `y` properties
- it has getters and setters for `x` and `y`
- `setX` and `setY` have logic that prevents negative numbers from being set.
- it implements a `toString` method
- it implements a nice `equals` method
- it implements a `distance` method that computes the distance between two points.

## Point.java

```java
public class Point {
    private int x;
    private int y;

    // New points default to zero zero if no coordinates
    // are provided.
    public Point() {
        // we call the regular constructor inside
        // the zero-arg constructor to reduce redundancy
        this(0, 0);
    }

    public Point(int x, int y) {
        setX(x);
        setY(y);
    }

    public int getX() {
        return x;
    }

    public void setX(int x) {
        if (x >= 0) {
            this.x = x;
        }
    }

    public int getY() {
        return y;
    }

    public void setY(int y) {
        if (y >= 0) {
            this.y = y;
        }
    }

    public double distance(Point p2) {
        int dx = this.x - p2.x;
        int dy = this.y - p2.y;
        return Math.sqrt(dx * dx + dy * dy);
    }

    public boolean equals(Object other) {
        if (other == null) return false;
        if (other == this) return true;
        if (!(other instanceof Point))return false;

        Point p2 = (Point)other;
        return (this.x == p2.x) && (this.y == p2.y);
    }

    public String toString() {
        return "(" + this.x + "," + this.y + ")";
    }
}
```

## MainPoint.java

```java
public class MainPoint {
    public static void main(String[] args) {
        Point origin = new Point();

        Point p1 = new Point(1, 2);
        Point p2 = new Point(3, 4);
        Point p3 = new Point(3, 4);
        Point p4 = p1;

        System.out.println("p1 == p1? " + (p1 == p1));
        System.out.println("p1 == p2? " + (p1 == p2));
        System.out.println("p2 == p3? " + (p2 == p3));
        System.out.println("p1 == p4? " + (p1 == p4));

        System.out.println("p1: " + p1);
        System.out.println("p4: " + p4);

        // changing the value of x of p1 changes it at the object level.
        // p4 refers to the same object so printing p4 will see the new
        // value too.
        p1.setX(5);

        // Setting p1 equal to a new Point only changes what p1 points too.
        // p4 still points to the original Point object.
        p1 = new Point(7, 8);

        System.out.println("p1: " + p1);
        System.out.println("p4: " + p4);

        System.out.println("p1.equals(p1)? " + p1.equals(p1));
        System.out.println("p1.equals(p2)? " + p1.equals(p2));
        System.out.println("p2.equals(p3)? " + p2.equals(p3));
        System.out.println("p1.equals(p4)? " + p1.equals(p4));

        // the setX method has logic which prevents x and y from being
        // set to Negative numbers.
        p1.setX(-99);

        System.out.println(p1);
    }
}
```
