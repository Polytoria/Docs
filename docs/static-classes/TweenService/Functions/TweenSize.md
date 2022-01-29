# TweenSize
### Description
Tweens the size of a DynamicInstance

Function of [TweenService](../../)

#### Parameters
Target `DynamicInstance`  
Destination `Vector3`  
Time `number`  
Type `TweenType`  
Callback `function`

### Example
```lua
TweenService:TweenSize(part, Vector3.New(5, 5, 5), 1, TweenType.linear, function() 
    print("Sizing finished")
end)
```
