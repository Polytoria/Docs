---
title: Achievements
description: Achivements is a static class, that is used to award place achivements to a player.
icon: polytoria/Achievements
---

# Achievements

{{ staticclass("Achievements") }}

{{ serverexclusive() }}

:polytoria-Achievements: Achievements is a static class, that is used to award place achievements to a player.

## Methods

### Award(playerUserID;number,achievementID;number,callback;function):callback { method }

Awards the specified player the specified achievement.

**Example**

```lua
game["Players"].PlayerAdded:Connect(function(plr)
    wait(2)
    Achievements:Award(plr.UserID, 31472, function(success, error)
        if success then
            print("Awarded achievement")
        else
            print("Error awarding achievement: " .. error)
        end
    end)
end)
```

The callback function has the parameters "success", indicating if the award succeded, and "error", which contains the error message if the award failed.

### HasAchievement(playerUserID;number,achievementID;number,callback;function):callback { method }

Check if the specified player has the specified achievement.

**Example**

```lua
game["Players"].PlayerAdded:Connect(function(plr)
    wait(2)
    Achievements:HasAchievement(plr.UserID, 31472, function(hasAchievement, success, error)
        if success then
            if hasAchievement then
                print(player.Name .. "has the achievement!")
            else
                print(player.Name .. "doesn't have the achievement :(")
            end
        else
            print("Error checking for achievement obtainability: " .. error)
        end
    end)
end)
```

The callback function has the parameters "hasAchievement", if the player has the achievement, "success", if the lookup succeeded and "error", which contains the error message if the lookup failed.
