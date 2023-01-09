# GetDatastore

### Description

Gets a Datastore object from the Datastore service.

Function of [Datastore](../../)

#### Parameters

key `string`

### Example

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)

while ds.Loading do
	wait()
end

ds:Get("Coins", function(value, success, error)
	if not success then
		print(error)
	else
		print(player.Name .. " has " .. value .. " coins.")
	end
end)
```
