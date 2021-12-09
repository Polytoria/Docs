# GetPlayers
### Description
Returns a list of all players.

Function of [Players](/classes/Players/)

#### Return type
`Player[]`

### Example
```lua
for i, p in pairs(game["Players"]:GetPlayers()) do
    print(p.Name)
end
```