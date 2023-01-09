# Set

### Description

Sets the value of a key in the Datastore.

Function of [Datastore](../../)

#### Parameters

key `string`

value `any`

callback `function`

### Example

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)

while ds.Loading do
	wait()
end

ds:Set("Coins", 100, function(success, error)
	if not success then
		print(error)
	else
		print(player.Name .. "'s coins have been set to 100!")
	end
end)
```
