# TweenVector3

### Description

Tweens a vector3 between two specified values.

Function of [Tween](../../)

#### Parameters

StartValue `Vector3`  
EndValue `Vector3`  
Time `number`  
CallPerStep `function`
Type `TweenType`  
Callback `function`

### Example

```lua
Tween:TweenVector3(Vector3.New(0,0,0), Vector3.New(0,50,0), 5, function(val)
    part.Position = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```
