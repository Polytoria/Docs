# Loading

### Description

Determines whether the Datastore is currently loading or not.

Property of [Datastore](../../)

#### Type

`boolean`

### Example

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)
while ds.Loading do
	wait()
end
```
