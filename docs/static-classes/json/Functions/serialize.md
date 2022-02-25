# serialize
### Description
Returns a json string with the contents of the specified table.

Function of [json](../../)

#### Parameters
table `Table`  

#### Return type
`string`

### Example
```lua
print(json.serialize({
    Name: "Cool Sword",
    Damage: 10,
}))
```