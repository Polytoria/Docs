# Award

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
    Achievements:Award(plr.UserID, 31472, function(success, error)
        if success then
            print("Awarded achievement")
        else
            print("Error awarding achievement: " .. error)
        end
    end)
end)
```
