Typography
==========

Font Styles
-----------

* [Bootstrap > Native Font Stack](https://getbootstrap.com/docs/5.0/content/reboot/#native-font-stack)

:::::{grid} 2

:::{grid-item}

```{rubric} Base
```

Fairy tales are more than true: not because they tell us that dragons exist,
but because they tell us that dragons can be beaten.

― Neil Gaiman, Coraline

:::

:::{grid-item}

```{rubric} Monospace
```

    He who is brave is free.

    --Seneca

:::

:::::

Text Elements
-------------

### Lead

* [Bootstrap > Typography > Lead](https://getbootstrap.com/docs/5.0/content/typography/#lead)

```{rst-class} lead
```

It does not do to dwell on dreams and forget to live.

### Rubric

* [Docutils > Directives > rubric](https://docutils.sourceforge.io/docs/ref/rst/directives.html#rubric)

:::::{grid} 2

:::{grid-item}

* [reStructuredText Directives > Rubric](https://docutils.sourceforge.io/docs/ref/rst/directives.html#rubric)

A rubric is like an informal heading that doesn't correspond to the document's
structure.

:::

:::{grid-item}

```{rubric} This is a rubric
```

[Wikipedia](https://en.wikipedia.org/wiki/Rubric) describes a rubric as:

A rubric is a word or section of text that is traditionally written or printed
in red ink for emphasis.

:::

:::::


Headings
--------

* [Bootstrap > Typography > Headings](https://getbootstrap.com/docs/5.0/content/typography/#headings)
* [Bootstrap > Reboot > Headings and Paragraphs](https://getbootstrap.com/docs/5.0/content/reboot/#headings-and-paragraphs)

Here's to the crazy ones. The misfits. The rebels. The troublemakers. The round
pegs in the square holes. The ones who see things differently. They're not fond
of rules. And they have no respect for the status quo. You can quote them,
disagree with them, glorify or vilify them. About the only thing you can't do
is ignore them. Because they change things. They push the human race forward.
And while some may see them as the crazy ones, we see genius. Because the
people who are crazy enough to think they can change the world, are the ones
who do.

― Rob Siltanen

### Heading 3

Sleep is good, he said, and books are better.

― George R. R. Martin

#### Heading 4

Two things are infinite: the universe and human stupidity; and I'm not sure
about the universe.

― Albert Einstein

##### Heading 5

You've gotta dance like there's nobody watching, \
Love like you'll never be hurt, \
Sing like there's nobody listening, \
And live like it's heaven on earth.

― William W. Purkey

###### Heading 6

You only live once, but if you do it right, once is enough.

― Mae West

<h3>
  Fancy Heading
  <small class="text-muted">With secondary text</small>
</h3>

Note that these headings will not appear in the table of contents.

<h3>Heading <span class="badge bg-info">With Badge</span></h3>

Display Headings
----------------

* [Bootstrap > Text Utilities > Display Headings](https://getbootstrap.com/docs/5.0/content/typography/#display-headings)

<h1 class="display-1">Display 1</h1>
<h2 class="display-2">Display 2</h2>
<h3 class="display-3">Display 3</h3>
<h4 class="display-4">Display 4</h4>
<h5 class="display-5">Display 5</h5>
<h6 class="display-6">Display 6</h6>


Variables
---------

```{rst-class} variables
```

| Variable                               | Value           | Demo                                              |
|----------------------------------------|-----------------|---------------------------------------------------|
| `--pst-font-size-base`                 | {span}`<value>` | {span}`demo <pst-font-size-base>`                 |
| `--pst-font-size-h1`                   | {span}`<value>` | <h1>demo</h1>                                     |
| `--pst-font-size-h2`                   | {span}`<value>` | <h2>demo</h2>                                     |
| `--pst-font-size-h3`                   | {span}`<value>` | <h3>demo</h3>                                     |
| `--pst-font-size-h4`                   | {span}`<value>` | <h4>demo</h4>                                     |
| `--pst-font-size-h5`                   | {span}`<value>` | <h5>demo</h5>                                     |
| `--pst-font-size-h6`                   | {span}`<value>` | <h6>demo</h6>                                     |
| `--pst-font-size-milli`                | {span}`<value>` | {span}`demo <pst-font-size-milli>`                |
| `--pst-sidebar-font-size`              | {span}`<value>` | {span}`demo <pst-sidebar-font-size-milli>`        |
| `--pst-sidebar-font-size-mobile`       | {span}`<value>` | {span}`demo <pst-font-size-mobile>`               |
| `--pst-sidebar-header-font-size`       | {span}`<value>` | {span}`demo <pst-sidebar-header-font-size>`       |
| `--pst-sidebar-header-font-weight`     | {span}`<value>` | {span}`demo <pst-sidebar-header-font-weight>`     |
| `--pst-admonition-font-weight-heading` | {span}`<value>` | {span}`demo <pst-admonition-font-weight-heading>` |
| `--pst-font-weight-caption`            | {span}`<value>` | {span}`demo <pst-font-weight-heading>`            |
| `--pst-font-weight-heading`            | {span}`<value>` | {span}`demo <pst-font-family-base>`               |
| `--pst-font-family-base`               | {span}`<value>` | {span}`demo <pst-font-family-monospace>`          |
| `--pst-font-family-heading`            | {span}`<value>` | {span}`demo <pst-font-family-heading>`            |
| `--pst-font-family-base-system`        | {span}`<value>` | {span}`demo <pst-font-family-base-system>`        |
| `--pst-font-family-monospace-system`   | {span}`<value>` | {span}`demo <pst-font-family-monospace-system>`   |
| `--pst-font-family-monospace`          | {span}`<value>` | {span}`demo <pst-font-family-monospace>`          |
| `--pst-sidebar-secondary`              | {span}`<value>` |                                                   |

<!-- | `--pst-header-height`                  | {span}`<value>` |                                                   | -->
<!-- | `--pst-header-article-height`          | {span}`<value>` |                                                   | -->
<!-- |                                        |                 |                                                   | -->

See Also
--------

:::{seealso}

* [announcement banners](https://pydata-sphinx-theme.readthedocs.io/en/latest/user_guide/announcements.html)
* [bootstrap text utilities](https://getbootstrap.com/docs/5.0/utilities/text/#text-decoration)
* [Bootstrap > Typography](https://getbootstrap.com/docs/5.0/content/typography/)
* [Bootstrap > Helpers > Text truncation](https://getbootstrap.com/docs/5.0/helpers/text-truncation/)

:::
