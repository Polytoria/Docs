# ChildRemoved

### Description

Gets triggered when a child instance is removed.

Event of [Instance](/classes/Instance/)

#### Returns

`Instance`

### Example

```lua
game["Environment"].ChildRemoved:Connect(function (child)
    print(child.Name .. " was removed")
end)
```
