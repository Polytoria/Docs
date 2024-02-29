---
title: Tween
description: Tween is a static class used for tweening properties of instances, such as Position, Rotation and Size.
icon: polytoria/Tween
---

# Tween

{{ staticclass("Tween")}}

:polytoria-Tween: Tween is a static class used for tweening properties of instances, such as Position, Rotation and Size.

<div data-search-exclude markdown>
!!! note "Overlapping Tweens"
    Multiple tweens can be applied on the same object at the same time, but they must not be tweening the same property. Only the latest tween will override any other one being applied to the property.
</div>

## Methods

### TweenColor(startValue;Color,endValue;Color,time;number,callPerStep;function,type;TweenType,callback;function) { method }

Tweens a color between two specified values.

**Example**

```lua
Tween:TweenColor(Color.New(1,1,1,1), Color.New(1,1,1,0), 5, function(val)
    part.Color = val
end, TweenType.linear, function()
    print("Tween finished")
end
```

### TweenNumber(startValue;int,endValue;int,time;number,callPerStep;function,type;TweenType,callback;function) { method }

Tweens a number between two specified values.

**Example**

```lua
Tween:TweenNumber(1, 10, 1, function(val)
    print(val)
end, TweenType.linear, function()
    print("Tween finished")
end)
```

### TweenPosition(target;DynamicInstance,destination;Vector3,time;number,type;TweenType,callback;function) { method }

Tweens the position of a DynamicInstance

**Example**

```lua
Tween:TweenPosition(part, Vector3.New(100, 0, 0), 100, TweenType.linear, function()
    print("I have arrived!")
end)
```

### TweenRotation(target;DynamicInstance,destination;Vector3,time;number,type;TweenType,callback;function) { method }

Tweens the rotation of a DynamicInstance

<div data-search-exclude markdown>
!!! note "Rotation is in euler angles."
</div>

**Example**

```lua
Tween:TweenRotation(part, Vector3.New(0, 90, 0), 1, TweenType.linear, function()
    print("Rotating finished")
end)
```

### TweenSize(target;DynamicInstance,endValue;Vector3,time;number,type;TweenType,callback;function) { method }

Tweens the size of a DynamicInstance

**Example**

```lua
Tween:TweenSize(part, Vector3.New(5, 5, 5), 1, TweenType.linear, function()
    print("Sizing finished")
end)
```

### TweenVector2(startValue;Vector2,endValue;Vector2,time;int,callPerStep;function,type;TweenType,callback;function) { method }

Tweens a vector2 between two specified values.

**Example**

```lua
Tween:TweenVector2(Vector2.New(0,0), Vector2.New(0,50), 5, function(val)
    UIView.PositionOffset = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```

### TweenVector3(startValue;Vector3,endValue;Vector3,time;int,callPerStep;function,type;TweenType,callback;function) { method }

Tweens a vector3 between two specified values.

**Example**

```lua
Tween:TweenVector3(Vector3.New(0,0,0), Vector3.New(0,50,0), 5, function(val)
    part.Position = val
end, TweenType.linear, function()
    print("Tween finished")
end)
```
