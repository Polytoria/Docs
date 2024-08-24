---
title: MeshPart
description: A part that can have custom mesh applied to it.

icon: polytoria/MeshPart
weight: 2
---

# MeshPart

:polytoria-MeshPart: MeshPart is a part that can have custom mesh applied to it, the mesh may be from the Polytoria Store (Hats, Tools and Heads) or user-uploaded meshes.

{{ inherits("Part") }}

## Methods

### MovePosition(position;Vector3) { method }

Moves the MeshPart to the specified position.

### MoveRotation(rotation;Vector3) { method }

Rotates the MeshPart to the specified rotation.

### PlayAnimation(animationName;string) { method }

Plays the animation with the specified name, if it exists.

### StopAnimation() { method }

Stops playing the current animation.

### GetAnimations() { method }

Returns the names of the animations associated with the mesh.

## Properties

### Anchored:bool { property }

Specifies whether the part is to be affected by physics or not.

### AngularVelocity:Vector3 = Vector3.New(0, 0, 0) { property }

Specifies the angular velocity of a part.

### AssetID:int { property }

The asset ID of the mesh part.

### CanCollide:bool { property }

Specifies whether the part can be collided with or not.

### Mass:float { property }

Specifies the mass of a part in kilograms.

### Material:PartMaterial { property }

Specifies the material of the part.

### Shape:PartShape { property }

Specifies the shape of a part.

### Velocity:Vector3 = Vector3.New(0, 100, 0) { property }

Specifies the velocity of a part.
