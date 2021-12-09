# UnicastMessage
### Description
Sends a system message in the chat to a specific user.

Function of [Game](/classes/Game/)

#### Parameters
Message `String`
Player `Player`

#### Return type
`Void`

### Example
```lua
game["Players"].PlayerAdded:Connect(function (plr)
    game:UnicastMessage("Welcome to the server, " .. plr.Name .. "!", plr)
end)
```