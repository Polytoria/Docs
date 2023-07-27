# FindChild

### Description

Finds the first child instance with the specified name.

Function of [Instance](/classes/Instance/)

#### Parameters

name `string`

#### Returns

`Instance`

### Example

```lua
print(game:FindChild("Environment").Name) -- Prints "Environment"
```

### Notes

- Returns `nil` when no children are found.
