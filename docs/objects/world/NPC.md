---
title: NPC
description: An NPC (non-player character) is an object similar to a Player but that can be controlled by code.

icon: polytoria/NPC
weight: 5
---

# NPC

:polytoria-NPC: NPC (non-player character) is an object similar to a {{ classLink("Player") }} but that can be controlled by code. Like players, it can walk and jump, and its body part colors can be customized.

{{ inherits("DynamicInstance") }}

## Events

### Died { event }

Fires when the NPC dies.

**Example**

```lua
game["Environment"]["NPC"].Died:Connect(function ()
    print("NPC died!")
end)
```

## Methods

### LoadAppearance(userID;int) { method }

Loads the specified user ID's avatar on the NPC.

**Example**

```lua
-- Loads the appearance of willemsteller
npc:LoadAppearance(2)
```

### ClearAppearance { method }

Clears the NPC's appearance.

**Example**

```lua
-- Clears the appearance of the NPC
npc:ClearAppearance()
```

## Properties

### Anchored:bool { property }

Determines whether the NPC is affected by physics or not.

### FaceID:int { property }

The face ID of the NPC's face.

### Grounded:bool { property }

Returns true if the NPC is currently standing on the ground.

### HeadColor:Color { property }

Specifies the color of the NPC's head.

### Health:int { property }

Specifies the current amount of health the NPC has.

### MoveTarget:Instance { property }

Determines the instance the NPC should walk towards.

### WalkSpeed:int { property }

Determines the walkspeed of the NPC.

### MaxHealth:int=100 { property }

Specifies the maximum amount of health a NPC can have.

### ShirtID:int { property }

Specifies the shirt ID of the NPC's shirt.

### PantsID:int { property }

The pants ID of the NPC's pants.

### TorsoColor:Color { property }

Specifies the color of the NPC's torso.

### LeftArmColor:Color { property }

Specifies the color of the NPC's left arm.

### RightArmColor:Color { property }

Specifies the color of the NPC's right arm.

### LeftLegColor:Color { property }

Specifies the color of the NPC's left leg.

### RightLegColor:Color { property }

Specifies the color of the NPC's right leg.
