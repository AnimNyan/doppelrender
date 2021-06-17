# Dopplerender Blender Plugin
![Dopplerender Logo](http://creativityhacker.ca/wp-content/uploads/2017/09/Dopplerender2-Logo.png)

## Credits
A Blender Add on originally made by Jefferson Smith for Blender 2.78, updated by Anime Nyan for Blender 2.93+.

## What does the Dopplerender Blender plugin do?
Dopplerender is a render-time add-on for Blender that eliminates time and resources wasted on producing redundant frames. 
It does this by detecting frames that will be identical to one already rendered and reusing that instead of rendering it again.

## Step by Step explanation:
1. The plugin renders out a really really small low quality version of the animation first. 
2. It will check if any of the frames in the low quality animation are exactly the same. 
3. It will render the full quality version only rendering the frames that are different and copying frames which are the same, saving you render time.