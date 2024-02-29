---
title: UI
description: UI was a static class used for creating User Interface elements through LocalScripts. Removed in v1.2.0.
icon: polytoria/UI
---

# (Removed) UI

<div data-search-exclude markdown>
!!! danger "Removed"
    The UI static class was removed in Version 1.2.0, and is currently noted for documentation purposes. It is not recommended, if possible, to use in recent versions.
</div>

{{ staticclass("UI")}}

UI was a static class used for creating User Interface elements through LocalScripts. While it is possible to create UI elements in normal scripts, it will only work in local playtesting and not on server.

## Methods

### CreateButton:UIButton { method }

Creates a GUI Button

**Example**

```lua
local button = UI:CreateButton()
button.Size = Vector2.New(200,100)
button:ApplyAnchorPreset(AnchorPreset.Center)
```

### CreateEmpty:UIField { method }

Creates an empty UIField

**Example**

```lua
local empty = UI:CreateEmpty()
```

### CreateImage:UIImage { method }

Creates an UI image.

**Example**

```lua
local image = UI:CreateImage()
image.ImageID = 12384
image.ApplyAnchorPreset(AnchorPreset.Center)
image.Size = Vector2.New(200,200)
```

### CreateLabel(text;string):UILabel { method }

Creates a text label.

**Example**

```lua
local text = UI:CreateLabel()
text.ApplyAnchorPreset(AnchorPreset.Center)
text.Size = Vector2.New(200, 32)
text.Text = "Hello, world!"
```

### CreateHorizontalLayout:UIHorizontalLayout { method }

Creates a horizontal UI layout.

**Example**

```lua
local layout = UI:CreateHorizontalLayout()
```

### CreateVerticalLayout:UIVerticalLayout { method }

Creates a horizontal UI layout.

**Example**

```lua
local layout = UI:CreateVerticalLayout()
```

## Properties

### ScreenHeight:int { property }

Get current user's screen height

**Example**

```lua
local Background = UI:CreateImage()
Background.ImageID = 12384
Background.ApplyAnchorPreset(AnchorPreset.Center)
Background.Size = Vector2.New(UI.ScreenWidth,UI.ScreenHeight)
```

### ScreenWidth:int { property }

Get current user's screen width

**Example**

```lua
local Background = UI:CreateImage()
Background.ImageID = 12384
Background.ApplyAnchorPreset(AnchorPreset.Center)
Background.Size = Vector2.New(UI.ScreenWidth,UI.ScreenHeight)
```
