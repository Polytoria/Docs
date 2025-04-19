---
title: Sound
description: Sounds are objects that can be placed in the world and emit audio.
icon: polytoria/Sound
weight: 2
---

# Sound

:polytoria-Sound: Sounds are objects that can be placed in the world and emit audio.

{{ inherits("DynamicInstance") }}

## Events

### Loaded { event }

The event that is fired when the sound is loaded from the server.

**Example**

```lua
sound.Loaded:Connect(function()
    sound.Play()
end)
```

## Methods

### Play:void { method }

Plays the sound.

### PlayOneShot(volume;float):void { method }

Plays the sound once, able to be ran in rapid succession without stopping existing playback.

### Stop:void { method }

Stops playing the sound.

## Properties

### Autoplay:bool { property }

Determines whether the sound should start playing automatically.

### Loading:bool { property }

Returns whether or not the sound is loading or not.

{{ readonly() }}

### Length:float { property }

Returns the length of the currently loaded audio.

{{ readonly() }}

### Loop:bool { property }

Determines whether the sound should loop or not.

### Pitch:float { property }

The pitch of the sound.

### PlayInWorld:bool { property }

When enabled, the sound will be played in 3D world space rather than having the same volume for everyone.

### MaxDistance:float { property }

Specifies how far the player must be from the sound for it to stop playing, if the `PlayInWorld` property is set to true.

### Playing:bool { property }

Determines whether the sound is currently playing or not.

{{ readonly() }}

### SoundID:string { property }

The asset ID of the sound.

### Time:float { property }

The time position the track is currently on.

### Volume:float { property }

The volume of the sound.
