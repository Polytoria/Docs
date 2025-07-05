---
title: Part
description: Parts are physical objects that can be placed in the world.

icon: polytoria/Part
weight: 1
---

# Part

:polytoria-Part: Parts are physical objects that can be placed in the world.

{{ inherits("DynamicInstance") }}

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
game["Environment"]["Part"]:MoveRotation(Vector3.New(0, 180, 0))
```

### AddForce(force;Vector3,mode;ForceMode) { method }

Adds a force to the part.

### AddTorque(torque;Vector3,mode;ForceMode) { method }

Adds a torque to the part.

### AddForceAtPosition(force;Vector3,position;Vector3,mode;ForceMode) { method }

Adds a force to the part at a specific position.

### AddRelativeForce(force;Vector3,mode;ForceMode) { method }

Adds a force to the part relative to its own rotation.

### AddRelativeTorque(torque;Vector3,mode;ForceMode) { method }

Adds a torque to the part relative to its own rotation.

## Properties

### Anchored:bool { property }

Specifies whether the part is to be affected by physics or not.

### AngularDrag:float { property }

Angular drag (air resistance) of this part.

### AngularVelocity:Vector3 { property }

Specifies the angular velocity of a part.

### Bounciness:float { property }

Determines how bouncy the part is when players land on it.

### CanCollide:bool { property }

Specifies whether the part can be collided with or not.

### CastShadows:bool { property }

Specifies whether the part casts its shadow on other parts.

### Color:Color { property }

Specifies the color of a part.

### Drag:float { property }

Determines Drag (air resistance) of this part.

### Friction:float { property }

Determines the amount of friction between the part and players on it.

### Forward:Vector3 { property }

Returns the forward vector of the part

### HideStuds:bool { property }

Determines whether to display studs on the part or not.

### IsSpawn:bool { property }

Specifies whether the part can be used as a spawn location or not.

### Mass:float { property }

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
