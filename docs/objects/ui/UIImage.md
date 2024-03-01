---
title: UIImage
description: UIImage is a class for displaying images in your place's UI.
icon: polytoria/UIImage
weight: 100
---

# UIImage

:polytoria-UIImage: UIImage is a class for displaying images in your place's UI.

{{ inherits("UIField") }}

## Properties

### Color:Color { property }

Specifies the color of the image.

**Example**

```lua
image.Color = Color.New(1, 0, 0)
```

### ImageID:int { property }

Specifies the image ID of the UIImage.

**Example**

```lua
image.ImageID = 12274
```

### ImageType:ImageType { property }

TO-DO

### Loading:bool { property }

Returns whether or not the image is loading.

**Example**

```lua
while image.Loading do
    wait(0)
end
print("Image loaded")
```

### Visible:bool { property }

Specifies if the image is visible.

**Example**

```lua
image.Visible = false
```
