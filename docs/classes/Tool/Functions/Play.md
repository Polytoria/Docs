# Play

### Description

Plays an animation on the tool or the player that is currently holding the tool.

Function of [Tool](/classes/Tool/)

#### Parameters

name `string`

#### Returns

`void`

### Example

```lua
local tool = script.Parent

tool.Activated:Connect(function()
    tool:Play("slash")
end)
```

### Animation List

```
slash (Sword Animation)
eat (Eating Animation)
drink (Drinking Animation)
```
