# N5 Computing Science
{:.no_toc}

[Home](index.md)

___Work in Progress___

## Web Design and Development
{:.no_toc}

**Note:** HTML, CSS, and JavaScript use American spelling so when you see `center` or `color` they are not typos.

All the code examples will work with [Replit](https://replit.com/).

## Table of Contents {#toc}
{:.no_toc}

* TOC will be displayed here
{:toc}

## Hypertext Markup Language (HTML) 

### HTML

HTML uses elements to display content.  An element normally consists of opening (`<tag>`) and closing (`</tag>`) tags, with the content to be display contained between the tags.

HTML is not whitespace sensitive.  This means a statement can be all on a single line or split over multiple lines.

``` html
<tag>content</tag>

<tag>
    content
</tag>
```

Opening tags can have attributes.

``` html
<tag attribute="value">
    content
</tag>
```

All element  HTML documents are contained within the opening and closing `html` tags.

``` html
<!DOCTYPE html>
<html lang="en-gb">

</html>
```

#### Information

##### Comments

Single line comment.

``` html
<!-- This comment is not displayed -->
```

Multiline comment.

``` html
<!--
This comment is not displayed
This comment is not displayed
-->
```

##### Display information

Without HTML tags information is displayed as plain text, but with tags it will have the formatting associated with the tag.

``` html
Hello world
```

### HTML document (Webpage)

A HTML documen has two main parts:

 * __head__: information about the page
 * __body__: the content that is displayed

``` html
<!DOCTYPE html>
<html lang="en-gb">

    <head>
    </head>

    <body>
    </body>

</html>
```

[Back to Table of Contents](#toc)

### Head

#### Title

The webpage title will be displayed on the browser tab:

``` html
<title>My Web Page</title>
```

#### StyleLink

The [CSS](#css) for a webpage can be internal using the `style` tag.

``` html
<style>
    <!-- CSS rules go here -->
</style>
```

#### 

The [CSS](#css) for a webpage can be in an external file using the `link` element.

``` html
<link href="styles.css" rel="stylesheet" type="text/css">
```

___Note___: A few HTML elements do not have a closing tag, and `link` is one of them.

[Back to Table of Contents](#toc)

### Body
#### Heading

There are six levels of heading.

``` html
<h1>Highest level heading</h1>

<h3>Mid-level heading</h3>

<h6>Lowest leveleast heading level</h6>
```

#### Paragraph

``` html
<p>A paragraph of text.</p>
<p>Another paragraph of text.</p>
<p>Plus another paragraph of text.</p>
```

#### Lists

Lists can be ordered (`ol`) or unordered `ul`).  Both types of lists contain list items (`li`).

##### Ordered list - Numbered
{:.no_toc}

``` html
<ol>
    <li>First list item</li>
    <li>Another list item</li>
    <li>Last list item</li>
</ol>
```

##### Unorderd list - Bullet points
{:.no_toc}

``` html
<ul>
    <li>First list item</li>
    <li>Another list item</li>
    <li>Last list item</li>
</ul>
```

[Back to Table of Contents](#toc)

#### Division

The `<div>` tag is used to divide the webpage into different parts.

``` html
<div>
	<h1>First area</h1>
<div>

<div>
	<h1>Second area</h1>
<div>
```

#### Anchor (Hyperlinks)

##### External
{:.no_toc}

Link to an external website, using asote aressin

``` html
<a href="https://mrfriendcs.github.io/">N5 CS Help</a>
```

##### Internal
{:.no_toc}

Link to another webpage, in the same folder, using relative addressing.

``` html
<a href="home.html">Home</a>
```

#### Media

To ensure that media is displayed / played correctly the `type` attribute is used.

| File type | Type |
| --------- | ---- |
| jpeg / jpg | image/jpeg |
| png | image/png |
| mp3 | audio/mpeg |
| mp4 | video/mp4 |

##### Image

The image tag (`<img>`) has three attributes.  The first (`src`) is where the image is located, and can use relative or absolute addressing.  The second (`alt`) is the alternative text that will be displayed if the image can't be displayed, and is used by screen readers.

``` html
<img src="laptop.jpg" alt="Laptop on a table">
```

##### Audio

``` html
<audio controls src="clapping.mp3">  
    No audio player available
</audio>
```

##### Video

``` html
<video controls src="clapping.mp4">  
	No video player available
</video>
```

## Classes and IDs

HTML elements can have additional attributes for `class` and `id` which are useful applying [CSS](#css) rules to specific elements, and can be used by [JavaScript](#js).

A class can be assigned to one or more cascading Style Sheets (CSS), whereas an ID can only be applied to one element on a page.

#### Classes

``` html
<p class="highlight">A paragraph.</p>
<p>Another paragraph.</p>
<p class="highlight">Plus another.</p>
```

#### IDs

``` html
<p id="main">A paragraph.</p>
<p>Another paragraph.</p>
<p>Plus another.</p>
```

#### Classes and IDs

An element can have an ID and a class.

``` html
<p id="main" class="highlight">A paragraph.</p>
<p>Another paragraph.</p>
<p class="highlight">Plus another.</p>
```

[Back to Table of Contents](#toc)

## Cascading Style Sheets (CSS) {#css}

### Information

#### Comments

Single line comment.

``` css
/* This comment is not displayed */
```

Multiline comment.

``` css
/*
This comment is not displayed
This comment is not displayed
*/
```

### CSS rules

Rules are terminated with a semicolon, **`;`**. A rule will be applied without a semicolon but multiple rules will not.

#### Single property

``` css
selector {property: value;}
```

#### Multiple properties

``` css
selector {property: value;
          property: value;}
```

### Selectors

#### Element selectors

Element selectors are HTML tags without the angle brackets.  All elements of that type will have their formatting modified by the CSS rule(s).

``` css
p {property: value;}
```

#### Class selectors

Class selectors use the class name with a dot in front.

``` css
.mainPara {property: value;}
```

#### ID selectors

ID selectors use the ID name with a hash in front.

``` css
#otherPara {property: value;}
```

#### CSS Precedence

##### Selectors

 * Element rules overwrite default rules
 * Class rules overwrite element rules
 * ID rules overwrite class rules

##### Location

 * External rules overwrite default rules
 * Internal rules overwrite external rules
 * Inline rules overwrite internal rules

[Back to Table of Contents](#toc)plify and implement internal and external Cascading Style Sheets (CSS):

### selectors, classes and IDs

### CSS rules

CSS rules 

#### Single property

``` css
selector {property: value;}
```

#### Multiple properties

``` css
selector {property: value;
          property: value;}
```

### Properties

**Note:** All examples will use a HTML element as the selector but would work equally well with a class or ID.

#### Font

``` css
p {font-family: sans-serif;}

h1 {font-size: large;}
```

#### Alignment

``` css
h2 {text-align: left;}

h3 {text-align: center;}

h4 {text-align: right;}
```

#### Colour

The colour of the text and / or the background can be changed using one of the many predefined colours.  To see a list visit [W3Schools](https://www.w3schools.com/colors/colors_names.asp). 

To change the colour, the properties are:

* __text__: `color`
* __background__: `background-color`

``` css
h5 {color: DarkRed;
    background-color: Cornsilk;}
```

[Back to Table of Contents](#toc)

## JavaScript (JS) {#js}

JavaScript statements are terminated with a semicolon, **`;`**. An individual statement will probably run without a semicolon but multiple statements will not.

### Information

#### Comments

Single line comment.

``` js
// This comment is not displayed
```

Multiline comment.

``` js
/*
This comment is not displayed
This comment is not displayed
*/
```

### Mouse Over

This event is triggered when the mouse is over an element that has the `onmouseover` listener set.  It calls the associated JS function.

``` html
<p id="mouse" onmouseover="over()">Function not called</p>

<script>
    function over() {
        document.getElementById("mouse").innerHTML = "Mouse over";
        document.getElementById("mouse").style.color = "red";
    }
</script>
```

### Mouse Out

This event is triggered when the mouse is no longer over an element that has the `onmouseout` listener set.  It calls the associated JS function.

``` html
<p id="mouse" onmouseout="out()">Function not called</p>

<script>
    function out() {
        document.getElementById("mouse").innerHTML = "Mouse out";
        document.getElementById("mouse").style.color = "red";
    }
</script>
```

### This

Passing `this` as a parameter to the JS function allows the same function to be used with multiple elements.

``` html
<p onmouseover="change(this)">A paragraph.</p>
<p onmouseover="change(this)">Another paragraph.</p>

<script>
    function change(x) {
        x.style.color = "red";
        x.style.backgroundColor = "yellow";
    }
</script>
```

[Back to Table of Contents](#toc)
