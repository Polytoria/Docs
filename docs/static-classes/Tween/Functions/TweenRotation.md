# TweenRotation

### Description

Tweens the rotation of a DynamicInstance

Function of [Tween](../../)

#### Parameters

target `DynamicInstance`

destination `Vector3`

time `number`

type `TweenType`

callback `function`

### Example

```lua
Tween:TweenRotation(part, Vector3.New(0, 90, 0), 1, TweenType.linear, function()
    print("Rotating finished")
end)
```

## Notes

- Rotation is in euler angles.
