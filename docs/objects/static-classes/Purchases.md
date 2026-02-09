---
title: Purchases
description: Purchases is a static class, that is used to prompt purchases to a player.
icon: polytoria/Purchases
---

# Purchases

{{ staticclass("Purchases") }}

{{ serverexclusive() }}

:polytoria-Purchases: Purchases is a static class, that is used to prompt purchases to a player.

<div data-search-exclude markdown>
!!! note "Purchases is not fully documented yet, and may receive changes."
</div>

## Methods

### Prompt(player;Player,itemID;int,callback;function):callback { method }

Prompts the specified player the specified item.

**Example**

```lua
game["Players"].PlayerAdded:Connect(function(plr)
    wait(2)
    Purchases:Prompt(plr, 86803, function(success, error)
        if success then
            print("Thank you for your purchase!")
        else
            print("Something went wrong with your purchase: " .. error)
        end
    end)
end)
```

The callback function has the parameter "success", indicating if the prompt was purchased, declined, or an error occurred. The callback function's "error" parameter contains the error message if the prompt failed.