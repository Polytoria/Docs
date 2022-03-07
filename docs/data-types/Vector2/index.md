# Vector2
### Description
Vector2 is a 2D vector with an x and y component.

### Constructors
|Vector2.New()|
|---|
|Creates a new Vector.|

|Vector2.New(`number` n)|
|---|
|Creates a new Vector2 with an X and Y value of n.|


|Vector2.New(`number` x, `number` y)|
|---|
|Creates a new Vector2 with the specified values.|

### Properties
|`number` x|
|---|
|The X component of the vector|

|`number` y|
|---|
|The Y component of the vector|

|`number` magnitude|
|---|
|The length of this vector|

|`number` sqrMagnitude|
|---|
|The squared length of this vector|

|`number` normalized|
|---|
|Returns this vector with a magnitude of 1|

### Functions
|`Vector2` Vector2.Lerp(`Vector2` a, `Vector2` b, `number` t)|
|---|
|Linearly interpolates between two points.|