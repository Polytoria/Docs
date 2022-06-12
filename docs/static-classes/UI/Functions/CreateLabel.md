# CreateLabel

<div class="alert alert-danger">Removed in version 1.2.0</div>

### Description
Creates a text label.

Function of [UI](../../)

#### Parameters
Text `string` (default = "")

#### Return type
`UILabel`

### Example
```lua
local text = UI:CreateLabel()
text.ApplyAnchorPreset(AnchorPreset.Center)
text.Size = Vector2.New(200, 32)
text.Text = "Hello, world!"
```