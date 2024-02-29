---
title: Game
description: Game is the root object in the Polytoria instance tree. It is the object of which everything is descended.
icon: polytoria/Game
weight: 1
---

# Game

{{ notnewable() }}

<div data-search-exclude markdown>
!!! tip "This object can be accessed in scripts by using the `game` keyword."
</div>

:polytoria-Game: Game is the root object in the Polytoria instance tree. It is the object of which everything is descended.

{{ inherits("Instance") }}

## Events

### Rendered { event }

Called every frame after the place has been rendered

<div data-search-exclude markdown>
!!! warning "Notice"

    The server is incapable of rendering frames; rather, on server Scripts, the event will fire at the server's tick rate which may vary between 1-30Hz.

    It is recommended to only listen to this event on LocalScripts.

</div>

## Properties

### GameID:int { property }

The ID of the current Polytoria place.

**Example**

```lua
print(game.GameID)
```

<div data-search-exclude markdown>
!!! note "The value is `0` when testing locally through Polytoria Creator, which can be used as a conditional to check if the place is live or not."
</div>

### InstanceCount:int { property }

The total number of instances currently loaded

**Example**

```lua
print(game.InstanceCount)
```

<div data-search-exclude markdown>
!!! note "Remarks"

    The value will differ depending on if it is being accessed through a Script or a LocalScript, as LocalScripts can only see instances that are relevant to the client.

</div>

### LocalInstanceCount:int { property }

The amount of instances currently loaded on the client.

**Example**

```lua
print(game.LocalInstanceCount)
```

### PlayersConnected:int { property }

Returns the amount of players connected to the game.

**Example**

```lua
print(game.PlayersConnected)
```

{{ readonly() }}
