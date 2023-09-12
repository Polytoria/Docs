# Invoked

<div class="alert alert-danger">Replaced with <a href="https://docs.polytoria.com/classes/NetworkEvent/">Network Events</a></div>

### Description

Fires when the Invoke function is called.

Event of [RemoteEvent](/classes/RemoteEvent/)

#### Returns

Parameter `Player`
Parameter `object`

### Example

```lua
event.Invoked:Connect(function(player, value)
    print("Received value "..value.." from "..player.Name)
end)
```
