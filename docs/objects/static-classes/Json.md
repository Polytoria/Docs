---
title: json
description: json is a module which allows for scripts to interface with JSON data representation by converting it to a table and vice versa.
icon: polytoria/json
---

# json

{{ staticclass("json")}}

:polytoria-json: json is a module which allows for scripts to interface with JSON data representation by converting it to a table and vice versa.

## Methods

### isNull(jsonString;string):bool { method }

Returns true if the value specified is a null read from a json string

**Example**

```lua
print(json.isNull("{}"))
```

### null:string { method }

Returns a special value which is a representation of a null in a json

**Example**

```lua
print(json.null())
```

### parse(jsonString;string):Table { method }

Returns a table with the contents of the specified JSON string

**Example**

```lua
Http:Get("https://api.polytoria.com/v1/asset/owner?userID=1&assetID=234", function (data, error, errmsg)
    if error then
        print("Something went wrong!")
        return
    end

    print(json.parse(data)["Success"])
end)
```

### serialize(array;array):string { method }

Returns a json string with the contents of the specified table.

**Example**

```lua
print(json.serialize({
    Name = "Cool Sword",
    Damage = 10,
}))
```
