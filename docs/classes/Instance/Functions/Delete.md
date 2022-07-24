# Delete

### Description

Deletes the instance.

Function of [Instance](/classes/Instance/)

#### Parameters

Delay `number, default = 0`

#### Return type

`Void`

### Example

```lua
instance:Delete(1) -- Will delete the object after 1 second.
```

### Notes

- Delete is a convenient rewrite of [Destroy](../Destroy) and calls [Destroy](../Destroy) internally. The functions are both the same.
