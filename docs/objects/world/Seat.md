---
title: Seat
description: Seats are parts the player can sit on.

icon: polytoria/Seat
weight: 3
---

# Seat

:polytoria-Seat: Seats are parts the player can sit on.

{{ inherits("Part") }}

## Events

### Sat(player;Player) { event }

Fires when a player sits in the seat.

### Vacated(player;Player) { event }

Fires when a player leaves the seat.

## Properties

### Occupant:Player { property }

The player that is currently sitting in this seat.

**Example**

```lua
seat.Occupant:Unsit()
```
