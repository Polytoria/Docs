---
title: BodyPosition
description: BodyPosition are objects that apply a force to their parent until it moves toward the target position.

icon: polytoria/BodyPosition
---

# BodyPosition

:polytoria-BodyPosition: BodyPosition are objects that apply a force to their parent until it moves toward the target position.

{{ inherits("Instance") }}

## Properties

### AcceptanceDistance:float { property }

Determines how close the body has to be to the target position to stop applying forces to it.

**Example**

```lua
bodyPosition.AcceptanceDistance = 5
```

### Force:float { property }

Determines how much force the body applies.

**Example**

```lua
bodyPosition.Force = 100
```

### TargetPosition:Vector3 { property }

Determines the target position that the body applies forces to get to.

**Example**

```lua
bodyPosition.TargetPosition = Vector3.New(0, 50, 0)
```
