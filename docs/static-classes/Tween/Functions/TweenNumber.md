# TweenNumber

### Description

Tweens a number between two specified values.

Function of [Tween](../../)

#### Parameters

startValue `number`

endValue `number`

time `number`

callPerStep `function`

type `TweenType`

callback `function`

### Example

```lua
Tween:TweenNumber(1, 10, 1, function(val)
    print(val)
end, TweenType.linear, function()
    print("Tween finished")
end)
```
