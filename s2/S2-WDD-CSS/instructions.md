# S2 WDD - CSS

## Introduction

Cascading Style Sheets (CSS) are used to format webpages.  The content is displayed on the page, and _tags_ are used to describe (_markup_) what the content is.  The content could be a heading, a paragraph, an image, etc.

CSS is used to change how the content is fomatted.

## Task

All the content that is needed has been added to the webpage, but it still needs to be formatted.

Using only CSS, format the webpage.

## CSS Rules

A CSS rule has three parts:

1. Selector
2. Property
3. Value

The _property_ and _value_ are in curly brackets `{ }`, with the _property_ followed by a colon `:`, and the and _value_  followed by a semi-colon `;`.  An example is shown below.

``` css
selector {property: value;}
```

More than one _property_ of a _selector_ can be changed, see below.

``` css
selector {property: value;
          property: value;}
```

## CSS Examples

### Single property

``` css
h1 {color: red;}
```

### Multiple properties

``` css
p {color: blue;
   font-family: sans-serif;}
```

## Style Element

CSS rules are declared in the `head` of a webpage using the `style` tag.

``` html
<!DOCTYPE HTML> 
<html>
    <head>
        <style>
            /* CSS rules go here */

        </style>
    </head>

    <body>
    </body>
</html>
```

## CSS Proprties and Values

CSS uses ___American___ spelling.

| Property | Example Values | Comment |
| -------- | ----- | ------- |
| color | red, green, blue | Text colour: [more](https://www.w3schools.com/colors/colors_names.asp) |
| background-color | red, green, blue | Background colour: [more](https://www.w3schools.com/colors/colors_names.asp) |
| text-align | left, center, right, justify | |
| font-family | sans-serif, monospaced | [More](https://www.w3schools.com/css/css_font.asp) |
| font-size | x-small, large, xx-large | [More](https://www.w3schools.com/cssref/pr_font_font-size.php) |
| width | 320px, 15% | [More](https://www.w3schools.com/cssref/pr_dim_width.php) | 
| height | 240px, 15% | [More](https://www.w3schools.com/cssref/pr_dim_height.php) |
