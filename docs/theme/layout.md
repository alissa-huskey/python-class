---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
Layout
======

Centered text
-------------

* [Sphinx > rst Directives > centered](https://www.sphinx-doc.org/en/master/usage/restructuredtext/directives.html#directive-centered)

You can create a statement with centered text with the ``{centered}``
directive.

```{centered} This is centered text!
```

Full Width
----------

* [Jupyter Book > Full-width content](https://jupyterbook.org/en/stable/content/layout.html#full-width-content)

Full-width content extends into the right margin, making it stand out against
the rest of your book’s content. To add full-width content to your page, add
the class `.full-width` to any of the elements in your documentation.

```{note}
:class: full-width
This content will be full-width
```

### Code cells

You can also trigger this behavior with a code cell by adding a full-width tag
to the cell.

```{code-cell} python
:tags: ["full-width"]
print("This is a test.")
```

Margin
------

* [Jupyter Book > Margin Content](https://jupyterbook.org/en/stable/content/layout.html#margin-content)

:::{margin} Ch'ien / The Creative
Lorem ipsum dolor sit amet consectetur adipisicing elit.

```{image} https://source.unsplash.com/200x200/daily?wildlife
```

Lorem ipsum dolor sit amet consectetur adipisicing elit.
:::

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

{{ clear }}

### Figures

You can configure figures to use the margin for captions. Here is a figure with
a caption to the right.

```{figure} https://source.unsplash.com/400x600/daily?dress
---
figclass: margin-caption
alt: My figure text
name: myfig5
align: right
---
**Dress** And here is my figure caption, but you probably already noticed that.
Really I am just taking up space to see how the margin caption looks like when
it is really long :-).
```

{{ clear }}

```{figure} https://source.unsplash.com/200x200/daily?window
---
figclass: margin
alt: My figure text
name: myfig4
---
And here is my figure caption
```

Or you can put the whole figure in the margin.

{{ clear }}

### .margin

:::{note}
:class: margin
This note will be in the margin!
:::

You can add the `.margin` class to any element to put it in the margin.

{{ clear }}

* * *

Sidebar
-------

* [Jupyter Book > Sidebar Content](https://jupyterbook.org/en/stable/content/layout.html#sidebar-content)

:::{sidebar} Ch'ien / The Creative
Lorem ipsum dolor sit amet consectetur adipisicing elit.

```{image} https://source.unsplash.com/200x200/daily?forest
```

Lorem [^lorem] ipsum [^ipsum] dolor sit amet consectetur adipisicing elit.

[^lorem]: footnote target
[^ipsum]: footnote target two

:::

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

{{ clear }}

### With Code

```{sidebar} A code example

With a sidebar on the right.
```

```{code-block} python
:caption: Code blocks can also have captions.
:linenos:

print("one")
print("two")
print("three")
print("four")
print("five")
print("six")
print("seven")
print("eight")
print("nine")
print("ten")
print("eleven")
print("twelve")
print("thirteen")
print("fourteen")
```

{{ clear }}

### With Rubric

`````{sidebar} Sidebar Title
:subtitle: Optional Subtitle

This is a sidebar.  It is for text outside the flow of the main
text.

```{rubric} This is a rubric inside a sidebar
```

Sidebars often appears beside the main text with a border and
background color.
`````

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt
voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic
voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

{{ clear }}

### .sidebar

:::{note}
:class: sidebar
This note will be in the sidebar
:::

You can add the `.sidebar` class to any element to put it in the sidebar.

{{ clear }}

* * *

Grid
----

* [Sphinx Design > Grids](https://sphinx-design.readthedocs.io/en/latest/grids.html)
* [Jupyter Book > Grids](https://jupyterbook.org/en/stable/content/components.html#grids)
* [Bootstrap > Layout > Grid System](https://getbootstrap.com/docs/5.0/layout/grid/)
* [Bootstrap > Layout > Columns](https://getbootstrap.com/docs/5.0/layout/columns/)
* [Bootstrap > Layout > Gutters](https://getbootstrap.com/docs/5.0/layout/gutters/)

:::{hlist}
:columns: 3

* [Jupyter Book > Grids](https://jupyterbook.org/en/stable/content/components.html?highlight=cards#grids)
* [Sphinx Design > Grids](https://sphinx-design.readthedocs.io/en/latest/grids.html)
* [Bootstrap > CSS Grid](https://getbootstrap.com/docs/5.3/layout/css-grid/)

:::

Grids allow you to structure arbitrary chunks of content in a grid-like system.
You can also control things like the width of columns, the "gutters" between
columns, etc.

::::{grid}
:gutter: 2

:::{grid-item-card}
:columns: 3
:padding: 2
A
:::

:::{grid-item-card}
:columns: 9
:padding: 2
B
:::

:::{grid-item-card}
:columns: 6
:padding: 2
C
:::

:::{grid-item-card}
:columns: 6
:padding: 2
D
:::

::::

Cards
-----

:::{hlist}
:columns: 2

* [Jupyter Book > Cards](https://jupyterbook.org/en/stable/content/components.html?highlight=cards#cards)
* [Jupyter Book > Grid Cards](https://jupyterbook.org/en/stable/content/components.html?highlight=cards#create-grids-of-cards)
* [Sphinx Design > Cards](https://sphinx-design.readthedocs.io/en/latest/cards.html)
* [Bootstrap > Cards](https://getbootstrap.com/docs/5.0/components/card/)

:::

Cards provide an easy way for you to put content into a standard "header",
"body", "footer" structure that has a similar alignment and visual style.

:::{card}
:margin: auto
:width: 25%

Basic Card

:::

{{ br }}
{{ br }}

### Card Options

Here's how the various card options look that effect rendering arranged using
[grid cards][].

[grid cards]: https://jupyterbook.org/en/stable/content/components.html?highlight=cards#create-grids-of-cards

:::::{grid} 2
:gutter: 3

:::{grid-item-card} Title {span}`Subtitle <text-muted>`
Header
^^^
Content
+++
Footer
:::

:::{grid-item-card}
:shadow: lg

Shadow

:::

:::{grid-item-card}
:link: http://example.com

<h4 class="card-header">Styled Header</h4>

Plus some content.

:::

:::{grid-item-card} Styled Title
:class-title: card-title

With some content.

:::

:::{grid-item-card}
:link: http://example.com

Clickable Link

:::

:::{grid-item-card}
:img-top: https://source.unsplash.com/300x50/daily?banner+pattern+warm+background

Image Top

:::

:::{grid-item-card}
:img-bottom: https://source.unsplash.com/300x50/daily?banner+pattern+cool+background

Image Bottom

:::

:::{grid-item-card}
:img-background: https://source.unsplash.com/300x200/daily?banner+pattern+dark+background

Image Background

:::

:::{grid-item-card} Left Aligned
:text-align: left
:columns: 4
:::

:::{grid-item-card} Center Aligned
:text-align: center
:columns: 4
:::

:::{grid-item-card} Right Aligned
:text-align: right
:columns: 4
:::

:::{grid-item-card} Primary
:class-card: bg-primary
:columns: 3
:::

:::{grid-item-card} Secondary
:class-card: bg-secondary
:columns: 3
:::

:::{grid-item-card} Success
:class-card: bg-success
:columns: 3
:::

:::{grid-item-card} Info
:class-card: bg-info text-dark
:columns: 3
:::

:::{grid-item-card} Warning
:class-card: bg-warning text-dark
:columns: 3
:::

:::{grid-item-card} Danger
:class-card: bg-danger
:columns: 3
:::

:::{grid-item-card} Light
:class-card: bg-light text-dark
:columns: 3
:::

:::{grid-item-card} Dark
:class-card: bg-dark
:columns: 3
:::

:::::

### Card Carousel

::::{card-carousel} 3

:::{card} A
:margin: 2
:::

:::{card} B
:margin: 2
:::

:::{card} C
:margin: 2
:::

:::{card} D
:margin: 2
Surprise!

Content!
:::

:::{card} E
:margin: 2
:::

:::{card} F
:margin: 2
:::

::::


Tabs
----

* [Jupyter Book > Tab Content](https://jupyterbook.org/en/stable/content/content-blocks.html#epigraphs)
* [Sphinx Design > Tabs](https://sphinx-design.readthedocs.io/en/latest/tabs.html)

{{ leftcol }}

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::

{{ rightcol }}

````{tab-set-code}

```{code-block} ruby
puts "hello"
```

```{code-block} python
print("hello")
```

````

{{ endcols }}

Dropdowns
---------

* [Jupyter Book > Components and UI Elements > The {dropdown} directive](https://jupyterbook.org/en/stable/content/components.html?highlight=dropdown#the-dropdown-directive)
* [Sphinx Design > Dropdowns](https://sphinx-design.readthedocs.io/en/latest/dropdowns.html)
* [Bootstrap > Components > Dropdown](https://getbootstrap.com/docs/5.0/components/dropdowns/)
* [Bootstrap > Layout > Breakpoints](https://getbootstrap.com/docs/5.0/layout/breakpoints/)
* [Bootstrap > Layout > Containers](https://getbootstrap.com/docs/5.0/layout/containers/)

This is an example of a dropdown.

{{ left }}

`````{dropdown} Need help?

1. `[ ]` Find where you assign `PLAYER_STATE`, `DEBUG_STATE`, etc. Just under
         that set `adventure.DELAY` to `0`
1. `[ ]` Run your tests. They should pass and be as fast as usual.

`````

{{ right }}

`````{dropdown} Code

```{literalinclude} ../../pythonclass/adventure/test_game-14.8.py
:linenos:
:lineno-match:
:pyobject: setup_module
:emphasize-lines: "9"
:caption: test_game.py

```

`````

{{ endcols }}

See Also
--------

:::{seealso}

* [Bootstrap > Display Utilities](https://getbootstrap.com/docs/5.0/utilities/display/)
* [Bootstrap > Flex Utilities](https://getbootstrap.com/docs/5.0/utilities/flex/)
* [Bootstrap > Float Utilities](https://getbootstrap.com/docs/5.0/utilities/float/)
* [Bootstrap > Overflow Utilities](https://getbootstrap.com/docs/5.0/utilities/overflow/)
* [Bootstrap > Position Utilities](https://getbootstrap.com/docs/5.0/utilities/position/)
* [Bootstrap > Sizing Utilities](https://getbootstrap.com/docs/5.0/utilities/sizing/)
* [Bootstrap > Spacing Utilities](https://getbootstrap.com/docs/5.0/utilities/spacing/)
* [Bootstrap > Vertical Alignment Utilities](https://getbootstrap.com/docs/5.0/utilities/vertical-align/)
* [Bootstrap > Visibility Utilities](https://getbootstrap.com/docs/5.0/utilities/visibility/)
* [Bootstrap > Components > Carosel](https://getbootstrap.com/docs/5.0/components/carousel/)
* [Bootstrap > Layout > Z-index](https://getbootstrap.com/docs/5.0/layout/z-index/)
* [Bootstrap > Helpers > Clearfix](https://getbootstrap.com/docs/5.0/helpers/clearfix/)
* [Bootstrap > Helpers > Ratios](https://getbootstrap.com/docs/5.0/helpers/ratio/)
* [Bootstrap > Helpers > Position](https://getbootstrap.com/docs/5.0/helpers/position/)
* [Bootstrap > Helpers > Visually Hidden](https://getbootstrap.com/docs/5.0/helpers/visually-hidden/)

:::

TODO
----

* [Jupyter Book > The {toggle} directive](https://jupyterbook.org/en/stable/interactive/hiding.html#the-toggle-directive)
