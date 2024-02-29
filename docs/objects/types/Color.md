---
title: Color
description: Color is a data type that represents a color.
icon: polytoria/Color
---

# Color

:polytoria-Color: Color is a data type that represents a color.

## Notes

The alpha property is between 0 and 255. 0 is fully transparent and 255 is fully visible.

## Constructors

| Name                                                      | Description                                                                |
| --------------------------------------------------------- | -------------------------------------------------------------------------- |
| Color.New()                                               | Creates a new black color.                                                 |
| Color.New(`number` n)                                     | Creates a new Color with an R, G and B value of n.                         |
| Color.New(`number` r, `number` g, `number` b)             | Creates a new Color with the set R, G and B values and an alpha value of 1 |
| Color.New(`number` r, `number` g, `number` b, `number` a) | Creates a new Color with the set R, G, B and A values                      |
| Color.FromHex(`string` HEX)                               | Creates a new Color from the specified hex value.                          |
| Color.Random()                                            | Returns a random color with an alpha value of 1.                           |

## Properties

| Name       | Description                     |
| ---------- | ------------------------------- |
| `number` r | Red color component             |
| `number` g | Green color component           |
| `number` b | Blue color component            |
| `number` a | Alpha (opacity) color component |

## Functions

| Name                                          | Description                                |
| --------------------------------------------- | ------------------------------------------ |
| Color.Lerp(`Color` a, `Color`, b, `number` t) | Linearly interpolates colors a and b by t. |
