# TweenRotation
### Description
Tweens the rotation of a DynamicInstance

Function of [TweenService](../../)

#### Parameters
Target `DynamicInstance`  
Destination `Vector3`  
Time `number`  
Type `TweenType`  
Callback `function`

### Example
```lua
TweenService:TweenRotation(part, Vector3.New(0, 90, 0), 1, TweenType.linear, function() 
    print("Rotating finished")
end)
```

## Notes
- Rotation is in euler angles.
