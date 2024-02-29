---
title: Player
description: Player is the class of the player and it's character controlled by it's player.
icon: polytoria/Player
weight: 5
---

# Player

{{ ambiguous("Players", "the service object that contains all connected players.") }}

{{ notnewable() }}

:polytoria-Player: Player is the class of the player and it's character controlled by it's player.

{{ inherits("DynamicInstance") }}

## Events

### Chatted(message;string) { event }

Fires when the player sends a chat message.

**Example**

```lua
game["Players"]["willemsteller"].Chatted:Connect(function (message)
    print("Player wrote: " .. message)
end)
```

### Died { event }

Fires when the player dies.

**Example**

```lua
game["Players"]["willemsteller"].Died:Connect(function ()
    print("Player died")
end)
```

### Respawned { event }

Fires when the player respawns.

**Example**

```lua
game["Players"]["willemsteller"].Respawned:Connect(function ()
    print("Player has respawned")
end)
```

## Methods

### DropTools { method }

Drops the tool the player is currently holding.

{{ serverexclusive() }}

### Kick(?Reason;string) { method }

Kicks the player from the server with an optional reason parameter.

{{ serverexclusive() }}

**Example**

```lua
game["Players"].PlayerAdded:Connect(function(player)
    if player.Name == "baggy" then
        player:Kick("Baggy u stink!!!")
    end
end)
```

### LoadAppearance(userID;int) { method }

Loads the specified user ID's avatar on the player.

**Example**

```lua
-- Loads the appearance of willemsteller
player:LoadAppearance(2)
```

### ClearAppearance { method }

Clears the player's appearance. This will set their appearance to a gray avatar.

**Example**

```lua
-- Clears the appearance of the player
player:ClearAppearance()
```

### OwnsItem(assetID;int,callback;function) { method }

Checks if the player owns an item

<div data-search-exclude markdown>
!!! note "The function will cache the result for 5 minutes."

!!! warning "There is a limit of 30 requests that can be made per minute per server."

</div>

**Example**

```lua
player:OwnsItem(24122, function(error, owns)
    if error then
        print("An error occurred!")
    else
        if owns then
            print("Player owns Polytoria Cap!")
        else
            print("Player does not own Polytoria Cap!")
        end
    end
end)
```

### ResetAppearance:void { method }

Resets the player's appearance to their original appearance.

**Example**

```lua
-- Resets the player's appearance back to their avatar
player:ResetAppearance()
```

### Respawn { method }

Respawns the player.

### Sit(Seat;Seat) { method }

Sit the player in a specific seat.

### Unsit(addForce;bool=false) { method }

Unsit the player.

## Properties

### CanMove:bool=true { property }

Determines whether or not the player can move.

### ChatColor:Color=(255,255,255) { property }

The player's username color in the chat.

```lua
game["Players"]["willemsteller"].ChatColor = Color3.New(0, 1, 0)
```

### HeadColor:Color { property }

Specifies the color of the players's head.

### Health:int=100 { property }

The current health of the player.

### IsAdmin:bool { property }

Returns whether or not the player is a Polytoria admin.

{{ readonly() }}

### IsCreator:bool { property }

Returns whether or not the player is the creator of the current place.

{{ readonly() }}

### IsInputFocused:bool { property }

Determines whether or not the player is currently focused on an input.

{{ readonly() }}

### JumpPower:int=36 { property }

Specifies how high the player's jump is.

### LeftArmColor:Color { property }

Specifies the color of the players's left arm.

### LeftLegColor:Color { property }

Specifies the color of the players's left leg.

### MaxHealth:int=100 { property }

Specifies the maximum health the player can have.

### MaxStamina:int=3 { property }

Specifies the maximum stamina the player can have.

### RespawnTime:int=5 { property }

Determines how long it takes between the player's death and respawn.

### RightArmColor:Color { property }

Specifies the color of the players's right arm.

### RightLegColor:Color { property }

Specifies the color of the players's right leg.

### SittingIn:Seat { property }

Returns the seat the player is currently sitting in, `nil` if the player is not sitting in any seat.

### SprintSpeed:int=25 { property }

Determines how fast the player is while sprinting.

<div data-search-exclude markdown>
!!! note "Remarks"

    Sprinting can be disabled by setting the player's SprintSpeed to their WalkSpeed.

</div>

### Stamina:int=0 { property }

The player's current amount of stamina.

### StaminaEnabled:bool=true { property }

Determines whether or not stamina is enabled for the player.

### StaminaRegen:int=1.2 { property }

The rate at which stamina regenerates after being depleted for the player.

### TorsoColor:Color { property }

Specifies the color of the players's torso.

### UserID:int { property }

Returns the player's user ID.

{{ readonly() }}

### WalkSpeed:int=16 { property }

Determines how fast the player walks.
