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

### Chatted(message;string,event;table={Player|message|Canceled}) { event }

Fires when the player sends a chat message. You can prevent other players from seeing the chat message by setting the event's `Canceled` property like this: `event.Canceled = true`.

**Example**

```lua
game["Players"]["willemsteller"].Chatted:Connect(function (message, event)
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
    if player.Name == "Player" then
        player:Kick("You've been kicked from the server.")
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

### Anchored:bool=false { property }

Determines whether or not the player is anchored. The idle animation still plays and this property does not reset on respawn/reset.

### CanMove:bool=true { property }

Determines whether or not the player can move.

### ChatColor:Color=(255,255,255) { property }

The player's username color in the chat.

```lua
game["Players"]["willemsteller"].ChatColor = Color3.New(0, 1, 0)
```

### ShirtID:int { property }

Determines the ID of the shirt the player is wearing.

### PantsID:int { property }

Determines the ID of the pants the player is wearing.

### FaceID:int { property }

Determines the ID of the face the player is wearing.

### HeadColor:Color { property }

Specifies the color of the players's head.

### Health:float=100 { property }

The current health of the player.

### IsAdmin:bool { property }

Returns whether or not the player is a Polytoria admin.

{{ readonly() }}

### IsCreator:bool { property }

Returns whether or not the player is the creator of the current place.

{{ readonly() }}

### IsInputFocused:bool { property }

Determines whether or not the player is currently focused on an input.

<div data-search-exclude markdown>
!!! note "The {{ classLink("Player") }} `.IsInputFocused` property has been moved to the {{ classLink("Input") }} static class, however the property still exists on the {{ classLink("Player") }} class for backwards-compatibility."
</div>

{{ readonly() }}

### JumpPower:float=36 { property }

Specifies how high the player's jump is.

### LeftArmColor:Color { property }

Specifies the color of the players's left arm.

### LeftLegColor:Color { property }

Specifies the color of the players's left leg.

### MaxHealth:float=100 { property }

Specifies the maximum health the player can have.

### MaxStamina:float=3 { property }

Specifies the maximum stamina the player can have.

### RespawnTime:float=5 { property }

Determines how long it takes between the player's death and respawn.

### RightArmColor:Color { property }

Specifies the color of the players's right arm.

### RightLegColor:Color { property }

Specifies the color of the players's right leg.

### SittingIn:Seat { property }

Returns the seat the player is currently sitting in, `nil` if the player is not sitting in any seat.

### SprintSpeed:float=25 { property }

Determines how fast the player is while sprinting.

<div data-search-exclude markdown>
!!! note "Remarks"

    Sprinting can be disabled by setting the player's SprintSpeed to their WalkSpeed.

</div>

### Stamina:float=0 { property }

The player's current amount of stamina.

### StaminaEnabled:bool=true { property }

Determines whether or not stamina is enabled for the player.

### StaminaRegen:float=1.2 { property }

The rate at which stamina regenerates after being depleted for the player.

### TorsoColor:Color { property }

Specifies the color of the players's torso.

### UserID:int { property }

Returns the player's user ID.

{{ readonly() }}

### WalkSpeed:float=16 { property }

Determines how fast the player walks.
