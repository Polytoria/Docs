# Clone
### Description
Clones the instance.

Function of [Instance](/classes/Instance/)

#### Return type
`Instance`

### Example
```lua
local clone = part:Clone()
clone.Position = Vector3.New(0, 10, 0)
```

### Notes
- Not all instances can be cloned. Instances like Environment, Lighting, ScriptService cannot be cloned. In this case the function will return `nil`
