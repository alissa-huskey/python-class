Typography
==========

This is quite important, for a website where the majority of the content is going to be prose.

Notice the font family being used for the prose, as well as the font family being used for the heading. Think about the spacing between the lines, as well as the spacing between various paragraphs. Also keep the font weight in mind, and consider if/how you want antialiasing and font-smoothing to work.

Multiple paragraphs are a common occurance, because you often need more than a single paragraph to describe a thing. The rest of this paragraph is gonna be the famous lorem-ipsum: Lorem ipsum **dolor** sit amet consectetur adipisicing elit. Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

```{list-table}
:header-rows: 1

* - Variable
  - Example
* - `--pst-font-size-base`
  - <p>base font size</p>
* - `--pst-font-size-h1`
  - <h1>h1. Heading</h1>
* - `--pst-font-size-h2`
  - <h2>h2. Heading</h2>
* - `--pst-font-size-h3`
  - <h3>h3. Heading</h3>
* - `--pst-font-size-h4`
  - <h4>h4. Heading</h4>
* - `--pst-font-size-h5`
  - <h5>h5. Heading</h5>
* - `--pst-font-size-h6`
  - <h6>h6. Heading</h6>
* - `--pst-font-size-milli`
  - <small>smaller than heading</small>
* - `--pst-sidebar-font-size`
  - sidebar font size
* - `--pst-sidebar-font-size-mobile`
  - sidebar font size on mobile
* - `--pst-sidebar-header-font-size`
  - sidebar header font size
* - `--pst-sidebar-header-font-weight`
  - sidebar header font weight
* - `--pst-admonition-font-weight-heading`
  - admonition heading font weight
* - `--pst-font-weight-caption`
  - caption font weight
* - `--pst-font-weight-heading`
  - heading font weight
* - `--pst-font-family-base`
  - base font family
* - `--pst-font-family-heading`
  - heading font family
* - `--pst-font-family-base-system`
  - base-system font family
* - `--pst-font-family-monospace-system`
  - monospace-system font family
* - `--pst-font-family-monospace`
  - monospace font family

```


Headings
--------

```
  // base font size - applied at body/html level
  --pst-font-size-base: 1rem;

  // heading font sizes based on bootstrap sizing
  --pst-font-size-h1: 2.5rem;
  --pst-font-size-h2: 2rem;
  --pst-font-size-h3: 1.75rem;
  --pst-font-size-h4: 1.5rem;
  --pst-font-size-h5: 1.25rem;
  --pst-font-size-h6: 1.1rem;

  // smaller than heading font sizes
  --pst-font-size-milli: 0.9rem;

  // Sidebar styles
  --pst-sidebar-font-size: 0.9rem;
  --pst-sidebar-font-size-mobile: 1.1rem;
  --pst-sidebar-header-font-size: 1.2rem;
  --pst-sidebar-header-font-weight: 600;

  // Admonition styles
  --pst-admonition-font-weight-heading: 600;

  // Font weights
  --pst-font-weight-caption: 300;
  --pst-font-weight-heading: 400;

  // Font family
  // These are adapted from https://systemfontstack.com/ */
  --pst-font-family-base-system: -apple-system, BlinkMacSystemFont, Segoe UI,
    "Helvetica Neue", Arial, sans-serif, Apple Color Emoji, Segoe UI Emoji,
    Segoe UI Symbol;
  --pst-font-family-monospace-system: "SFMono-Regular", Menlo, Consolas, Monaco,
    Liberation Mono, Lucida Console, monospace;

  --pst-font-family-base: var(--pst-font-family-base-system);
  --pst-font-family-heading: var(--pst-font-family-base-system);
  --pst-font-family-monospace: var(--pst-font-family-monospace-system);
```

This next bit will explore how the various headings look. Think about how the content separation should work, and how the various headings should interact with the main content.

### Heading 3

#### Heading 4

##### Heading 5

###### Heading 6


Heading 2 with content
----------------------

Lorem ipsum **dolor** sit amet consectetur adipisicing elit.

Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

### Heading 3 with content

Lorem ipsum **dolor** sit amet consectetur adipisicing elit.

Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

#### Heading 4 with content

Lorem ipsum **dolor** sit amet consectetur adipisicing elit.

Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

##### Heading 5 with content

Lorem ipsum **dolor** sit amet consectetur adipisicing elit.

Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.

###### Heading 6 with content

Lorem ipsum **dolor** sit amet consectetur adipisicing elit.

Accusamus, sunt voluptatum tenetur libero nulla esse veritatis accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam.
