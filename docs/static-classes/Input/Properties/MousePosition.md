# MousePosition

### Description

Get current mouse position.

Property of [Input](../../)

#### Type

`Vector2`

### Example

```lua
local Text = script.Parent["Text"]

game.Rendered:Connect(function()
    Text.Position = Input.MousePosition
end)
```
