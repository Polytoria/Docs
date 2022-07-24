# Shadows

### Description

Specifies whether this light emits shadows or not.

Property of [PointLight](/classes/PointLight/)

#### Type

`boolean`

### Example

```lua
light.Shadows = true
```

### Notes

- Having many lights with shadows enabled will cause a massive hit in performance. Consider minimzing the amount of lights with shadows to ensure every player is enjoying your game with minimal framerate issues.
