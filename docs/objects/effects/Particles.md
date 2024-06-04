---
title: Particles
description: Particles are objects, that spawn and render particles in the world.
icon: polytoria/Unknown
---

# Particles

:polytoria-Unknown: Particles are objects, that spawn and render particles in the world.

{{ inherits("DynamicInstance") }}

## Methods

### Play { method }

Starts the emission of the particles from this object.

### Pause { method }

Pauses the emission of the particles from this object.

### Stop { method }

Stops the emission of the particles from this object.

### Clear { method }

Clears all currently emitted particles.

### Emit(count;int) { method }

Emits the specified amount of particles immediately.

### Simulate(time;float) { method }

Simulates the particles object for the specified time. This includes all physics, emission, etc.

## Properties

### ImageID:int { property }

Specifies the image asset ID that the particles will use.

### ImageType:ImageType { property }

The image type of the specified image id.

### Color:ColorRange { property }

The color of the particles, over the lifetime of the particle.

### ColorMode:ParticleColorMode { property }

The color mode of the particles.

### Lifetime:NumberRange { property }

Specifies the range of the lifetime of the particles. A random value in this range will be choosen as particle lifetime.

### SizeOverLifetime:NumberRange { property }

The size of the particles, over the lifetime of the particle.

### Speed:NumberRange { property }

The speed of the particles.  A random value in this range will be choosen. The particle moves in its direction at this speed.

### EmissionRate:int { property }

The amount of particles spawned in every second

### MaxParticles:int { property }

The maximum amount of particles that can exist at any time.

### Gravity:float { property }

If not set to 0, this will apply a gravitational force to the particles.

### SimulationSpace:ParticleSimulationSpace { property }

Whether the particles are simulated in world or local space.

### StartRotation:NumberRange { property }

The rotation the particles will start in. A random value in this range will be choosen.

### AngularVelocity:NumberRange { property }

The angular velocity (= the rate of rotation) of the particles. A random value in this range will be choosen.

### Autoplay:bool { property }

Whether these particles should automatically start emitting or be manually scripted.

### Loop:bool { property }

Whether these particles should loop indefinitely, or stop after the specified duration.

### Duration:float { property }

The duration of how long the particles object keeps emitting particles.

### Shape:ParticleShape { property }

The shape of the particles.

### ShapeRadius:float { property }

The radius of the specified shape.

### ShapeAngle:float { property }

The angle of the specified shape.

### ShapeScale:float { property }

The scale of the specified shape.

### IsPlaying:bool { property }

Whether this particles object is currently emitting particles.

{{ readonly() }}

### IsPaused:bool { property }

Whether this particles object is currently paused.

{{ readonly() }}

### IsStopped:bool { property }

Whether this particles object is currently stopped.

{{ readonly() }}

### ParticleCount:int { property }

The count of particles currently emitted and still alive.

{{ readonly() }}

### Time:float { property }

The current time in the duration timespan.

{{ readonly() }}

### TotalTime:float { property }

The total time the particles object has been emitting particles for.

{{ readonly() }}

