---
title: PointLight
description: PointLight is a source of light that can be placed in the world.
icon: polytoria/PointLight
---

# PointLight

:polytoria-PointLight: PointLight is a source of light that can be placed in the world.

{{ inherits("DynamicInstance") }}

## Properties

### Brightness:int { property }

Specifies how bright/intense the light is.

**Example**

```lua
light.Brightness = 0.75
```

### Color:Color { property }

Specifies the color of the light.

**Example**

```lua
light.Color = Color.Random()
```

### Range:int { property }

Specifies how far out the light can reach.

**Example**

```lua
light.Range = 60
```

### Shadows:bool { property }

Specifies whether this light emits shadows or not.

**Example**

```lua
light.Shadows = true
```

<div data-search-exclude markdown>
!!! note "Shadows"

    Having many lights with shadows enabled will cause a massive hit in performance. Consider minimizing the amount of lights with shadows to ensure every player is enjoying your place with minimal framerate issues.

</div>
