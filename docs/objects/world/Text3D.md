---
title: Text3D
description: Text3D allows placement of text in the world.

icon: polytoria/Text3D
weight: 4
---

# Text3D

:polytoria-Text3D: Text3D allows for placement of text in the world.

{{ inherits("DynamicInstance") }}

## Properties

### Color:Color { property }

Specifies the color of the text.

**Example**

```lua
-- Sets the text color to a random color
text.Color = Color.Random()
```

### FaceCamera:bool { property }

Determines whether or not the text should be facing the camera or not.

**Example**

```lua
text.FaceCamera = true
```

### Font:TextFontPreset { property }

Specifies the font of the text (using the `TextFontPreset` enum)

### FontSize:float { property }

Specifies the size of the font.

**Example**

```lua
text.FontSize = 64
```

### HorizontalAlignment:HorizontalAlignment { property }

Specifies the horizontal alignment of the text.

**Example**

```lua
text.HorizontalAlignment = HorizontalAlignment.Left
```

### Text:string { property }

Specifies the text to display.

**Example**

```lua
text.Text = "Hello world!"
```

### VerticalAlignment:VerticalAlignment { property }

Specifies the vertical alignment of the text.

**Example**

```lua
text.VerticalAlignment = VerticalAlignment.Middle
```
