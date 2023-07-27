# TweenVector2

### Description

Tweens a vector2 between two specified values.

Function of [Tween](../../)

#### Parameters

StartValue `Vector2`
EndValue `Vector2`
Time `number`
CallPerStep `function`
Type `TweenType`
Callback `function`

### Example

```lua
Tween:TweenVector2(Vector2.New(0,0), Vector2.New(0,50), 5, function(val)
    UIView.PositionOffset = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```
