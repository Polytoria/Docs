# CreateImage
### Description
Create a GUI Image

Function of [UI](../../)

#### Return type
`UIImage`

### Example
```lua
local CoolImage = UI:CreateImage()
CoolImage.ImageID = 12384
CoolImage.ApplyAnchorPreset(AnchorPreset.Center)
CoolImage.Size = Vector2.New(200,200)
```