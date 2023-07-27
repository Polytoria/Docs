# LookAt

### Description

Rotates the DynamicInstance so that the forward vector looks at the target.

Function of [DynamicInstance](/classes/DynamicInstance/)

#### Parameters

target `DynamicInstance`
worldUp `Vector3` = (0, 1, 0)

OR

target `Vector3`
worldUp `Vector3` = (0, 1, 0)

#### Returns

`void`

### Example

```lua
part.LookAt(Vector3.New(12, 34, 56))
```
