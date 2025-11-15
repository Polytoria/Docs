## PR Summary

## Changed all C# mentions of arrays to be Lua-friendly **site-wide**
## ex: before, it would mention arrays of instances as Instance[], but now it will mention them as {Instance}. This is so that lua programmers know what they're looking at, and so that we can fit multiple class names as needed.

## Edited Camera.md to change the "Freecam" typo to "FreeCam"
## Added warning about lua's single-thread nature in BaseScript.md, and how to work around it

## Environment.md changes:
## Added links to nearly every reference of objects in the entire file
## Added optional parameter markers for CreateExplosion
## Modified CreateExplosion note to be more in depth and specific with wording
## Added optional parameter marker for OverlapBox and OverlapSphere
## Completely rewrote the Raycast and RaycastAll methods to be more comprehensive
## Remade RebuildNavMesh documentation :sob: :pray:, please tell me I'm not the only one that laughed when I saw game["Workspace"]
## Added optional parameter marker for GetPointOnNavMesh
## Rewrote AutoGenerateNavMesh documentation to be more comprehensive
## Added more details to PartDestroyHeight's behavior with NPCs and Players

## Added extensive explanation as to how RayResult.Normal works in RayResult.md

## Added warning about GUI.Visible behavior in GUI.md

## Added warning about Tool-descendant scripts and their odd inability to run until the first Tool.Equipped event in Tool.md

## merged with the latest pull request (all they did was organize the layout in creator-setup.md :sob:)