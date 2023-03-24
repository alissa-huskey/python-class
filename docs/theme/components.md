Components
==========

* [Sphinx Design > Badges, Buttons & Icons](https://sphinx-design.readthedocs.io/en/latest/badges_buttons.html)

Badges
------

|                            |                                      |
|----------------------------|--------------------------------------|
| {bdg-primary}`primary`     | {bdg-primary-line}`primary-line`     |
| {bdg-secondary}`secondary` | {bdg-secondary-line}`secondary-line` |
| {bdg-success}`success`     | {bdg-success-line}`success-line`     |
| {bdg-info}`info`           | {bdg-info-line}`info-line`           |
| {bdg-warning}`warning`     | {bdg-warning-line}`warning-line`     |
| {bdg-danger}`danger`       | {bdg-danger-line}`danger-line`       |
| {bdg-light}`light`         | {bdg-light-line}`light-line`         |
| {bdg-dark}`dark`           | {bdg-dark-line}`dark-line`           |
|                            |                                      |


Buttons
-------

:::::{grid} 2

:::{grid-item}

```{button-link} https://example.com
:color: success
Success
```

:::

:::{grid-item}

```{button-link} https://example.com
:color: info
:outline:
Info Outline
```
:::

:::{grid-item}

```{button-link} https://example.com
:color: warning
:shadow:
Warning Shadow
```
:::

:::{grid-item}

```{button-link} https://example.com
:outline:
:color: danger
Danger Outline Shadow
```

:::

:::{grid-item}

```{button-link} https://example.com
:color: primary
:ref-type: myst
**Primary Bold**
```
:::

:::{grid-item}

```{button-link} https://example.com
:color: secondary
:align: right
Secondary Right Align
```
:::

:::{grid-item}
:columns: 12

```{button-link} https://example.com
:color: light
:expand:
Light Expanded
```
:::

:::::

Icons
-----

* [Octicons](https://primer.style/octicons/) -- github's icons

### Octicon

:::{hlist}
:columns: 3

- {octicon}`comment` Basic
- {octicon}`bell;3em` Resized
- {octicon}`bell-fill;3em` Filled
- {octicon}`bookmark;3em;sd-text-info` Info
- {octicon}`beaker;3em;sd-text-success` Success
- {octicon}`report;3em;sd-text-warning` Warning
- {octicon}`blocked;3em;sd-text-danger` Danger
- {octicon}`home;3em;sd-text-primary` Primary
- {octicon}`key;3em;sd-text-secondary` Secondary
- {octicon}`sun;3em;sd-text-light` Light
- {octicon}`moon;3em;sd-text-dark` Dark

:::

### Material

* [Material Symbols](https://fonts.google.com/icons)

:::{list-table}
:header-rows: 1

* - &nbsp;
  - Regular
  - Outlined
  - Round
  - Sharp
  - Two Tone

* - Basic
  - {material-regular}`star`
  - {material-outlined}`star`
  - {material-round}`star`
  - {material-sharp}`star`
  - {material-twotone}`star`

* - Resized
  - {material-regular}`settings;3em`
  - {material-outlined}`settings;3em`
  - {material-round}`settings;3em`
  - {material-sharp}`settings;3em`
  - {material-twotone}`settings;3em`

* - Info
  - {material-regular}`check_circle;3em;sd-text-info`
  - {material-outlined}`check_circle;3em;sd-text-info`
  - {material-round}`check_circle;3em;sd-text-info`
  - {material-sharp}`check_circle;3em;sd-text-info`
  - {material-twotone}`check_circle;3em;sd-text-info`

* - Success
  - {material-regular}`home;3em;sd-text-success`
  - {material-outlined}`home;3em;sd-text-success`
  - {material-round}`home;3em;sd-text-success`
  - {material-sharp}`home;3em;sd-text-success`
  - {material-twotone}`home;3em;sd-text-success`

* - Warning
  - {material-regular}`favorite;3em;sd-text-warning`
  - {material-outlined}`favorite;3em;sd-text-warning`
  - {material-round}`favorite;3em;sd-text-warning`
  - {material-sharp}`favorite;3em;sd-text-warning`
  - {material-twotone}`favorite;3em;sd-text-warning`

* - Danger
  - {material-regular}`disabled_by_default;3em;sd-text-danger`
  - {material-outlined}`disabled_by_default;3em;sd-text-danger`
  - {material-round}`disabled_by_default;3em;sd-text-danger`
  - {material-sharp}`disabled_by_default;3em;sd-text-danger`
  - {material-twotone}`disabled_by_default;3em;sd-text-danger`

* - Primary
  - {material-regular}`dataset;3em;sd-text-primary`
  - {material-outlined}`dataset;3em;sd-text-primary`
  - {material-round}`dataset;3em;sd-text-primary`
  - {material-sharp}`dataset;3em;sd-text-primary`
  - {material-twotone}`dataset;3em;sd-text-primary`

* - Secondary
  - {material-regular}`thumb_up;3em;sd-text-secondary`
  - {material-outlined}`thumb_up;3em;sd-text-secondary`
  - {material-round}`thumb_up;3em;sd-text-secondary`
  - {material-sharp}`thumb_up;3em;sd-text-secondary`
  - {material-twotone}`thumb_up;3em;sd-text-secondary`

* - Light
  - {material-regular}`rocket_launch;3em;sd-text-light`
  - {material-outlined}`rocket_launch;3em;sd-text-light`
  - {material-round}`rocket_launch;3em;sd-text-light`
  - {material-sharp}`rocket_launch;3em;sd-text-light`
  - {material-twotone}`rocket_launch;3em;sd-text-light`

* - Dark
  - {material-regular}`mood;3em;sd-text-dark`
  - {material-outlined}`mood;3em;sd-text-dark`
  - {material-round}`mood;3em;sd-text-dark`
  - {material-sharp}`mood;3em;sd-text-dark`
  - {material-twotone}`mood;3em;sd-text-dark`

:::

### Font Awesome

* [Font Awesome > Icons](https://fontawesome.com/icons)

:::{list-table}
:header-rows: 1

* - &nbsp;
  - Solid
  - Outline
  - Sharp
  - Animated

* - Basic
  - {fas}`face-smile`
  - {far}`face-smile`
  - {fas}`face-smile;fa-sharp`
  - {fas}`face-smile;fa-spin`

* - Resized
  - {fas}`heart;fs-1`
  - {far}`heart;fs-1`
  - {fas}`heart;fs-1 fa-sharp`
  - {fas}`heart;fs-1 fa-spin-reverse`

* - Info
  - {fas}`star;fs-1 pst-color-info`
  - {far}`star;fs-1 pst-color-info`
  - {fas}`star;fs-1 pst-color-info fa-sharp`
  - {fas}`star;fs-1 pst-color-info fa-bounce`

* - Muted
  - {fas}`comment;fs-1 pst-color-muted`
  - {far}`comment;fs-1 pst-color-muted`
  - {fas}`comment;fs-1 pst-color-muted fa-sharp`
  - {fas}`comment;fs-1 pst-color-muted fa-shake`

* - Success
  - {fas}`vials;fs-1 pst-color-success`
  - {far}`vials;fs-1 pst-color-success`
  - {fas}`vials;fs-1 pst-color-success fa-sharp`
  - {fas}`vials;fs-1 pst-color-success fa-spin-pulse`

* - Warning
  - {fas}`fire;fs-1 pst-color-warning`
  - {far}`fire;fs-1 pst-color-warning`
  - {fas}`fire;fs-1 pst-color-warning fa-sharp`
  - {fas}`fire;fs-1 pst-color-warning fa-beat-fade`

* - Danger
  - {fas}`skull;fs-1 pst-color-danger`
  - {far}`skull;fs-1 pst-color-danger`
  - {fas}`skull;fs-1 pst-color-danger fa-sharp`
  - {fas}`skull;fs-1 pst-color-danger fa-spin`

* - Light
  - {fas}`sun;fs-1 pst-color-light`
  - {far}`sun;fs-1 pst-color-light`
  - {fas}`sun;fs-1 pst-color-light fa-sharp`
  - {fas}`sun;fs-1 pst-color-light fa-spin-reverse`

* - Dark
  - {fas}`moon;fs-1 pst-color-dark`
  - {far}`moon;fs-1 pst-color-dark`
  - {fas}`moon;fs-1 pst-color-dark fa-sharp`
  - {fas}`moon;fs-1 pst-color-dark fa-spin-pulse`

* - Brands
  - {fab}`github;fs-1 fa-solid`
  - {fab}`github;fs-1`
  - {fas}`github;fs-1 fa-sharp`
  - {fas}`github;fs-1 fa-beat fa-beat`


:::
