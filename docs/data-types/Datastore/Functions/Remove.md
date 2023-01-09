# Remove

### Description

Removes a value from the datastore.

Function of [Datastore](../../)

#### Parameters

key `string`

callback `function`

### Example

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)

while ds.Loading do
	wait()
end

ds:Remove("Coins", function(success, error)
	if not success then
		print(error)
	else
		print(player.Name .. "'s coins have been removed!")
	end
end)
```
