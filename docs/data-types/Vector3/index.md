# Vector3

### Description

Vector3 is a 3D vector with an x, y and z component.

### Constructors

| Vector3.New()         |
| --------------------- |
| Creates a new Vector. |

| Vector3.New(`number` n)                              |
| ---------------------------------------------------- |
| Creates a new Vector3 with an X, Y and Z value of n. |

| Vector3.New(`number` x, `number` y)                                          |
| ---------------------------------------------------------------------------- |
| Creates a new Vector3 with X and Y set to the specified values and a Z of 0. |

| Vector3.New(`number` x, `number` y, `number` z)  |
| ------------------------------------------------ |
| Creates a new Vector3 with the specified values. |

### Properties

| `number` x                    |
| ----------------------------- |
| The X component of the vector |

| `number` y                    |
| ----------------------------- |
| The Y component of the vector |

| `number` z                    |
| ----------------------------- |
| The Z component of the vector |

| `number` magnitude        |
| ------------------------- |
| The length of this vector |

| `number` sqrMagnitude             |
| --------------------------------- |
| The squared length of this vector |

| `number` normalized                       |
| ----------------------------------------- |
| Returns this vector with a magnitude of 1 |

### Functions

| `number` Vector3.Angle(`Vector3` from, `Vector3` to) |
| ---------------------------------------------------- |
| Returns the angle in degrees between from and to.    |

| `Vector3` Vector3.ClampMagnitude(`Vector3` vector, `number` maxLength) |
| ---------------------------------------------------------------------- |
| Returns a copy of this vector with its magnitude clamped to maxLength  |

| `Vector3` Vector3.Cross(`Vector3` a, `Vector3` b) |
| ------------------------------------------------- |
| Cross product of two vectors.                     |

| `number` Vector3.Distance(`Vector3` a, `Vector3` b) |
| --------------------------------------------------- |
| Returns the distance between a and b                |

| `number` Vector3.Dot(`Vector3` a, `Vector3` b) |
| ---------------------------------------------- |
| Dot product of two vectors                     |

| `Vector3` Vector3.Lerp(`Vector3` a, `Vector3` b, `number` t) |
| ------------------------------------------------------------ |
| Linearly interpolates between two points.                    |

| `Vector3` Vector3.Max(`Vector3` a, `Vector3` b)                           |
| ------------------------------------------------------------------------- |
| Returns a vector that is made from the largest components of two vectors. |

| `Vector3` Vector3.Min(`Vector3` a, `Vector3` b)                            |
| -------------------------------------------------------------------------- |
| Returns a vector that is made from the smallest components of two vectors. |

| `Vector3` Vector3.MoveTowards(`Vector3` current, `Vector3` target, `number` maxDistanceDelta)                                               |
| ------------------------------------------------------------------------------------------------------------------------------------------- |
| Calculate a position between the points specified by current and target, moving no farther than the distance specified by maxDistanceDelta. |

| `Vector3` Vector3.Normalize(`Vector3` value) |
| -------------------------------------------- |
| Makes this vector have a magnitude of 1.     |

| `Vector3` Vector3.Project(`Vector3` vector, `Vector3` onNormal) |
| --------------------------------------------------------------- |
| Projects a vector onto another vector.                          |

| `Vector3` Vector3.ProjectOnPlane(`Vector3` vector, `Vector3` planeNormal)   |
| --------------------------------------------------------------------------- |
| Projects a vector onto a plane defined by a normal orthogonal to the plane. |

| `Vector3` Vector3.Reflect(`Vector3` inDirection, `Vector3` inNormal) |
| -------------------------------------------------------------------- |
| Reflects a vector off the plane defined by a normal.                 |

| `Vector3` Vector3.RotateTowards(`Vector3` current, `Vector3` target, `number` maxRadiansDelta, `number` maxMagnitudeDelta) |
| -------------------------------------------------------------------------------------------------------------------------- |
| Rotates a vector current towards target.                                                                                   |

| `Vector3` Vector3.Scale(`Vector3` a, `Vector3` b) |
| ------------------------------------------------- |
| Multiplies two vectors component-wise.            |

| `number` Vector3.SignedAngle(`Vector3` from, `Vector3` to, Vector3 axis) |
| ------------------------------------------------------------------------ |
| Returns the signed angle in degrees between from and to.                 |

| `Vector3` Vector3.Slerp(`Vector3` a, `Vector3` b) |
| ------------------------------------------------- |
| Spherically interpolates between two vectors.     |

| `Vector3` Vector3.SlerpUnclamped(`Vector3` a, `Vector3` b) |
| ---------------------------------------------------------- |
| Spherically interpolates between two vectors.              |

| `Vector3` Vector3.SmoothDamp(`Vector3` current, `Vector3` target, `ref Vector3` currentVelocity, `number` smoothTime, `number` maxSpeed, `number` deltaTime) |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Gradually changes a vector towards a desired goal over time.                                                                                                 |
