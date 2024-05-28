---
title: Scripting difference between Roblox and Polytoria
description: Guide on the main differences between Roblox and Polytoria related to scripting.
weight: 4
---

# Main scripting differences between Roblox and Polytoria

This page will explain everything you need to know before scripting in Polytoria.

## Finding Objects

In Roblox, is very common to use dots to find objects
```lua
local block = game.Workspace.Part
```
But here, we use brackets instead of dots. So the example i used above would be something like this
```lua
local block = game["Environment"]["Part"]
```
## Callback Methods

Polytoria scripting uses mostly callback methods instead of :Wait() or yeld. Let's use [TweenService](https://docs.polytoria.com/objects/static-classes/Tween/) as an example, in Roblox you need to wait until the tween ends, you could use Tween:Wait() but you need to put the function in callback.
```lua
-- Roblox

local tween1 = TweenService:Create(part, tweenInfo, {Position = Vector3.new(0, 10, 20)})
tween:Play()
tween.Completed:Wait()
print("I have arrived!")

-- Polytoria

Tween:TweenPosition(part, Vector3.New(0, 10, 20), 100, TweenType.linear, function()
print("I have arrived!")
end)

```

## Enums

In Polytoria, you don't need to call "Enum.X" to find an Enum, you can just type it's name.
```lua
-- Roblox

Enum.EasingStyle.Exponential

-- Polytoria:

TweenType.easeOutExpo
```

## InputKeyDown doesn't give you interrupt state

In Roblox, we mostly use "`UserInputService.InputBegan`" to see if the key is being pressed or not, it do return the key that us being pressed. But for Polytoria, the event will not return you the interrupt state. The event will not fire if the Chat or any of the CoreGUIs[^1] are open.

## Polytoria uses Static Classes instead of services

In Roblox, we mostly call functions from services using `game:GetService("TweenService")`. But in Polytoria there will be static classes accessible from all scripts. You don't have to store them in variables, but be careful to not name the variable the same thing as an static class.
```lua
-- Roblox:

local tweenService = game:GetService("TweenService")

-- Polytoria:

local tweenService = Tween
```

[^1]: Main Menu and other client menus in general.
