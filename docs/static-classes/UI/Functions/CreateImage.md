# CreateImage
### Description
Creates an UI image.

Function of [UI](../../)

#### Return type
`UIImage`

### Example
```lua
local image = UI:CreateImage()
image.ImageID = 12384
image.ApplyAnchorPreset(AnchorPreset.Center)
image.Size = Vector2.New(200,200)
```