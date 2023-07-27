# FindChildByClass

### Description

Finds the first child instance of the specified class.

Function of [Instance](/classes/Instance/)

#### Parameters

className `string`

#### Returns

`Instance`

### Example

```lua
print(game:FindChildByClass("Environment").Name) -- Prints "Environment"
```

### Notes

- Returns `nil` when no children are found.
