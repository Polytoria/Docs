# TweenPosition
### Description
Tweens the position of a DynamicInstance

Function of [Tween](../../)

#### Parameters
Target `DynamicInstance`  
Destination `Vector3`  
Time `number`  
Type `TweenType`  
Callback `function`

### Example
```lua
Tween:TweenPosition(part, Vector3.New(100, 0, 0), 100, TweenType.linear, function() 
    print("I have arrived!")
end)
```
