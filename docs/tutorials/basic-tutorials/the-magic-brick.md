---
title: The Magic Brick
description: How to make a brick do the things we want.
weight: 3
---

# The Magic Brick

Welcome to my magical show, I require your help!

I was hoping to show a magic trick but it would seem that I've run out of `Bricks` to use.

What I need you to do to help me is to first spawn a `Brick`!

![Hovering over Insert > Part > Brick in the Creator menu.](/assets/tutorials/basic-tutorials/the-magic-brick/image-0.webp)

Good, good! We now have a `Brick` for us to make magic!

First let's set the scale so we have a nice even `Brick` as our basis.

We'll want to be `4 , 4 , 4` and set the position to be `0 , 10 , 0`.

![Hovering over the Size options in the properties panel.](/assets/tutorials/basic-tutorials/the-magic-brick/image-1.webp)

Next, we'll need a floor for you to stand on so you can observe our interesting `bricks` we'll be using!

So we're going to create another `Brick`!

We'll want to be `20 , 1 , 20` and set the position to be `0 , 0 , 0`.

Just be careful not to fall off when you enter the game world!

Now we're going to select our `4 , 4 , 4` `Brick` and give it a `LocalScript`.

A `LocalScript` allow for only the client to see changes, this could be used to make it so other players can see different things as they happen! We're going to be using this knowledge to our advantage to make a magic `Brick` that can appear different for everybody!

![Hovering over Insert > Scripting > LocalScript in the Creator menu.](/assets/tutorials/basic-tutorials/the-magic-brick/image-2.webp)

You may notice that the `LocalScript` that we made has been put under the `ScriptService` object, this is because `ScriptService` normally holds all of our scripts that we'd use to manage games and experiences.

This time however we should reparent our LocalScript into the `4 , 4 , 4` `Brick` like so. As we want to have it as the parent of the script.

![Re-parented LocalScript inside of the Brick in the Explorer menu.](/assets/tutorials/basic-tutorials/the-magic-brick/image-3.webp)

Okay good! Now we just need to double click the `LocalScript` to open it in a text editor!

We're going to start off by adding the following code:

```
local Brick = script.Parent

game.Rendered:Connect(function(dt)
    Brick.Rotation = Vector3.New(0,Brick.Rotation.y + 1,0)
end)
```

The object `game` refers to the whole game world, and the `Rendered` event is what allows us to do updates every frame, we're going to use this to have a constantly modified `Brick` that changes over time! In this case, we would like to make it spin first!

`script.Parent` is how we grab our `Brick` relative to the `LocalScript` we just made!

You can modify this to be `Rotation` or `Size` or any of the other documented properties that fall under `DynamicInstance` as a `Brick` inherits it!

Well, Now we can try pressing the `Tools > Test Game` button in the Creator and you should see our `Brick` spinning!

It's cool to see our `Brick` spinning now, but we should also give it some bounce!

Next we should add a `time` variable! This will hold our time so that when we want a bounce, we can do that.

We'll also want to see this in action, so we'll update the `time` variable and apply it using a `math.sin()` function to the `y` position of our `Brick`. We also want to use `10` as our base position, as this is updated every frame, if we used the current `Brick` position, it can get a little crazy.

```
local Brick = script.Parent
local time = 0

game.Rendered:Connect(function(dt)
    time = time + (1 * dt)
  	Brick.Rotation = Vector3.New(0, Brick.Rotation.y + 1 ,0)
    Brick.Position = Vector3.New(0, 10 + math.sin(time) ,0)
end)
```

Now we should have a nice bouncing `Brick` that goes up and down! How magical!

We'll also apply this concept to the `Size` of the `Brick` so it's constantly changing size over time!

We need do this uniformly, so we need to create a variable to hold our total compiled size and apply it!

```
local Brick = script.Parent
local time = 0

game.Rendered:Connect(function(dt)
    time = time + (1 * dt)
  	Brick.Rotation = Vector3.New(0, Brick.Rotation.y + 1 ,0)
    Brick.Position = Vector3.New(0, 10 + math.sin(time) ,0)

    local compiledscale = 2 + math.sin(time)
    Brick.Size = Vector3.New(compiledscale,compiledscale,compiledscale)

end)
```

Great work, we're almost done now!

To differentiate our `Brick` in the `LocalScript` we should give it a `Color`! In this instance we're going to use `Color.Random()`!

So we need to add that to our `LocalScript` just above the `game.Rendered` line. As we want it to run once, and not every frame!

```
local Brick = script.Parent
local time = 0

Brick.Color = Color.Random()

game.Rendered:Connect(function(dt)
    time = time + (1 * dt)
  	Brick.Rotation = Vector3.New(0, Brick.Rotation.y + 1 ,0)
    Brick.Position = Vector3.New(0, 10 + math.sin(time) ,0)

    local compiledscale = 2 + math.sin(time)
    Brick.Size = Vector3.New(compiledscale,compiledscale,compiledscale)

end)
```

Now the last thing we need to do is publish our project for everybody to see!

Go to the `File > Publish` tab and click the `Create New Place` button.

This will open up a new webpage in your browser, click the little gear icon next to your username in this tab to edit it!

![Setting for the Place](/assets/tutorials/basic-tutorials/the-magic-brick/image-5.webp)

Name your place! I'll be naming mine "The Magic Brick Tutorial".

Next, we want to go to the `Create` tab in your browser! This can be found [here](https://polytoria.com/create/) and click `Quick Actions > Set Public`

![Setting the Place to public.](/assets/tutorials/basic-tutorials/the-magic-brick/image-4.webp)

After we do this, all you have to do is go to the same `File > Publish` tab and click the place you just made, and press `Publish to Polytoria`!

Now you have your own `Place` to share with your friends!
