---
title: Accessing Objects in a Script
description: Learn to access objects in a Script.
weight: 2
---

# Accessing Objects in a Script

To interact with the world using a script, you must be able to access objects to modify their properties, call their functions or connect code to an event.

You may access objects in the world like how you would access children of a table.
Every object is a descendant of `game`. To help you understand this, you may look at the Explorer, which has every object listed in the way it needs to be accessed using code.

If you have multiple objects with the same name under the same parent, the script will use the first object it finds with that name.
Additionally, you may use :FindChild(`instance name here`) as well.

Example:

```lua
game["Environment"]["myPart"]
game["Environment"]:FindChild("myPart")
```

`Environment` is a child of `game` and `myPart` is a child of `Environment`.

You may use variables to hold references to objects.

```lua
local myPart = game["Environment"]["myPart"]
```

You may store references to objects in tables.

```lua
local parts = {
    game["Environment"]["myPart"],
    game["Environment"]["Index's Epic Tool"],
    game["Environment"]["Baggy Man Light"],
    game["Environment"]:FindChild("Diving for Treasure Text3D")
}
```

Accessing a child of an object that doesn't exist results in an error:

```lua
-- Will error: "Cannot index nil"
game["Environment"]["Non-existant Object"]["myPart2"]
```

Accessing a non-existant child of an object will not error instantly, but further use cases might do:

```lua
local part = game["Environment"]["Existing Model"]["Non existing Part"]

-- Will error: "Cannot index nil"
local light = part["Light source"]

-- Will error: "Cannot index nil"
local price = part:FindChild("PriceValue")
```

Accessing a non-existant child of an object will return `nil`, which we can use to check if an object exists:

```lua
if game["Environment"]["myPart"] ~= nil then
    print("myPart exists!")
end

-- :FindChild() returns nil if no objects are found
if game["Environment"]:FindChild("my second Part") == nil then
    print("my second Part doesn't exist!")
end
```

View [Modifying Object Properties](/tutorials/basic-scripting/modifying-object-properties/) to find out how to modify object properties.
