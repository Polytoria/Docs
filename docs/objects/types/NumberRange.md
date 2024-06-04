---
title: NumberRange
description: NumberRange is a data type that represents a number range.
icon: polytoria/Unknown
---

# ColorRange

:polytoria-Unknown: NumberRange is a data type that represents a number range.

## Constructors

| Name                                      | Description                                                |
| ----------------------------------------- | ---------------------------------------------------------- |
| NumberRange.New(`float` min, `float` max) | Creates a new NumberRange with the set min and max values. |

## Properties

| Name        | Description       |
| ----------- | ----------------- |
| `float` min | The minimum value |
| `float` max | The maximum value |

## Functions

| Name                        | Description                                     |
| --------------------------- | ----------------------------------------------- |
| NumberRange.Lerp(`float` t) | Linearly interpolates numbers min and max by t. |
