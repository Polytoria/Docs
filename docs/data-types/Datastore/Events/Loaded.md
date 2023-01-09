# Loaded

### Description

Gets triggered when the Datastore has finished loading.

Event of [Datastore](/data-types/Datastore/)

### Example

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)
ds.Loaded:Connect(function ()
	ds:Set("Coins", 100)
end)
```

### Notes
If a datastore is already loaded, for example in another script, the event will not be fired. It is recommended to check the [Loading](../Properties/Loading) property before connecting to the event. Alternatively, you can use a while loop and a wait function to wait for the datastore to load:

```lua
local ds = Datastore:GetDatastore("Player_" .. player.UserID)
while ds.Loading do
	wait()
end
```