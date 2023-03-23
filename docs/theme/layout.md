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

You can create a statement with centered text with the ``{centered}``
directive.

```{centered} This is centered text!
```

Dropdowns
---------

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

Rubric
------

A rubric is like an informal heading that doesn't correspond to the document's
structure.

<https://docutils.sourceforge.io/docs/ref/rst/directives.html#rubric>

```{rubric} This is a rubric
```

[Wikipedia](https://en.wikipedia.org/wiki/Rubric) says it is something different:

A rubric is a word or section of text that is traditionally written or printed
in red ink for emphasis.

This is stylized as docutils tells us to stylize it, since it is used for
footnote headers. ([More info](https://docs.python.org/3/reference/lexical_analysis.html).)

Margin
------

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

* * *

Sidebar
-------

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

Full-Width
----------

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

Grid
----

* [Jupyter Book > Grids](https://jupyterbook.org/en/stable/content/components.html?highlight=cards#grids)
* [Sphinx Design > Grids](https://sphinx-design.readthedocs.io/en/latest/grids.html)

::::{grid}

:::{grid-item}
:outline:
:columns: 3
A
:::
:::{grid-item}
:outline:
:columns: 9
B
:::
:::{grid-item}
:outline:
:columns: 6
C
:::
:::{grid-item}
:outline:
:columns: 6
D
:::

::::

Cards
-----

* [Sphinx Design > Cards](https://sphinx-design.readthedocs.io/en/latest/cards.html)

:::{card} Card Title

Card content
:::

:::{card} Card Title
Header
^^^
Card content
+++
Footer
:::

Tabs
----

* [Sphinx Design > Tabs](https://sphinx-design.readthedocs.io/en/latest/tabs.html)

::::{tab-set}

:::{tab-item} Label1
Content 1
:::

:::{tab-item} Label2
Content 2
:::

::::

````{tab-set-code}

```{code-block} ruby
puts "hello"
```

```{code-block} python
print("hello")
```

````


TODO
----

* announcement banners: https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/announcements.html
