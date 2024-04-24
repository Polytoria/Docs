---
title: Players
description: Players is the container class for all Player instances.
icon: polytoria/Players
weight: 4
---

# Players

{{ ambiguous("Player", "the object that represents a single player.") }}

{{ service() }}

{{ notnewable() }}

:polytoria-Players: Players is the container class for all Player instances.

{{ inherits("Instance") }}

## Events

### PlayerAdded(player;Player) { event }

Fires when a player joins the server.

**Example**

```lua
game["Players"].PlayerAdded:Connect(function(player)
    if player.Name == "Player" then
        player:Kick("A player has joined the server, so they have been removed.")
    end
end)
```

### PlayerRemoved(player;Player) { event }

Fires when a player leaves the server.

**Example**

```lua
game["Players"].PlayerRemoved:Connect(function(player)
    if player.Name == "Player" then
        print("A player has left the server.")
    end
end)
```

## Methods

### GetPlayer(username;String):Player { method }

Returns the player instance from their username.

### GetPlayerByID(userID;int):Player { method }

Returns the player instance from their user ID.

### GetPlayers:array { method }

Returns all players in the place as a table.

**Example**

```lua
for i, player in ipairs(game["Players"]:GetPlayers()) do
    print(player.Name .." is in the server!")
end
```

## Properties

### LocalPlayer:Player { property }

Returns the local player currently playing.

{{ readonly() }}

{{ clientexclusive() }}

**Example**

```lua
print(game["Players"].LocalPlayer.Name)
```

### PlayerCollisionEnabled:bool { property }

Determines whether or not collisions between players are enabled.

**Example**

```lua
print("Turning off player collisions!")
game["Players"].PlayerCollisionEnabled = false
```
