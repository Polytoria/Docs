# MousePosition

### Description

Get current mouse position.

Property of [Input](../../)

#### Type

`Vector2`

### Example

```lua
local Text = UI:CreateLabel("I will keep following the cursor!")
Text.Size = Vector2.New(200,200)

game.Rendered:Connect(function()
    Text.Position = Input.MousePosition
end)
```
