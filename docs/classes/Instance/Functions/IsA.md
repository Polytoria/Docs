# IsA
### Description
Returns whether the instance is of the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters
className `String`

#### Return type
`Boolean`

### Example
```lua
part.Touched:Connect(function(other)
    if other:IsA("Player") then
        print("A player touched this part!")
    end
end)
```
