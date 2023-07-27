# InvokeClient

### Description

Sends a NetMessage from the server to a specific player. Can only be called from server.

Function of [NetworkEvent](/classes/NetworkEvent/)

#### Parameters

message `NetMessage`

player `Player`

#### Returns

`void`

### Example

```lua
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeClient(message, game["Players"]["willemsteller"])
```
