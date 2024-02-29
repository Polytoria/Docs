---
title: PlayerDefaults
description: PlayerDefaults is a service used for storing the default values of the Player when created.
icon: polytoria/PlayerDefaults
weight: 6
---

# PlayerDefaults

{{ service() }}

{{ notnewable() }}

:polytoria-PlayerDefaults: PlayerDefaults is a service used for storing the default values of the :polytoria-Player: Player when created.

{{ inherits("Instance") }}

## Methods

### LoadDefaults(player;Player) { method }

Resets the specified player back to their default values.

## Properties

### ChatColor:Color=(255,255,255) { property }

Determines the default color of players' usernames in chat.

### JumpPower:int=36 { property }

Determines how high the player jumps by default.

### MaxHealth:int=100 { property }

Determines the default maximum health of players.

### MaxStamina:int=3 { property }

Determines the default maximum stamina of players.

### RespawnTime:int=5 { property }

Determines the default of how long it takes between player's death and respawn.

### SprintSpeed:int=25 { property }

Determines the default sprint speed of players.

### Stamina:int=0 { property }

Determines the default stamina of players.

### StaminaEnabled:bool=true { property }

Determines whether or not stamina is enabled by default for players.

### StaminaRegen:int=1.2 { property }

Determines the default rate at which stamina regenerates after being depleted for players.

### WalkSpeed:int=16 { property }

Determines how fast the player walks by default.
