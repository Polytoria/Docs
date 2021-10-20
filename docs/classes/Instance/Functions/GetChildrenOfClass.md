# GetChildrenOfClass
### Description
Returns a list of all children with the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters
ClassName `string`

#### Returns
Children `Array`

### Example
```lua
for i, child in pairs(game["Environment"]:GetChildrenOfClass("Part")) do
    print(child.Name)
end
```