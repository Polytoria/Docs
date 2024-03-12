---
title: RemoteEvent
description: RemoteEvents was events that can be called by clients to send data to the server.
icon: polytoria/NetworkEvent
---

# (Removed) RemoteEvent

<div data-search-exclude markdown>
!!! danger "Removed"
    The RemoteEvent class was removed in a previous version of Polytoria, and is currently noted for documentation purposes.
    
</div>

RemoteEvents was events that could be called by clients to send data to the server.

<div data-search-exclude markdown>
!!! note "RemoteEvents only supported one parameter due to networking limitations."
</div>

## Events

### Invoked:Player { event }

Fires when the Invoke function is called.

<div data-search-exclude markdown>
!!! tip "This event had the ability to return paramaters `Player` or `object`"
</div>

**Example**

```lua
event.Invoked:Connect(function(player, value)
    print("Received value "..value.." from "..player.Name)
end)
```

## Methods

### Invoke(object) { method }

Invokes the event. Can only be called from client.

**Example**

```lua
event.Invoke(Vector3.New(0, 100, 0))
```
