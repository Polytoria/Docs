# Chatted

### Description

Gets triggered when a player sends a chat message.

Event of [Player](/classes/Player/)

#### Returns

Message `string`

### Example

```lua
game["Players"]["willemsteller"].Chatted:Connect(function (message)
    print("Player wrote: " .. message)
end)
```
