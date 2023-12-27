# parse

### Description

Returns a table with the contents of the specified JSON string

Function of [json](../../)

#### Parameters

value `string`

#### Returns

`Table`

### Example

```lua
Http:Get("https://api.polytoria.com/v1/store/25272", function (data, error, errmsg)
    if error then
        print("Something went wrong!")
        return
    end

    print(json.parse(data)["Success"])
end)
```
