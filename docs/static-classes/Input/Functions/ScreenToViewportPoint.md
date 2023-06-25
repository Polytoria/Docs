# ScreenToViewportPoint

### Description

Transforms `screenPosition` from screen space into viewport space. <br />
Screenspace is defined in pixels. <br />
The bottom-left of the screen is (0,0); the right-top is ([pixelWidth](https://docs.unity3d.com/ScriptReference/Camera-pixelWidth.html),[pixelHeight](https://docs.unity3d.com/ScriptReference/Camera-pixelHeight.html)). The z position is in world units from the camera.

Function of [Input](../../)

#### Parameters

screenPosition `Vector3`

#### Return type

`Vector3`

### Example

```lua
Input.ScreenToViewportPoint(screenPosition)
```
