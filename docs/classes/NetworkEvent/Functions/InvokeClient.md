# InvokeClient

### Description

Sends a NetMessage from the server to a specific player. Can only be called from server.

Function of [NetworkEvent](/classes/NetworkEvent/)

#### Parameters

msg `NetMessage`
player `Player`

#### Return type

`Void`

### Example

```lua
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeClient(message, game["Players"]["willemsteller"])
```
