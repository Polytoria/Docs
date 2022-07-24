# Changed

### Description

Gets invoked when the value of this object changes.

Event of [ValueBase](/classes/ValueBase/)

### Example

```lua
boolValue.Changed:Connect(function()
    print("My new value is " .. boolValue.Value)
end)
```
