# GetPlayers
### Description
Returns a list of all players.

Function of [Player](/classes/Player/)

#### Returns
Players `Array`

### Example
```lua
for i, p in pairs(game["Players"]:GetPlayers()) do
    print(p.Name)
end
```