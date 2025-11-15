---
title: Tool
description: Tools are objects that can be held by players.

icon: polytoria/Tool
weight: 7
---

# Tool

:polytoria-Tool: Tools are objects that can be held by players.

{{ inherits("DynamicInstance") }}

<div data-search-exclude markdown>
!!! warning "{{ classLink("BaseScript") }}s that are descendants of Tools won't run until after the Tool's first Equipped Event."
</div>

## Events

### Activated { event }

Fires when the user clicks while holding the tool.

**Example**

```lua
tool.Activated:Connect(function()
    print("Tool has been activated!")
end)
```

### Deactivated { event }

Gets fired when the user lets go of the mouse button while holding the tool.

### Equipped { event }

Fired when the tool is equipped.

### Unequipped { event }

Fired when the tool is unequipped.

## Methods

### Play(animationName;string) { method }

Plays an animation on the tool or the player that is currently holding the tool.

**Example**

```lua
local tool = script.Parent

tool.Activated:Connect(function()
    tool:Play("slash")
end)
```

<div data-search-exclude markdown>
!!! tip "You can use the following emotes on these tools: `slash`, `eat`, and `drink`."
</div>

## Properties

### Droppable:bool { property }

Determines whether the tool can be dropped by the player or not.

**Example**

```lua
tool.Droppable = true
```
