# TweenColor
### Description
Tweens a color between two specified values.

Function of [Tween](../../)

#### Parameters
StartValue `Color`  
EndValue `Color`  
Time `number`  
CallPerStep `function`
Type `TweenType`  
Callback `function`

### Example
```lua
Tween:TweenColor(Color.New(1,1,1,1), Color.New(1,1,1,0), 5, function(val) 
    part.Color = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```
