---
title: ColorRange
description: ColorRange is a data type that represents a color range.
icon: polytoria/Unknown
---

# ColorRange

:polytoria-Unknown: ColorRange is a data type that represents a color range.

## Constructors

| Name                                                  | Description                                                                |
| ----------------------------------------------------- | -------------------------------------------------------------------------- |
| ColorRange.New(`Color` min, `Color` max)              | Creates a new ColorRange with the set min and max values.                  |

## Properties

| Name        | Description                     |
| ----------- | ------------------------------- |
| `Color` min | The minimum value               |
| `Color` max | The maximum value               |

## Functions

| Name                                         | Description                                    |
| -------------------------------------------- | ---------------------------------------------- |
| ColorRange.Lerp(`float` t)                   | Linearly interpolates colors min and max by t. |
