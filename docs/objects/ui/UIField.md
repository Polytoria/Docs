---
title: UIField
description: UIField is the base class of all UI classes.
icon: polytoria/UIField
weight: 100
---

# UIField

:polytoria-UIField: UIField is the base class of all UI classes.

{{ abstract() }}

{{ inherits("Instance") }}

## Events

### MouseDown { event }

Fires when the mouse is clicked

**Example**

```lua
label.MouseDown:Connect(function()
    label.Text = "Mouse Down"
end)
```

### MouseUp { event }

Fires when the mouse is released

**Example**

```lua
label.MouseUp:Connect(function()
    label.Text = "Mouse Up"
end)
```

## Properties

### PivotPoint:Vector2 = Vector2.New(0.5, 0.5) { property }

The pivot point of the UI element.

### PositionOffset:Vector2 = Vector2.New(100, 100) { property }

The offset of the UI element in pixels.

### PositionRelative:Vector2 = Vector2.New(0.5, 0.5) { property }

The position of the UI element relative to its parent.

### Rotation:float { property }

The rotation of the UI element.

### SizeOffset:Vector2 = Vector2.New(100, 100) { property }

The size of the UI element in pixels.

### SizeRelative:Vector2 = Vector2.New(1, 1) { property }

The size of the UI element relative to its parent.

### Visible:bool { property }

Determines whether the UI element is visible or not.

### ClipDescendants:bool { property }

Determines whether the UI element clips its descendants.
