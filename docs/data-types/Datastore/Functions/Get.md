# Get

### Description

Gets the value of a key in the datastore.

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

ds:Get("Coins", function(value, success, error)
	if not success then
		print(error)
	else
		print(player.Name .. " has " .. value .. " coins.")
	end
end)
```
