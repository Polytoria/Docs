---
title: Camera
description: Camera is a class that represents the local player's camera.
icon: polytoria/Camera
weight: 4
---

# Camera

{{ service() }}

{{ notnewable() }}

{{ clientexclusive() }}

:polytoria-Camera: Camera is a class that represents the local player's camera.

{{ inherits("Instance") }}

## Properties

### Distance:float { property }

Determines the distance between the camera and the player when the camera is in `FollowPlayer` mode.

**Example**

```lua
Camera.Distance = 20
```

### FOV:float { property }

Determines or returns the camera's field of view.

**Example**

```lua
Camera.FOV = 90
```

### FastFlySpeed:float { property }

Determines the camera speed when the camera is in `FreeCam` mode while holding shift.

**Example**

```lua
Camera.FastFlySpeed = 100
```

### FlySpeed:float { property }

Determines the camera speed when the camera is in `FreeCam` mode.

**Example**

```lua
Camera.FlySpeed = 10
```

### FollowLerp:bool { property }

Determines whether or not to use lerping in `FollowPlayer` mode.

**Example**

```lua
Camera.FollowLerp = true
```

### FreeLookSensitivity:float { property }

Determines the mouse sensitivity while in `FreeCam` mode.

**Example**

```lua
Camera.FreeLookSensitivity = 3
```

### HorizontalSpeed:float { property }

Determines the horizontal movement speed of the camera in `FollowPlayer` mode.

**Example**

```lua
Camera.HorizontalSpeed = 120
```

### IsFirstPerson:bool { property }

Returns whether or not the camera is in first person.

**Example**

```lua
print(Camera.IsFirstPerson)
```

{{ readonly() }}

### LerpSpeed:float { property }

Determines the lerp speed of the camera when lerping is enabled.

**Example**

```lua
Camera.LerpSpeed = 15
```

### MaxDistance:float { property }

Determines camera's maximum distance from the player in `FollowPlayer` mode.

**Example**

```lua
Camera.MaxDistance = 0
```

### MinDistance:float { property }

The camera's minimum distance from the player in FollowPlayer mode.

**Example**

```lua
Camera.MinDistance = 5
```

### Mode:CameraMode { property }

Determines or returns the camera's current mode `(Scripted, FollowPlayer, Freecam)`.

**Example**

```lua
Camera.Mode = CameraMode.Scripted
```

### Orthographic:bool { property }

Determines whether or not the camera should render in orthographic (2D) mode or not (3D).

**Example**

```lua
Camera.Orthographic = true
```

### OrthographicSize:float { property }

Determines the half-size of the camera when in orthographic mode.

**Example**

```lua
Camera.OrthographicSize = 30
```

### Position:Vector3 { property }

Determines or returns position of the camera in the world.

**Example**

```lua
Camera.Position = Vector3.New(0, 100, 0)
```

### PositionOffset:Vector3 { property }

Determines the camera's offset from its position.

**Example**

```lua
-- Offsets the camera to be slightly above the player
Camera.PositionOffset = Vector3.New(0, 5, 0)
```

### Rotation:Vector3 { property }

Determines or returns rotation of the camera.

**Example**

```lua
Camera.Rotation = Vector3.New(90, 0, 0)
```

### RotationOffset:Vector3 { property }

Determines the camera's offset from its rotation.

**Example**

```lua
-- Offsets the camera to be slightly rotated
Camera.RotationOffset = Vector3.New(0, 5, 0)
```

### ScrollSensitivity:float { property }

Determines the scroll move speed of the camera.

**Example**

```lua
Camera.ScrollSensitivity = 15
```

### VerticalSpeed:float { property }

Determines the vertical move speed of the camera.

**Example**

```lua
Camera.VerticalSpeed = 120
```
