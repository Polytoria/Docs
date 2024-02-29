---
title: DynamicInstance
description: DynamicInstance is the base class where all objects with a position, rotation and scale derive from.
icon: polytoria/DynamicInstance
weight: 101
---

# DynamicInstance

:polytoria-DynamicInstance: DynamicInstance is the base class where all objects with a position, rotation and scale derive from.

{{ abstract() }}

{{ inherits("Instance") }}

## Methods

### LookAt(rotation;Vector3) { method }

Rotates the DynamicInstance so that the forward vector looks at the target.

**Example**

```lua
part.LookAt(Vector3.New(12, 34, 56))
```

### Translate(translation;Vector3) { method }

Moves the transform in the direction and distance of translation.

**Example**

```lua
part.Translate(part.Forward * 5)
```

## Properties

### Forward:Vector3 { property }

The forward vector of this DynamicInstance

### LocalPosition:Vector3 = Vector3.New(0, 10, 0) { property }

Specifies the position relative to the parent of an instance.

### LocalRotation:Vector3 = Vector3.New(0, 45, 0) { property }

Specifies the rotation relative to the parent of an instance.

<div data-search-exclude markdown>
!!! note "Rotation is in euler angles."
</div>

### LocalSize:Vector3 = Vector3.New(1, 1, 1) { property }

The size of the instance relative to its parent.

### Position:Vector3 = Vector3.New(0, 10, 0) { property }

Specifies the position of an instance.

### Right:Vector3 { property }

The right vector of this DynamicInstance

**Example**

```lua
part.Translate(part.Right * 5)
```

### Rotation:Vector3 = Vector3.New(0, 45, 0) { property }

Specifies the rotation of an instance.

<div data-search-exclude markdown>
!!! note "Rotation is in euler angles."
</div>

### Size:Vector3 = Vector3.New(5, 10, 4) { property }

Specifies the size of an instance.

### Up:Vector3 { property }

The Y axis of this DynamicInstance
