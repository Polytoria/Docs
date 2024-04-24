---
title: Vector2
description: Vector2 is a 2D Vector with an x and y component, commonly used with UI.
icon: polytoria/Vector2
---

# Vector2

:polytoria-Vector2: Vector2 is a 2D vector with an x and y component, commonly used with UI.

## Constructors

| Name                                | Description                                       |
| ----------------------------------- | ------------------------------------------------- |
| Vector2.New()                       | Creates a new Vector.                             |
| Vector2.New(`float` n)             | Creates a new Vector2 with an X and Y value of n. |
| Vector2.New(`float` x, `float` y) | Creates a new Vector2 with the specified values.  |

## Properties

| Name                  | Description                               |
| --------------------- | ----------------------------------------- |
| `float` x             | The X component of the vector             |
| `float` y             | The Y component of the vector             |
| `float` magnitude     | The length of this vector                 |
| `float` sqrMagnitude  | The squared length of this vector         |
| `float` normalized    | Returns this vector with a magnitude of 1 |

## Methods

| Name                                                         | Description                               |
| ------------------------------------------------------------ | ----------------------------------------- |
| `Vector2` Vector2.Lerp(`Vector2` a, `Vector2` b, `float` t)  | Linearly interpolates between two points. |
