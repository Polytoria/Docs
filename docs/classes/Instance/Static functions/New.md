# New
### Description
Creates a new instance of the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters
ClassName `string`  
Parent `Instance`

#### Returns
Instance `Instance`

### Example
```lua
local part = Instance.New("Part", game["Environment"])
part.Size = Vector3.New(4, 4, 4)
part.Color = Color.New(0.5, 0.5, 0.5, 1.0)
```

### Notes
- Not all instances can be instantiated. Instances like Environment, Lighting, ScriptService cannot be created. In this case the function will throw an exception.
- The default Parent parameter is [Environment](/classes/Environment/) and can be left blank.