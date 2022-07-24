# ChildAdded

### Description

Gets triggered when a child instance is added.

Event of [Instance](/classes/Instance/)

#### Returns

`Instance`

### Example

```lua
game["Environment"].ChildAdded:Connect(function (child)
    print(child.Name .. " was added")
end)
```
