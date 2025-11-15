---
title: Environment
description: Environment is the primary object intended for storing active objects in the place.
icon: polytoria/Environment
weight: 2
---

# Environment

{{ service() }}

{{ notnewable() }}

:polytoria-Environment: Environment is the primary object intended for storing active objects in the place.

{{ inherits("Instance") }}

## Methods

### CreateExplosion(Position;Vector3,?Radius;float=10,?Force;float=5000,?affectAnchored;bool=true,?callback;function=DynamicInstance,?damage;float=10000) { method }

Creates a deadly explosion killing {{ classLink("Players") }} and applying force to {{ classLink("DynamicInstance") }}s at the given position.

**Example**

```lua
game["Environment"]:CreateExplosion(Vector3.New(0, 0, 0), 30, 5000, false, nil, 10)
```

<div data-search-exclude markdown>
!!! note "When set to true, AffectAnchored will disable the Anchor property for {{ classLink("DynamicInstance") }}s within the explosion radius."
</div>

<div data-search-exclude markdown>
!!! note "Callback gets called for each {{ classLink("DynamicInstance") }} within explosion radius."
</div>

### OverlapBox(position;Vector3,size;Vector3,rotation;Vector3,?ignoreList;array={Instance}):{Instance} { method }

Returns a list of {{ classLink("DynamicInstance") }}s intersecting with the box in the given position, size and rotation.

A demo of this method is available [here](https://polytoria.com/places/9269).

**Example**

```lua
local intersections = game["Environment"]:OverlapBox(Vector3.New(0,0,0), Vector3.New(2,2,3), Vector3.New(0,0,0))

for i,v in ipairs(intersections) do
    print(v.Name .." is intersecting the box!")
end
```

### OverlapSphere(position;Vector3,radius;float,?ignoreList;array={Instance}):{Instance} { method }

Returns a list of {{ classLink("DynamicInstance") }}s intersecting with the sphere in the given position and radius.

**Example**

```lua
local intersections = game["Environment"]:OverlapSphere(Vector3.New(100,0,45), 25, {game["Environment"]["TheIgnored"]})

for i,v in ipairs(intersections) do
    print(v.Name .." is intersecting the sphere!")
end
```

### Raycast(origin;Vector3,direction;Vector3,?maxDistance;float=infinite,?ignoreList;array={Instance}):RayResult { method }

Casts a ray from origin, shooting in the direction of the second argument until it reaches the distance threshold, only stopping upon reaching a {{ classLink("DynamicInstance") }} that isn't nested in ignoreList.

**Example**

```lua
local Ray = game["Environment"]:Raycast(barrel.Position, barrel.Forward, 25, {game["Environment"]["IgnoredInstances"], game["Environment"]["OtherIgnoredInstances"]})

if Ray ~= nil then
    local Hit = Ray.Instance -- Player
    if Hit:IsA("Player") then
        print("Hit",Hit,"at",Ray.Position,"!") -- [Hit Player at (3.24, 1.2, 5.93) !]
        Hit.Health = math.max(Hit.Health - 12 * (1.5-(1- Ray.Distance / 25)), 0)
        --Point blank deals 18 damage while max distance deals 6 damage
    end
end
```

<div data-search-exclude markdown>
!!! note "The descendants of an {{ classLink("Instance") }} in ignoreList are ignored too."
!!! warning "If the Raycast fails to hit a {{ classLink("DynamicInstance") }}, it is returned as nil."
</div>

### RaycastAll(origin;Vector3,direction;Vector3,?maxDistance;float=infinite,?ignoreList;array={Instance}):{RayResult} { method }

Casts a ray from origin, shooting in the given direction until it reaches the distance threshold, only returning a table of {{ classLink("DynamicInstance") }}s that aren't nested within the ignoreList.

**Example**

```lua
local Ray = game["Environment"]:RaycastAll(Vector3.New(0, 10, 0), Vector3.New(0, -1, 0), 100, game["Environment"]["Map"])

--We call this the Railgun.
for i, hit in pairs(Ray) do
    if hit.Instance:IsA("NPC") then
        if hit.Position.y - hit.Instance.Position.y >= hit.Instance.Size.y then
            hit.Instance.Health = 0 --An accurate headshot detection, no matter the size of the NPC
            --(hit.Instance.Position.y + hit.instance.Size.y == where the NPC's neck is on the y scale)
        else
            hit.Instance.Health = math.max(0, hit.Instance.Health - 50) --Body shot
        end
    end
end
```

### RebuildNavMesh(?root;Instance) { method }

Rebuilds the navigation mesh which determines the empty space where {{ classLink("NPC") }}s can pathfind in.

**Example**

```lua
game["Environment"]:RebuildNavMesh(game["Environment"]["Map"])
```

### GetPointOnNavMesh(position;Vector3,?maxDistance;float=infinite):Vector3 { method }

Returns a point on the navigation mesh at the given position.

## Properties

### AutoGenerateNavMesh:bool { property }

Determines whether or not to automatically build a navigation mesh from :polytoria-Environment: Environment for {{ classLink("NPC") }} pathfinding. This property is disabled by default so there are no performance issues with larger maps.

<div data-search-exclude markdown>
!!! warning "AutoGenerateNavMesh only runs once upon being set to true. Changing the map will still require you to run RebuildNavMesh."
</div>

### FogColor:Color { property }

The color of the fog. Fog is a visual effect that makes the world look like it is covered in a colored mist.

**Example**

Change the fog color to white:

```lua
game["Environment"].FogColor = Color.New(1, 1, 1, 1)
```

### FogEnabled:boolean { property }

Whether or not fog is enabled.

### FogStartDistance:float { property }

The distance from the {{ classLink("Camera") }} at which fog starts to appear

### FogEndDistance:float { property }

The distance from the {{ classLink("Camera") }} at which fog is fully opaque

### Gravity:Vector3=Vector3.New(0, -75, 0) { property }

The direction and strength of gravity in the world

### PartDestroyHeight:float { property }

The height at which unanchored parts are destroyed when they fall below it.

**Example**

```lua
game["Environment"].PartDestroyHeight = -2000
```

<div data-search-exclude markdown>
!!! note "PartDestroyHeight only kills {{ classLink("Players") }}, and destroys {{ classLink("DynamicInstance") }}s with Anchor set to false."
!!! warning "PartDestroyHeight may kill {{ classLink("Players") }}, but it does not kill {{ classLink("NPC") }}s."
</div>

### Skybox:SkyboxPreset { property }

The default skybox preset to use for the world, if no ImageSky is present.
