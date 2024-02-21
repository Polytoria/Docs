# HasAchievement

### Description

Awards the specified player the specified achievement.

Function of [Achievements](../../)

#### Parameters

userId `number`

achievementId `number`

callback `function`

### Example

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

The callback function has the parameters `hasAchievement`, if the player has the achievement, `success`, if the lookup succeeded and `error`, which contains the error message if the lookup failed.
