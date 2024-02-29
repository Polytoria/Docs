---
title: Lighting
description: Lighting is responsible for controlling the state of the lighting in the place.
icon: polytoria/Lighting
weight: 3
---

# Lighting

{{ service() }}

{{ notnewable() }}

:polytoria-Lighting: Lighting is responsible for controlling the state of the lighting in the place. It provides many different options for creators to enhance and fine-tune the visuals of their worlds.

By parenting an [:polytoria-ImageSky: ImageSky](/objects/world/ImageSky) object to Lighting, you can change the skybox of the world.

{{ inherits("Instance") }}

## Properties

### AmbientColor:Color { property }

The color of the ambient light. Ambient light is light that is not coming from any particular direction, and is used to simulate light bouncing off of surfaces.

This property is only used if [:polytoria-Property: AmbientSource](#AmbientSource) is set to `AmbientSource.AmbientColor`.

### AmbientSource:AmbientSource { property }

The source of the ambient light

### SunBrightness:float { property }

The brightness of the sun

### SunColor:Color { property }

The color of the sun. This affects the color of the ambient lighting in the environment.

### Shadows:boolean { property }

Whether or not shadows are enabled
