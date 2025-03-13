# S2 WDD - HTML

Hypertext Markup Language (HTML) is used to create webpages.  The content is displayed on the page, and _tags_ are used to describe (_markup_) what the content is.  The content could be a heading, a paragraph, an image, etc.

A HTML element has three parts:

1. Start tag
2. Content
3. End tag

The _start_ and _end_ tags are in angle brackets `< >` and the _end_ tag also has a forward slash `/`.  An example is shown below.

``` html
<exampleTag>Content to be displayed</exampleTag>
```

The content of an element is often other elements.  An element in an element is said to be a _child_ element.


## Basic Webpage

``` html
<!DOCTYPE html> 
<html lang="en-gb">
    <head>
        <!-- Head elements go below this comment -->


    </head>
    
    <body>
        <!-- Body elements go below this comment -->


    </body>
</html>
```

Every other HTML element goes inside the `html` element _start_ and and _end_ tags.  Information about the webpage goes in the `head` element.  Anything to be displayed goes in the `body` element.


## Head Elements

| Tag   | Meaning                  | Comment |
| ---   | -------                  | ------- |
| title | Displayed on browser tab | Required on every page |

``` html
<title>My first page</title>
```


## Body Elements

### Normal

| Tag | Meaning        | Comment |
| --- | -------        | ------- |
| h1  | Heading        | Largest |
| h6  | Heading        | Smallest |
| p   | paragraph      | |
| ol  | Ordered list   | Numbers |
| ul  | Unordered list | Bullet points| 
| li  | List item      | used in `ol` and `ul` |

#### h1

``` html
<h1>My first page</h1>
```

#### h2

``` html
<h2>A Subheading</h2>
```

#### p

``` html
<p>A paragrapgh of text.</p>
```

#### ol

``` html
<ol>
    <li>A list item</li>
    <li>Another item</li>
</ol>
```

Change `ol` to `ul` for an unordered list.

### Special

This elements also include attributes in the start tag.

| Tag   | Meaning          | Comment |
| ---   | -------          | ------- |
| a     | Anchor           | Hyperlinks |
| img   | Add an image     | No end tag<br>Must have `alt` attribute |
| audio | Add a sound file | |
| video | Add a video file | |

#### a

``` html
<a href="https://www.bbc.co.uk/">My first link</a>
```

#### img

___No end tag!___

There are two attributes.  The file name, and a short description of the image.
The image file is in the same folder as the webpage file.

``` html
<img src="cat.gif" alt="Cat sat on a mat.">
```

#### audio

Text only displayed if there is a problem.
The audio file is in the same folder as the webpage file.

``` html
<audio controls src="cat.mp3">
    No audio player available
</audio>

```

#### video

Text only displayed if there is a problem.
The video file is in the same folder as the webpage file.

``` html
<video controls src="cat.mp4">
    No video player available
</video>
```


## Media Files

Use the links below to download the required media files.

* Image: [Cat image](assets/cat.gif)
* Audio: [Cat sound](assets/cat.mp3)
* Video: [Cat video](assets/cat.mp4)
