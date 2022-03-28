Welcome to SimpleScene Documentation!

-- texts
createText(text, position, color, size, fontFamily, rotation)
~ create a text in your scene
~ return an textObj

changeText(textObj, text)
~ change the text

checkOffScreen(sprite)
~ return a boolean that if the sprite is offscreen, then return True, or else False

getScreenSize()
~ return your screen size ( list )
~ item[0] > your screen width
~ item[1] > your screen height

moveSteps(sprite, steps, imgDir)
~ move forward the sprite for how many steps
~ imgDir means
	* 0 : the image's front is pointing at the NORTH
	* 1 : the image's front is pointing at the EAST
	* 2 : the image's front is pointing at the SOUTH
	* 3 : the image's front is pointing at the WEST
	
turnDegrees(sprite, deg)
~ turn the sprite for how many deg
~ if you enter 20deg, then the sprite will turn right for 20deg

pointTo(sprite, x, y, imgDir)
~ let the sprite point to a point
~ imgDir is same as moveSteps ( detail on moveSteps function )

playSound(src)
~ play for a music
~ you a play for more than one music at once too
~ return a soundObj
tips 1 : make a var and store it if you want to stop it later
tips 2 : the music will automatically stop when you closed the scene

setVolume(percent)
~ set the music volume, enter 0 - 100 in the percent parameter
~ IMPORTANT : You must change the volume before playing the music, or else it wont set the volume if you play the music and then setVolume

stopSound(soundObj)
~ require a soundObj
~ stop the music as you entered

createChild(imgSrc, options, position, z_position, scale, x_scale, y_scale, alpha, speed, size, color, blend_mode, rotation)

~ imgSrc is required, others are optional
~ creates a sprite
~ z_position means the layer
~ scale means : size * your scale value ( default is 1 )
~ x_scale and y_scale are the x, y scaling

~ options can be :
	followMouse
	followMouseX
	followMouseY
	
	example 1: options=[followMouse]
	example 2: options=[followMouseX, followMouseY]
	tips : remember to list it
	
~ return a spriteObj

removeSprite(spriteObj)
~ remove a sprite
	
registerOption(spriteObj, option=[your options.....])
~ add some options into the sprite

unregisterOption(spriteObj, option=[your options that you want to deleted....])
~ remove the option in the sprite

clearOptions(spriteObj)
~ clear all options

setSpriteImg(spriteObj, imgSrc, scale)
~ change the img of the sprite
~ tips : spriteObj and imgSrc are required, scale is optional

scaleSprite(spriteObj, scale)
~ scale the sprite by the scale parameter

setLayer(spriteObj, layer)
~ set the layer of a sprite

goToFrontLayer(spriteObj)
~ let the sprite go to the front layer
~ tips : if two or more sprites went to the same layer in the meantime, the newest created sprite will be the top but will not change the layer

goToBackLayer(spriteObj)
~ let the sprite go to the back layer

setPosition(spriteObj, x, y)
~ set the sprite's position to x, y

setPositionX(spriteObj, x)
~ set the sprite's position x to x

setPositionY(spriteObj, y)
~ set the sprite's position y to y

getPosition(spriteObj)
~ get the position of a sprite
~ return a list ( [your sprite x, your sprite y])

getPositionX(spriteObj)
~ get the position x of a sprite

getPositionY(spriteObj)
~ get the position y of a sprite

setSize(spriteObj, width, height)
~ set the sprite's size to width, height
~ you can also only set width or ony set height too ( just dont enter the parameter that you dont want )

getSize(spriteObj)
~ return a list ( it returns : [your sprite width, your sprite height]) of your sprite's size

setRotation(spriteObj, deg)
~ set the sprite's rotation to a deg

getRotation(spriteObj)
~ get the rotation of a sprite

rotateSprite(spriteObj, deg)
~ like your sprite's rotation is 130, then use this function to + ( plus ) the rotation by deg

getDistance(objA, objB)
~ get the distance of objA and objB ( they can be sprite )
~ special usage : you can type "mouse" in the second arg ( objB ) then it will get the distance of objA and the mouse pointer

getClicked(spriteObj)
~ return a boolean that is the sprite clicked, of the sprite is clicked, it returns True, or else it returns False

checkCollide(objA, objB)
~ return a boolean that is objA touching objB, if is, returns True, else False

getScreenTouched()
~ return a boolean that if user touched the screen then returns True, else False

setOpacity(spriteObj, percent)
~ set the opacity percent of a sprite
~ 100 > default ( no hiding effect )
~ 0 > hide ( 0 means the fully hide the sprite )

getOpacity(spriteObj)
~ return percents of opacity of sprite

changeOpacity(spriteObj, percent)
~ change the sprite opacity by percent

setBgColor(color)
~ you can type text color like "red"
~ or hex color like "#FFFFFF"

setBgImg(src)
~ set the bg to an image

clearCache()
~ clear the cache
~ to fix the small bugs
~ IMPORTANT IF YOU USED IT WRONGLY YOUR SCRIPTS WILL BE NOT WORKING
~ my scripts ( example ) :

	from SimpleScene import *

	plane = createChild("spc:PlayerShip2Blue", position=(100,400))
	runScene()

Then, I can input clearCache() in this places :

	from SimpleScene import *
	> Here

	plane = createChild("spc:PlayerShip2Blue", position=(100,400))
	runScene()

runScene(fps, show_fps, multiTouch, doForever)
~ fps can be changed in these values [60, 30, 20, 1-15] ( optional, default : 60 )
~ show_fps needs : True / False ( optional, default : True )
~ multiTouch : True / False ( optional, default : True)
~ doForever : create a def by yourself and then put some scripts into that def, finally, in runScene(), the doForever parameter can be : yourDefName

~ example:
	from SimpleScene import *
	clearCache()
	plane = createChild("spc:PlayerShip2Blue", position=(100,400))
	
	def updateForever():
		pointTo(plane, getPositionX("mouse"), getPositionY("mouse"), 0)
		moveSteps(plane, 5)
		
	runScene(doForever=updateForever)
