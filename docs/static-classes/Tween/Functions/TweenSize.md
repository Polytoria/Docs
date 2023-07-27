# TweenSize

### Description

Tweens the size of a DynamicInstance

Function of [Tween](../../)

#### Parameters

target `DynamicInstance`

destination `Vector3`

time `number`

type `TweenType`

callback `function`

### Example

```lua
Tween:TweenSize(part, Vector3.New(5, 5, 5), 1, TweenType.linear, function()
    print("Sizing finished")
end)
```
