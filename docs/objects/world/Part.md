---
title: Part
description: Parts are physical objects that can be placed in the world.

icon: polytoria/Part
weight: 1
---

# Part

:polytoria-Part: Parts are physical objects that can be placed in the world.

{{ inherits("BasePart") }}

## Methods

### MovePosition(position;Vector3):void { method }

Moves the part to the specified position while keeping physics in mind.

**Example**

```lua
game["Environment"]["Part"]:MovePosition(Vector3.New(50, 0, 0))
```

### MoveRotation(rotation;Vector3):void { method }

Rotates the part while keeping physics in mind.

**Example**

```lua
game["Environment"]["Part"]:MovePosition(Vector3.New(0, 180, 0))
```

## Properties

### Anchored:bool { property }

Specifies whether the part is to be affected by physics or not.

### AngularDrag:int { property }

Angular drag (air resistance) of this part.

### AngularDrag:int { property }

Angular drag (air resistance) of this part.

### AngularVelocity:Vector3 { property }

Specifies the angular velocity of a part.

### CanCollide:bool { property }

Specifies whether the part can be collided with or not.

### Color:Color { property }

Specifies the color of a part.

### Drag:int { property }

Determines Drag (air resistance) of this part.

### Forward:Vector3 { property }

Returns the forward vector of the part

### HideStuds:bool { property }

Determines whether to display studs on the part or not.

### IsSpawn:bool { property }

Specifies whether the part can be used as a spawn location or not.

### Mass:int { property }

Specifies the mass of a part in kilograms.

### Material:PartMaterial { property }

Specifies the material of the part.

**Example**

```lua
part.Material = PartMaterial.Concrete
```

### Shape:PartShape { property }

Specifies the shape of a part.

**Example**

```lua
part.Shape = PartShape.Wedge
```

### UseGravity:bool { property }

Determines whether this part is affected by gravity or not.

### Velocity:Vector3 { property }

Specifies the velocity of a part.
