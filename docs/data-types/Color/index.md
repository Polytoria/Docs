# Color

### Description

Color is a data type that represents a color.

### Constructors

| Color.New()               |
| ------------------------- |
| Creates a new black Color |

| Color.New(`number` n)                             |
| ------------------------------------------------- |
| Creates a new Color with an R, G and B value of n |

| Color.New(`number` r, `number` g, `number` b)                              |
| -------------------------------------------------------------------------- |
| Creates a new Color with the set R, G and B values and an alpha value of 1 |

| Color.New(`number` r, `number` g, `number` b, `number` a) |
| --------------------------------------------------------- |
| Creates a new Color with the set R, G, B and A values     |

| Color.FromHex(`string` hex)                       |
| ------------------------------------------------- |
| Creates a new Color from the specified hex value. |

| Color.Random()                                   |
| ------------------------------------------------ |
| Returns a random color with an alpha value of 1. |

### Properties

| `number` r                     |
| ------------------------------ |
| The red component of the color |

| `number` g                       |
| -------------------------------- |
| The green component of the color |

| `number` b                      |
| ------------------------------- |
| The blue component of the color |

| `number` a                                 |
| ------------------------------------------ |
| The alpha (opacity) component of the color |

### Functions

| `Color` Color.Lerp(`Color` a, `Color` b, `number` t) |
| ---------------------------------------------------- |
| Linearly interpolates colors a and b by t.           |
