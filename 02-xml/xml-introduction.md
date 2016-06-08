# What is XML?

**XML** stands for *extensible markup language*. It is the base schema that is used by HTML, so you may already be familiar with XML.

## XML Tags

XML contains **tags**. These are defined as something of importance. When it comes to Android, **tags** can be *various user interface components* such as a `TextView` (which is an element that renders text on the phone). A tag could look like `<someTag>`. Notice the starting `<` and closing `>`. These define our tags by wrapping around them.

Each *tag* contains a **start** and an **end** tag. Alternatively, some tags may be **abbreviated** (also known as self-closing). Let's take a look at what those look like:

A TextView that contains a *start* and *end* tag:
```xml
<TextView></TextView>
```

A TextView that is self-closing:

```xml
<TextView />
```

Let's consider a **Button**:

```xml
<Button></Button>
```

```xml
<Button />
```

### Checking for Understanding

* Each XML tag must be *wrapped* with special characters. What are they?
* What is the primary difference between these two types of **XML Tags**?
* Which of these two types appears easier (or more convenient) to write?
