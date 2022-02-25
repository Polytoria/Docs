# parse
### Description
Returns a table with the contents of the specified json string

Function of [json](../../)

#### Parameters
jsonString `string`  

#### Return type
`Table`

### Example
```lua
Http:Get("https://api.polytoria.com/v1/asset/owner?userID=1&assetID=234", function (data, error, errmsg)
    if error then
        print("Something went wrong!")
        return
    end
    
    print(json.parse(data)["Success"])
end)
```