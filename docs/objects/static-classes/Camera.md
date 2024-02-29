---
title: Camera
description: Camera is a class that represents the local player's camera.
icon: polytoria/Camera
---

# Camera

{{ staticclass("Camera") }}

{{ clientexclusive() }}

{{ notnewable() }}

:polytoria-Camera: Camera is a class that represents the local player's camera.

{{ inherits("Instance") }}

## Properties

### Distance:int { property }

The distance between the camera and the player when the camera is in FollowPlayer mode.

**Example**

```lua
Camera.Distance = 20
```

### FOV:int { property }

Sets or return the camera's field of view.

**Example**

```lua
Camera.FOV = 90
```

### FastFlySpeed:int { property }

The camera speed when the camera is in FreeCam mode while holding shift.

**Example**

```lua
Camera.FastFlySpeed = 100
```

### FlySpeed:int { property }

The camera speed when the camera is in FreeCam mode.

**Example**

```lua
Camera.FlySpeed = 10
```

### FollowLerp:bool { property }

Determines whether or not to use lerping in FollowPlayer mode.

**Example**

```lua
Camera.FollowLerp = true
```

### FreeLookSensitivity:int { property }

The mouse sensitivity while in FreeCam mode.

**Example**

```lua
Camera.FreeLookSensitivity = 3
```

### HorizontalSpeed:int { property }

The horizontal movement speed of the camera in FollowPlayer mode.

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

### LerpSpeed:int { property }

The lerp speed of the camera when lerping is enabled.

**Example**

```lua
Camera.LerpSpeed = 15
```

### MaxDistance:int { property }

The camera's maximum distance from the player in FollowPlayer mode.

**Example**

```lua
Camera.MaxDistance = 0
```

### MinDistance:int { property }

The camera's minimum distance from the player in FollowPlayer mode.

**Example**

```lua
Camera.MinDistance = 5
```

### Mode:CameraMode { property }

Sets or returns the camera's current mode.

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

### OrthographicSize:int { property }

Determines the half-size of the camera when in orthographic mode.

**Example**

```lua
Camera.OrthographicSize = 30
```

### Position:Vector3 { property }

The position of the camera in the world.

**Example**

```lua
Camera.Position = Vector3.New(0, 100, 0)
```

### Rotation:Vector3 { property }

The rotation of the camera.

**Example**

```lua
Camera.Rotation = Vector3.New(90, 0, 0)
```

### ScrollSensitivity:int { property }

Determines the scroll move speed of the camera.

**Example**

```lua
Camera.ScrollSensitivity = 15
```

### VerticalSpeed:int { property }

Determines the vertical move speed of the camera.

**Example**

```lua
Camera.VerticalSpeed = 120
```
