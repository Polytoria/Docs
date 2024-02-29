---
title: Modifying Object Properties
description: Learn to modify object properties.
weight: 3
---

# Modifying Object Properties

Modifying object properties is a vital part of scripting, as it allows you to manipulate objects.

To get and set properties, you need a reference to the object itself.

To access a property, you may use the dot notation.

Example:

```lua
game["Environment"]["myPart"].Position
```

<i>Tip: To see a list of properties, that the object may have, you can view its documentation or look at its properties below the Explorer.</i>

That alone will already return the value of the property. Although nothing is being done with it.
You may use something like `print()` to print out the value to the console.

Example:

```lua
print(game["Environment"]["myPart"].Position)
```

To set the property, you may do it how you would set variables.

Example:

```lua
game["Environment"]["myPart"].Position = Vector3.New(10,10,10)
```

There are certain properties that can't be changed:

```lua
-- Will error, the property 'ClassName' is read-only.
game["Environment"]["myPart"].ClassName = "StringValue"
```

<i>Tip: To see which properties are read-only, you may look them up in the Documentation.</i>

Changing the `Name` and `Parent` properties, which every object has, will affect how you access that object in the script. Changing the `Name` property renames the object and changing the `Parent` will move the object to a new Parent in the place structure.

Example using `Name`:

```lua
-- myPart gets renamed to epicPart
game["Environment"]["myPart"].Name = "epicPart"

-- You can no longer access that part using game["Environment"]["myPart"], as its name changed.
print(game["Environment"]["epicPart"].Name) -- Prints out "epicPart"
```

Example using `Parent`:

```lua
-- myPart gets reparented to game["Hidden"]
game["Environment"]["myPart"].Parent = game["Hidden"]

-- You can no longer access that part using game["Environment"]["myPart"], as its parent, and thus its location in the place structure, changed.
print(game["Hidden"]["myPart"].Parent.Name) -- Prints out "Hidden"
```

References to object will not be lost, despite the object being renamed and moved to new parents:

```lua
local myPart = game["Environment"]["myPart"]

myPart.Name = "The Part"

-- We can still access the same object using the variable, despite it changing names.
print(myPart.Name) -- Prints out "The Part"


myPart.Parent = game["ScriptService"]

-- We can also still access the same object using the variable, despite it being reparented.
print(myPart.Parent.Name) -- Prints out "ScriptService"
```
