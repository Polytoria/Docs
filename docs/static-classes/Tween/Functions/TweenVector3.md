# TweenVector3

### Description

Tweens a vector3 between two specified values.

Function of [Tween](../../)

#### Parameters

startValue `Vector3`

endValue `Vector3`

time `number`

callPerStep `function`

type `TweenType`

callback `function`

### Example

```lua
Tween:TweenVector3(Vector3.New(0,0,0), Vector3.New(0,50,0), 5, function(val)
    part.Position = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```
