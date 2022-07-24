# InvokeServer

### Description

Sends a NetMessage from the client to the server. Can only be called from client.

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
netEvent.InvokeServer(message)
```
