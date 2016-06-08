# Challenge: Identifying Layouts

Below are real Android Studio application layouts. Can you identify the XML elements and attributes in each?

## Hello World

```xml
<?xml version="1.0" encoding="utf-8"?>
<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:paddingBottom="@dimen/activity_vertical_margin"
    android:paddingLeft="@dimen/activity_horizontal_margin"
    android:paddingRight="@dimen/activity_horizontal_margin"
    android:paddingTop="@dimen/activity_vertical_margin"
    app:layout_behavior="@string/appbar_scrolling_view_behavior"
    tools:context="org.androidlayoutplayground.codeforcoffee.androidlayoutplayground.MainActivity"
    tools:showIn="@layout/app_bar_main">

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hello World!" />

    <Button
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Click me for things to happen"
        android:id="@+id/button"
        android:layout_alignParentTop="true"
        android:layout_alignParentStart="true" />
</RelativeLayout>
```

## Web View App

```xml
<FrameLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:background="#0099cc"
    tools:context=".FullscreenActivity">

    <!-- The primary full-screen view. This can be replaced with whatever view
         is needed to present your content, e.g. VideoView, SurfaceView,
         TextureView, etc. -->
    <!-- This FrameLayout insets its children based on system windows using
         android:fitsSystemWindows. -->
    <FrameLayout android:layout_width="fill_parent"
                 android:layout_height="match_parent"
                 android:fitsSystemWindows="true"
                 android:layout_gravity="center_horizontal|top"
                 android:layout_marginRight="-95dp"
                 android:layout_marginLeft="311dp">
        <LinearLayout android:id="@+id/fullscreen_content_controls"
                      style="?buttonBarStyle"
                      android:layout_width="fill_parent"
                      android:layout_height="fill_parent"
                      android:layout_gravity="bottom|center_horizontal"
                      android:background="@color/black_overlay"
                      android:orientation="horizontal"
                      tools:ignore="UselessParent">
        </LinearLayout>
    </FrameLayout>

    <WebView
            android:layout_width="fill_parent"
            android:layout_height="fill_parent"
            android:id="@+id/WebView"
            android:layout_gravity="left|top"
            android:clickable="true"
            android:focusable="true"/>

</FrameLayout>
```
