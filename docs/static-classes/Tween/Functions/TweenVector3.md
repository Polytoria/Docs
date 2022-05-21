# TweenVector3
### Description
Tweens the position of a DynamicInstance

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
Tween:TweenVector3(part.Position, Vector3.New(100, 0, 0), 1, function(val)
  part.Position = val
end, TweenType.linear, function()
    print('Tween Finished')
end)
```
