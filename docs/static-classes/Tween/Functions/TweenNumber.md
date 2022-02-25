# TweenNumber
### Description
Tweens the number

Function of [Tween](../../)

#### Parameters
StartValue `number`  
EndValue `number`  
Time `number`  
CallPerStep `function`
Type `TweenType`  
Callback `function`

### Example
```lua
Tween:TweenNumber(1, 10, 1, function(val) 
    print(val)
end, TweenType.linear,function()
    print("I'm Here!")
end)
```
