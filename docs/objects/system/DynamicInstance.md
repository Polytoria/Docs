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

### LookAt(rotation;Vector3,worldUp;Vector3) { method }

Rotates the DynamicInstance so that the forward vector looks at the target.

### LookAt(dynamicInstance;DynamicInstance) { method }

Rotates the DynamicInstance so that the forward vector looks at the target.

### Translate(translation;Vector3) { method }

Moves the transform in the direction and distance of translation.

**Example**

```lua
part.Translate(part.Forward * 5)
```

### RotateAround(point;Vector3,axis;Vector3,angle;float) { method }

Rotates the DynamicInstance around a point.

### Rotate(eulerAngles;Vector3) { method }

Rotates the DynamicInstance by the specified Euler angles.

### InverseTransformPoint(point;Vector3):Vector3 { method }

Undocumented

### TransformPoint(point;Vector3):Vector3 { method }

Undocumented

### InverseTransformDirection(direction;Vector3):Vector3 { method }

Undocumented

### TransformDirection(direction;Vector3):Vector3 { method }

Undocumented

### InverseTransformVector(vector;Vector3):Vector3 { method }

Undocumented

### InverseTransformPosition(position;Vector3):Vector3 { method }

Undocumented

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

### Quaternion:Quaternion { property }

The quaternion of this DynamicInstance

### LocalQuaternion:Quaternion { property }

The local quaternion of this DynamicInstance
