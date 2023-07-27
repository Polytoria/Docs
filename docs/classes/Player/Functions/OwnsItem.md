# OwnsItem

### Description

Check whether a player owns an item or not.

Function of [Player](/classes/Player/)

#### Parameters

AssetID `number`
Callback `function (bool error, bool ownsItem)`

### Example

```lua
player:OwnsItem(11117, function(error, owns)
    if error then
        print("An error occurred!")
    else
        if owns then
            print("Player owns Blade of Spooks!")
        else
            print("Player does not own Blade of Spooks!")
        end
    end
end)
```

### Notes

- Results are cached for 5 minutes.
- A maximum of 30 requests per minute can be made per server.
