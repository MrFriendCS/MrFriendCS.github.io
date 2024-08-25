# S2 HTML

Hypertext Markup Language (HTML) is used to create webpages.  The content is displayed on the page, and _tags_ are used to describe (_markup_) what the content is.  The content could be a heading, a paragraph, an image, etc.

A HTML element has three parts:

1. Start tag
2. Content
3. End tag

The _start_ and _end_ tags are in angle brackets `< >` and the _end_ tag also has a forward slash `/`.  An example is shown below.

``` html
<tag>Content</tag>
```

The content of an element is often other elements.  An element in an element is said to be a _child_ element.

## Basic Webpage

``` html
<!DOCTYPE HTML> 
<html lang="en-gb">
    <head>
    </head>
    
    <body>
    </body>
</html>
```

Every other HTML element goes inside the `html` element _start_ and and _end_ tags.  Information about the webpage goes in the `head` element.  Anything to be displayed goes in the `body` element.

## Head Elements

| Tag | Meaning | Comment |
| --- | ------- | ------- |
| title | Displayed on browser tab | Required on every page |

``` html
<title>My first page</title>
```

## Body Elements

### Normal

| Tag | Meaning | Comment |
| --- | ------- | ------- |
| h1 | Heading | Largest |
| h6 | Heading | Smallest |
| p | paragraph | |
| ol | Ordered list | Numbers |
| ul | Unordered list | Bullet points| 
| li | List item | used in `ol` and `ul` ||

#### h1

``` html
<h1>My first page</h1>
```

#### h2

``` html
<h2>My first page</h2>
```

#### p

``` html
<p>My first page</p>
```

#### ol

``` html
<ol>
    <li>My first page</li>
    <li>My first page</li>
</ol>
```

___Change `ol` to `ul` for an unordered list.___

### Special

This elements also include attributes in the start tag.

| Tag | Meaning | Comment |
| --- | ------- | ------- |
| a | Anchor | Hyperlinks |
| img | Add an image | No end tag<br>Must have `alt` attribute |
| audio | Add a sound file | |
| video | Add a video file | |

#### a

``` html
<a href="https://www.bbc.co.uk/">My first link</a>
```

#### img

___No end tag!___

There are two attributes.  File name, and a short description of the image.

``` html
<img src="cat.gif" alt="cat on mat">
```

#### audio

Text only displayed if there is a problem.

``` html
<audio controls src="cat.mp3">
    No audio player available
</audio>

```

#### video

Text only displayed if there is a problem.

``` html
<video controls src="cat.mp4">
    No video player available
</video>
```
