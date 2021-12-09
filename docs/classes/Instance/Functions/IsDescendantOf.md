# IsDescendantOf
### Description
Returns true if the instance is a descendant (child, child of child, etc.) of the specified instance.

Function of [Instance](/classes/Instance/)

#### Parameters
other `Instance`

#### Return type
`Boolean`

### Example
```lua
print(game["Environment"]["Part"]["Part"]:IsDescendantOf(game["Environment"])) -- true
```
