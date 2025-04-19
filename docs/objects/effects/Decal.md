---
title: Decal
description: Decals are objects that can have an image texture and are placed in the world.
icon: polytoria/Decal
---

# Decal

:polytoria-Decal: Decals are objects that can have an image texture and are placed in the world.

{{ inherits("DynamicInstance") }}

## Properties

### Color:Color { property }

Determines the color of the decal.

### ImageType:ImageType { property }

The type of image to be used.

### ImageID:int { property }

Specifies the image asset ID of the decal.

**Example**

```lua
game["Environment"]["Decal"].ImageID = 11643
```

### TextureOffset:Vector2 { property }

The offset of the texture on the decal.

### TextureScale:Vector2 { property }

The scale of the texture on the decal.

**Example**

```lua
game["Environment"]["Decal"].TextureOffset = Vector2.New(0, 0)
```

### CastShadows:bool { property }

Determines whether or not the decal should cast shadows.