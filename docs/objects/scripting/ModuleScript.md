---
title: ModuleScript
description: ModuleScripts are specialized scripts to hold data that can be accessed by other scripts using the `require()` function.
icon: polytoria/ModuleScript
weight: 3
---

# ModuleScript

<div data-search-exclude markdown>
!!! bug "BETA Feature"

    ModuleScripts are currently in BETA. As of right now, you aren't able to run functions from ModuleScripts. However this is a planned feature in the near future.

</div>

:polytoria-ModuleScript: ModuleScripts are specialized scripts to hold data that can be accessed by other scripts using the `require()` function.

It is important to define and return a table in a ModuleScript. When the place starts, the server and the client will run the ModuleScript once and store the result for other scripts to retrieve with `require()`.

<div data-search-exclude markdown>
!!! note "When trying to require a specific module script, put the path to the ModuleScript in the require function."
</div>

{{ inherits("BaseScript") }}

**Example**

ModuleScript named `Structures` located in `game["ScriptService"]`

```lua
local Structures = {
    ["Tower"] = {
        ["Description"] = "This tower will obliterate any enemies on the way to the castle!",
        ["Price"] = 95,
        ["AttackDamage"] = 5
    }
}

-- Make sure to return the table to be able to access it in other scripts!
return Structures
```

In a Script/LocalScript:

```lua
wait(0.1) -- The ModuleScript might only start running after this Script/LocalScript began running and thus this wait() is necessary
local Structures = require(game["ScriptService"]["Structures"])

print(Structures["Tower"]["Description"]) -- Prints out "This tower will obliterate any enemies on the way to the castle!" like how it was defined in the ModuleScript above.
```
