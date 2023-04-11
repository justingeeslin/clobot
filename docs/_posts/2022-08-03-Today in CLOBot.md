---
layout: post
title:  "Today in CLOBot: The Flying Nun Problem"
date:   2022-08-03- 16:07:00 -0500
categories: flying-nun-problem
---
Even without simulations saved into the blocks sometimes you will have blocks that are placed incorrectly, too low.
![](/assets/images/Screen%20Shot%202022-08-02%20at%207.29.33%20PM.png)

Resetting the 3D arrangement seems to solve this problem. 
![](/assets/images/Screen%20Shot%202022-08-02%20at%207.30.17%20PM.png)

A Reset 3D arrangement button in the API would be useful so that we don’t keep having simulations where the garments appear misplaced.
Looking for a function with reset in the name inside of `mdsa`  and `mdm` returns empty set. 

Here are some other candidates:
`UpdateSimulation`
`MoveUpGarment` - seems useful. going up is always the problem. The simulation usually handles the going down part. ;) 
`SetAvatarSkinOffset` - seems like long shot. But same principle, moving things away from the avatar.


Interesting results for: 
```
mdm.MoveUpGarment(200)
```
![](/assets/images/Screen%20Shot%202022-08-02%20at%207.42.59%20PM.png)
This moved the garment up. But how will I be able to do this for all possible avatars. I’ll never know exactly how much to move it.


Weirdly, tapping the Y Position slider in the Property Editor “resets” the 3D position for the selected piece. 

What if:
`GetAxisY`
Then
`SetAxisY`
In an attempt to reset? Ok, how do you select the pieces?
Let’s see if these functions work they way I think. TBD Babies need watching.
