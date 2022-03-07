# InvokedClient
### Description
Gets invoked on the client when the server sends a message.

Event of [NetworkEvent](/classes/NetworkEvent/)

#### Returns
Sender `nil`
Message `NetMessage`

### Example
```lua
netEvent.InvokedClient:Connect(function (sender, message)
    local value = message:GetString("key")
end)
```
