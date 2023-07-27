# GetChildrenOfClass

### Description

Returns a list of all children with the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters

className `string`

#### Returns

`Instance[]`

### Example

```lua
for i, child in pairs(game["Environment"]:GetChildrenOfClass("Part")) do
    print(child.Name)
end
```
