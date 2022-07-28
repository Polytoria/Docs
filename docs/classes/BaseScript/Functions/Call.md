# Call

### Description

Calls a function of this script.

Function of [BaseScript](/classes/BaseScript/)

#### Parameters

function `string`
args `DynValue[]`

### Example

```lua
game["ScriptService"]["Script"]:Call("Foo", "Bar")
```

### Notes

- Local functions cannot be called
