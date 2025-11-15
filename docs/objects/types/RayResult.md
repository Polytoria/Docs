---
title: RayResult
description: RayResult is a data type that contains data about a raycast result.
icon: polytoria/RayResult
---

# RayResult

:polytoria-RayResult: RayResult is a data type that contains data about a raycast result.

## Constructors

| Name                | Description                              |
| ------------------- | ---------------------------------------- |
| `Instance` Instance | The instance hit by the raycast.         |
| `Vector3` Position  | The position the ray made contact at.    |
| `float` Distance    | The distance between the hit and origin. |
| `Vector3` Normal    | The normal of the surface the ray hit.   |

<div data-search-exclude markdown>
Normal is a naturally complicated property to describe. In a simple case of a cube, Normal describes the exact side the RayResult hit, with x being left/right, y being top/bottom, and z being front/back. For a more complicated hitbox like a Sphere, the values can blend together. It's important to remember that the Instance's Rotation should be considered when making calculations with Normal.
</div>