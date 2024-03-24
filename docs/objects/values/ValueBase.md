---
title: ValueBase
description: Base class of all value classes.
icon: polytoria/ValueBase
weight: 20
---

# ValueBase

{{ ambiguousMultiple([["BoolValue", "used for storing bool values."], ["ColorValue", "used for storing color values."], ["InstanceValue", "used for storing instances."], ["IntValue", "used for storing integer values."], ["NumberValue", "used for storing number values."], ["StringValue", "used for storing string values."], ["Vector3Value", "used for storing Vector3 values."]])}}

Base class of all value classes.

{{ abstract() }}

{{ inherits("Instance") }}

## Events

### Changed { event }

Fires when the value of the ValueBase changes.

**Example**

```lua
boolValue.Changed:Connect(function()
    print("My new value is " .. boolValue.Value)
end)
```
