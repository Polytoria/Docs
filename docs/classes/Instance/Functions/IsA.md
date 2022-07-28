# IsA

### Description

Returns whether the instance is of the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters

className `string`

#### Return type

`boolean`

### Example

```lua
part.Touched:Connect(function(other)
    if other:IsA("Player") then
        print("A player touched this part!")
    end
end)
```
