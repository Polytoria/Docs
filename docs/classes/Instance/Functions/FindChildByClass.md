# FindChildByClass
### Description
Finds the first child instance of the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters
className `String`

#### Return type
`Instance`

### Example
```lua
print(game:FindChildOfClass("Environment").Name) -- Prints "Environment"
```

### Notes
- Returns `nil` when no children are found.
