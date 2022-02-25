# CreateLabel
### Description
Create a GUI Text

Function of [UI](../../)

#### Parameters
Text `string`  

#### Return type
`UILabel`

### Example
```lua
local Text = UI:CreateLabel()
Text.ApplyAnchorPreset(AnchorPreset.Center)
Text.Size = Vector2.New(200,200)

for i = 10, 0, 1 do
    Text.Text = i
end
Text.Text = "😁 Hi!"
```