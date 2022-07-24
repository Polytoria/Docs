# CreateImage

<div class="alert alert-danger">Removed in version 1.2.0</div>

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
