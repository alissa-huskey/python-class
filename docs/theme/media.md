Media
=====

Images
------

* [Jupyter Book > Adding Images](https://jupyterbook.org/en/stable/file-types/markdown.html#adding-images)
* [Docutils > Directives > image](https://docutils.sourceforge.io/docs/ref/rst/directives.html#image)
* [Bootstrap > Images](https://getbootstrap.com/docs/5.0/content/images/)

You can add images using standard markdown as well as the `{image}` directive .

{{ leftcol }}

An image:

```{image} https://source.unsplash.com/250x250/daily?sleeping+puppy
:height: 250
:width: 250
:align: center
```

{{ rightcol }}

A linked image:

```{image} https://source.unsplash.com/250x250/daily?flower
:target: https://unsplash.com/
:height: 250
:width: 250
:align: center
```

{{ endcols }}

{{ clear }}

{{ br }} {{ br }}

```{image} https://source.unsplash.com/200x200/daily?mountain
:align: right
:height: 200
:width: 200
```

This is a lot of text to go along with a right-aligned image, that is
helping make this content feel less linear. It is important to have such
a body of text, since the image is meant to be "floated" to the right,
which would interfere with the rest of the document otherwise.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit nihil temporibus eius sequi
animi, illo libero labore fuga.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit nihil temporibus eius sequi
animi, illo libero labore fuga.

```{image} https://source.unsplash.com/200x200/daily?fruit
:align: left
:height: 200
:width: 200
```

This is a lot of text to go along with a left-aligned image, that is
helping make this content feel less linear. It is important to have such
a body of text, since the image is meant to be "floated" to the right,
which would interfere with the rest of the document otherwise.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit nihil temporibus eius sequi
animi, illo libero labore fuga.

Lorem ipsum dolor sit amet consectetur adipisicing elit. Blanditiis
sapiente veritatis doloribus accusantium molestiae modi recusandae
excepturi facere, corrupti expedita sit nihil temporibus eius sequi
animi, illo libero labore fuga.

Figures
-------

* [Jupyter Book > Figures](https://jupyterbook.org/en/stable/content/content-blocks.html#figures)
* [Docutils > Directives > figure](https://docutils.sourceforge.io/docs/ref/rst/directives.html#figure)

```{figure} https://source.unsplash.com/400x400/daily?map
:alt: Find your way
:width: 400
:height: 400

A figure is an image with a caption and/or a legend:

| Symbol | Meaning |
|--------|---------|
| `N`    | north   |
| `S`    | south   |
| `E`    | east    |
| `W`    | west    |

This paragraph is also part of the legend.
```

Diagrams
--------

* [kroki.io](https://kroki.io/)
* [sphinx-contrib/kroki](https://github.com/sphinx-contrib/kroki/)

You can create diagrams from textual descriptions in a number of formats using
the `{kroki}` directive.

```{rubric} kroki
```

{{ leftcol }}

```{kroki} mermaid
pie title Pie Status
    "Eaten": 80
    "Left": 20
```

{{ rightcol }}

```{kroki} mermaid
flowchart TD
  should[Should I...]
  should -- stay --> trouble{Trouble}
  should -- go --> double{Double}
  style trouble fill:#f9f,stroke:#333,stroke-width:4px
  style double fill:#bbf,stroke:#f66,stroke-width:2px,color:#fff,stroke-dasharray: 5 5
```

{{ endcols }}

Math
----

* [Myst Parser > Math and equations](https://myst-parser.readthedocs.io/en/latest/syntax/math.html)
* [Jupyter Book > Math and equations](https://jupyterbook.org/en/stable/content/math.html)

Math equation blocks can be written in common LaTeX markup using the `{math}`
role or `$$` dollar math blocks.

```{rubric} math
```

:::::{grid}

:::{grid-item}

```{math}
:label: math-example-a

(a + b)^2 = a^2 + 2ab + b^2

(a + b)^2  &=  (a + b)(a + b) \\
           &=  a^2 + 2ab + b^2
```

:::

:::{grid-item}

$$
wow = its^{math}
$$(math-example-b)

:::

:::{grid-item}

```{math}
:label: math-example-c

\begin{align*}
yep = its_{more}^{math}
\end{align*}
```

:::

:::::


See Also
--------

:::{seealso}

* [Bootstrap > Figures](https://getbootstrap.com/docs/5.0/content/figures/)

:::

TODO
----

* [Jupyter Book > Adding Movies](https://jupyterbook.org/en/stable/file-types/markdown.html#adding-movies)
* [Jupyter Book > Code Outputs > Images](https://jupyterbook.org/en/stable/content/code-outputs.html#images)
* [Jupyter Book > Images and Figures](https://jupyterbook.org/en/stable/content/figures.html)
