# TweenVector2

### Description

Tweens a vector2 between two specified values.

Function of [Tween](../../)

#### Parameters

startValue `Vector2`

endValue `Vector2`

time `number`

callPerStep `function`

type `TweenType`

callback `function`

### Example

```lua
Tween:TweenVector2(Vector2.New(0,0), Vector2.New(0,50), 5, function(val)
    UIView.PositionOffset = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```
