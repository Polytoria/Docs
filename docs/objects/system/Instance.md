---
title: Instance
description: Instance is the base class of all classes. Every class derives from it and has all properties, events and functions Instance has.
icon: polytoria/Instance
weight: 100
---

# Instance

{{ notnewable() }}

:polytoria-Instance: Instance is the base class of all classes. Every class derives from it and has all properties, events and functions Instance has.

{{ abstract() }}

## Events

### ChildAdded(child;Instance) { event }

Fires when a child instance is added.

**Example**

```lua
game["Environment"].ChildAdded:Connect(function (child)
    print(child.Name .. " was added")
end)
```

### ChildRemoved(child;Instance) { event }

Fires when a child instance is removed.

**Example**

```lua
game["Environment"].ChildRemoved:Connect(function (child)
    print(child.Name .. " was removed")
end)
```

### Clicked(player;Player) { event }

Fires when the instance is clicked by a player.

**Example**

```lua
game["Environment"]["Part"].Clicked:Connect(function (player)
    print(player.Name .. " clicked on this part!")
end)
```

### MouseEnter { event }

Fires when the mouse enters the instance.

**Example**

```lua
part.MouseEnter:Connect(function()
    part.Color = Color.New(1, 0, 0)
end)
```

### MouseExit { event }

Fires when the mouse enters the instance.

**Example**

```lua
part.MouseExit:Connect(function()
    part.Color = Color.New(0, 1, 0)
end)
```

### Touched(otherPart;Instance) { event }

Fires when the instance was touched by another instance. If you are trying to detect a player touching the instance, make sure to check with `otherPart:IsA('Player')` before continuing the anonymous function. Also, it's recommended to apply a debounce variable to the event.

**Example**

```lua
game["Environment"]["Part"].Touched:Connect(function (otherPart)
    print(otherPart.Name .. " touched this part!")
end)
```

<div data-search-exclude markdown>
!!! note "There must be an active collider on the instance for this event to trigger ({{ classLink("Part") }}, {{ classLink("Player") }}, etc.)"
</div>

### TouchEnded(otherPart;Instance) { event }

Fires when the instance is no longer being touched by another instance.

**Example**

```lua
game["Environment"]["Part"].TouchEnded:Connect(function (otherPart)
    print(otherPart.Name .. " stopped touching this part!")
end)
```

<div data-search-exclude markdown>
!!! note "There must be an active collider on the instance for this event to trigger ({{ classLink("Part") }}, {{ classLink("Player") }}, etc.)"
</div>

## Methods

### New(typeOfInstance;string):Instance { method }

Create a new instance.

**Example**

```lua
local newInstance = Instance.New("Part")
```

### New(typeOfInstance;string,parent;Instance):Instance { method }

Create a new instance.

**Example**

```lua
local newInstance = Instance.New("Part", game["Environment"])
```

### Clone { method }

Clones the instance

### Destroy { method }

Destroys the instance (same as Delete method)

### Delete { method }

Deletes the instance (same as Destroy method)

### GetParent:Instance { method }

Returns the parent of the instance (same as accessing the `.Parent` property).

### SetParent(newParent;Instance) { method }

Sets the parent of the instance (same as setting the `.Parent` property)

### IsA(className;string):bool { method }

Returns whether or not the instance is the specified class.

### IsDescendantOf(other;Instance):bool { method }

Returns whether or not the instance is a descendant (child, child of child, etc) of the specified instance.

### FindChild(name;string):Instance { method }

Attempts to find the first child instance with the specified name (`nil` if not found).

### FindChildByClass(className;string):Instance { method }

Attempts to find the first child instance with the specified class (`nil` if not found).

### GetChildren:Instance[] { method }

Returns an array of all the children instances parented to the instance.

### GetChildrenOfClass(className;string):Instance[] { method }

Returns an array of all the children instances with the specified class.

### GetBounds():Bounds { method }

Returns the bounds of the instance.

## Properties

### CanReparent:bool { property }

Returns whether this instance can be reparented/deleted or not.

### ClassName:string { property }

Returns the name of the class.

### Item:Instance { property }

Specifies the name of an instance.

### Name:string { property }

Specifies the name of an instance.

### Parent:Instance { property }

Specifies the parent instance of an instance.

### Shared:array { property }

An empty table you can use to hold metadata about anything on any object or player you want.

<div data-search-exclude markdown>
!!! note "Shared doesn't sync from the client to the server, or from the server to the client."
</div>

**Example**

```lua
-- Script 1
local players = game.Players.GetChildren()
local lucky = players[math.random(1, #players)]

lucky.Shared.IsZombie = true
```

```lua
-- Script 2
local killBrick = game.Environment["Kill Brick"]

killBrick.Touched:Connect(function(hit)
    if hit.IsA("Player") then
        if hit.Shared.IsZombie then
            print("YOU CAN'T KILL ME, I'M ALREADY DEAD!")
        else
            hit.Health = 0
        end
    end
end
```

### ClientSpawned:bool { property }

Returns whether or not the instance was spawned by the client.
