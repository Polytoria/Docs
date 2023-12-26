# InvokedServer

### Description

Gets invoked on the server when a client sends a message.

Event of [NetworkEvent](/classes/NetworkEvent/)

#### Returns

Sender `Player`
Message `NetMessage`

### Example

```lua
netEvent.InvokedServer:Connect(function (sender, message)
    local value = message.GetString("key")
end)
```
