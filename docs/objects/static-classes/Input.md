---
title: Input
description: Input is a class used for retrieving user input data, such as the mouse and keyboard.
icon: polytoria/Input
---

# Input

{{ staticclass("Input")}}

:polytoria-Input: Input is a class used for retrieving user input data, such as the mouse and keyboard.

## Events

### KeyDown(key;string) { event }

Fires when a key is pressed.

**Example**

```lua
Input.KeyDown:Connect(function (key)
    print(key .. " was pressed!")

    if key == "P" then
        print("The 'P' key was pressed!")
    end
end)
```

### KeyUp(key;string) { event }

Fires when a key is released.

```lua
Input.KeyUp:Connect(function (key)
    print(key .. " was pressed!")

    if key == "P" then
        print("The 'P' key was pressed!")
    end
end)
```

## Methods

<div data-search-exclude markdown>
!!! danger "Undocumented Methods"

    This section is a work in progress! The methods `GetMouseWorldPoint`, and `GetMouseWorldPosition`, are not written yet. Want to contribute? Go to the GitHub and open a pull request [here](https://github.com/Polytoria/Docs)!

</div>

### ScreenPointToRay(Vector3;pos, List ignoreList = null):RayResult { method }

Cast a ray from the camera at screen point into the game world


### ViewportPointToRay(Vector3;pos, List ignoreList = null):RayResult { method }

Cast a ray from the camera at the specified ViewportPoint (Vector3 with components with values in range of 0 - 1 describing how far a point is to to right and to the top of the screen) into the game world

### ScreenToViewportPoint(screenPosition;Vector3):Vector3 { method }

Transforms `screenPosition` parameter from screen space into viewport space.

### ScreenToWorldPoint(screenPosition;Vector3):Vector3 { method }

Transforms `screenPosition` from screen space into world space.

<div data-search-exclude markdown>
!!! note "World space coordinates can still be calculated even when provided as an off-screen coordinate."
</div>

### ViewportToScreenPoint(viewportPosition;Vector3):Vector3 { method }

Transforms `viewportPosition` from viewport space into screen space.

### ViewportToWorldPoint(viewportPosition;Vector3):Vector3 { method }

Transforms `viewportPosition` from viewport space into world space.

<div data-search-exclude markdown>
!!! note "ViewportToWorldPoint transforms an x-y screen position into a x-y-z position in 3D space."
</div>

### WorldToScreenPoint(worldPosition;Vector3):Vector3 { method }

Transforms `worldPosition` from world space into screen space.

### WorldToViewportPoint(worldPosition;Vector3):Vector3 { method }

Transforms `worldPosition` from world space into viewport space.

## Properties

### MousePosition:Vector2 { property }

Returns the current mouse position.

### CursorLocked:bool { property }

Determines whether or not the cursor is locked.

**Example**

```lua
Input.CursorLocked = true
```

### CursorVisible:bool { property }

Determines whether or not the cursor is visible.

**Example**

```lua
Input.CursorVisible = true
```
