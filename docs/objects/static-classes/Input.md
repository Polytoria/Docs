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

    This section is a work in progress! The method `GetMouseWorldPoint` is not written yet. Want to contribute? Go to the GitHub and open a pull request [here](https://github.com/Polytoria/Docs)!

</div>

### GetAxis(axisName;string):float { method }

Returns the value of the specified axis.

### GetAxisRaw(axisName;string):float { method }

Returns the value of the specified axis without smoothing filtering.

### GetButton(buttonName;string):bool { method }

Returns `true` if the specified button is being held down.

### GetButtonDown(buttonName;string):bool { method }

Returns `true` during the frame in which the specified button was pressed.

### GetButtonUp(buttonName;string):bool { method }

Returns `true` during the frame in which the specified button was released.

### GetKey(keyName;string):bool { method }

Returns `true` if the specified key is being held down.

### GetKeyDown(keyName;string):bool { method }

Returns `true` during the frame in which the specified key was pressed.

### GetKeyUp(keyName;string):bool { method }

Returns `true` during the frame in which the specified key was released.

### GetMouseButton(mouseButton;int):bool { method }

Returns `true` if the specified mouse button is being held down.

### GetMouseButtonDown(mouseButton;int):bool { method }

Returns `true` during the frame in which the specified mouse button was pressed.

### GetMouseButtonUp(mouseButton;int):bool { method }

Returns `true` during the frame in which the specified mouse button was released.

### GetMouseWorldPosition:Vector3 { method }

Returns the 3D world-space position corresponding to the current mouse cursor location.

### ScreenPointToRay(position;Vector3, List ignoreList = null):RayResult { method }

Cast a ray from the camera at screen point into the game world

### ViewportPointToRay(position;Vector3, List ignoreList = null):RayResult { method }

Cast a ray from the camera at the specified ViewportPoint (Vector3 with components with values in range of 0 - 1 describing how far a point is to to right and to the top of the screen) into the game world

### ScreenToViewportPoint(screenPosition;Vector3):Vector3 { method }

Transforms `screenPosition` parameter from screen space into viewport space.

### ScreenToWorldPoint(screenPosition;Vector2):Vector3 { method }

Transforms `screenPosition` from screen space into world space.

<div data-search-exclude markdown>
!!! note "World space coordinates can still be calculated even when provided as an off-screen coordinate."
</div>

### ViewportToScreenPoint(viewportPosition;Vector2):Vector3 { method }

Transforms `viewportPosition` from viewport space into screen space.

### ViewportToWorldPoint(viewportPosition;Vector2):Vector3 { method }

Transforms `viewportPosition` from viewport space into world space.

<div data-search-exclude markdown>
!!! note "ViewportToWorldPoint transforms an x-y screen position into a x-y-z position in 3D space."
</div>

### WorldToScreenPoint(worldPosition;Vector3):Vector3 { method }

Transforms `worldPosition` from world space into screen space.

### WorldToViewportPoint(worldPosition;Vector3):Vector3 { method }

Transforms `worldPosition` from world space into viewport space.

## Properties

### AnyKey:bool { property }

Returns `true` if any key is being pressed.

### AnyKeyDown:bool { property }

Returns `true` if any new key presses happened during the current frame. Held down key presses from previous frames do not count.

### IsInputFocused:bool { property }

Determines whether or not the local player is currently focused on an input.

{{ readonly() }}

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

### ScreenWidth:float { property }

Returns the current screen's width.

{{ readonly() }}

### ScreenHeight:float { property }

Returns the current screen's height.

{{ readonly() }}
