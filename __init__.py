import scene, SimpleScene, sound, importlib, math
	
print("Hello from SimpleScene!\nFor help, type help()!\n==============================")


#documentation: scene

#init - vars

sprites = []
bg_color = "white"
bg_img = None
bgGenerated = False

# init - option vars

followMouse = "followMouse"
followMouseX = "followMouseX"
followMouseY = "followMouseY"

# init - mouse x, y

mx, my = 0, 0

# functions
	
# -- text labels

def createText(text, position=(0,0), color="black", size=20, fontFamily="Helvetica", rotation=0):
	
	label = scene.LabelNode(font=(fontFamily, size), text=text)
	label.removed = False
	
	label.position = position
	label.color = color
	label.rotation = math.radians(rotation)
	label.options = []
	
	sprites.append(label)
	
	return label
	
def changeText(label, text):
	label.text = text

# -- screen

def checkOffScreen(sprite):
	pos = getPosition(sprite)
	return (pos[0] < 0) or (pos[0] > getScreenSize()[0]) or (pos[1] < 0) or (pos[1] > getScreenSize()[1])

def getScreenSize():
	return [scene.get_screen_size().w, scene.get_screen_size().y]
	
# -- motion blocks
	
def moveSteps(sprite, steps=1, imgDir=0):
	rot = sprite.rotation - imgDir * math.radians(90)
	sprite.position = (sprite.position.x + math.sin(rot) * -steps, sprite.position.y + math.cos(rot) * steps)
		
	
def turnDegrees(sprite, deg):
	sprite.rotation += math.radians(deg)
	
def pointTo(sprite, x, y, imgDir):
	try:
		halfScreenX = scene.get_screen_size().w / 2
		halfScreenY = scene.get_screen_size().h / 2
	
		basex = getPositionX(sprite) - halfScreenX
		basey = getPositionY(sprite) - halfScreenY
	
		pointx = x - halfScreenX
		pointy = y - halfScreenY
	
		deg = math.atan((pointx - basex) / (pointy - basey)) * 57.2957795
		deg = (90 * imgDir - deg)
		if pointy < basey:
			deg += 180
		
		if (int(sprite.position.x) != int(getPositionX("mouse"))) and (int(sprite.position.y) != int(getPositionY("mouse"))):
			sprite.rotation = math.radians(deg)
	except:
		pass
	
	
# -- sounds

def playSound(src):
	return sound.play_effect(src)
	
def setVolume(percent):
	sound.set_volume(percent / 100)
	
def stopSound(soundEffect):
	sound.stop_effect(soundEffect)
	
# -- sprites and options

def createChild(imgSrc, options=[], position=(0,0), z_position=0.0, scale=1.0, x_scale=1.0, y_scale=1.0, alpha=1.0, speed=1.0, size=None, color="white", blend_mode=0, rotation=0):
	global sprites
	
	sprites.append({ "name" : imgSrc, "position" : position, "z_position" : z_position, "scale": scale, "x_scale" : x_scale, "y_scale" : y_scale, "alpha" : alpha, "speed" : speed, "parent" : False, "size" : size, "color" : color, "blend_mode" : blend_mode})
	
	i = sprites[len(sprites) - 1]
	s = scene.SpriteNode(i["name"], i["position"], i["z_position"], i["scale"], i["x_scale"], i["y_scale"], i["alpha"], i["speed"])
	s.color = i["color"]
	if size != None:
		s.size = i["size"]
	s.blend_mode = i["blend_mode"]
	s.clicked = False
	s.removed = False
	s.options = options
	s.removedFromParent = False
	setRotation(s, rotation)
	
	del sprites[len(sprites) - 1]
	sprites.append(s)
	
	return s
	
def removeSprite(sprite):
	global sprites
	sprite.removedFromParent = True
	sprites.remove(sprite)
	sprite.remove_from_parent()
	
def registerOption(sprite, option):
	sprite.options.append(option)
	
def unregisterOption(sprite, options):
	for option in options:
		del sprite.options[sprite.options.index(option)]
		
def clearOptions(sprite):
	sprite.options = []

def setSpriteImg(sprite, imgSrc, scale=(1,1)):
	sprite.texture = scene.Texture(imgSrc)
	
	sprite.x_scale = scale[0]
	sprite.y_scale = scale[1]
	
def scaleSprite(sprite, scale):
	sprite.x_scale = scale[0]
	sprite.y_scale = scale[1]

def setLayer(sprite, layer):
	if layer < -1:
		layer = -1
		raise Error("The minimum layer value is -1")
	if layer > 100000000:
		layer = 100000000
		raise Error("The maximum layer value is 100000000")
		
	sprite.z_position = layer
	
def getLayer(sprite):
	return sprite.z_position
	
def goToFrontLayer(sprite):
	sprite.z_position = 100000000
	
def goToBackLayer(sprite):
	sprite.z_position = -1

def setPosition(sprite, x=None, y=None):
	setx = x
	sety = y
	if x == None:
		setx = sprite.position.x
	if y == None:
		sety = sprite.position.y
		
	sprite.position = (setx, sety)
	
	
def moveBy(sprite, x, y):
	sprite.position += (x, y)
	
def setPositionX(sprite, x):
	sprite.position = (x, getPosition(sprite)[1])
	
def setPositionY(sprite, y):
	sprite.position = (getPosition(sprite)[0], y)
	
def getPosition(sprite):
	if sprite == "mouse":
		return [mx, my]
	else:
		return [sprite.position.x, sprite.position.y]
	
def getPositionX(sprite):
	if sprite == "mouse":
		return mx
	else:
		return sprite.position.x
	
def getPositionY(sprite):
	if sprite == "mouse":
		return my
	else:
		return sprite.position.y
	
def getSize(sprite):
	return [sprite.size.w, sprite.size.h]
	
def setSize(sprite, width=None, height=None):
	setw = width
	seth = height
	if width == None:
		setw = sprite.size.w
	if height == None:
		seth = sprite.size.h
	
	sprite.size = (setw, seth)

def setRotation(sprite, deg):
	sprite.rotation = math.radians(deg)
	
def rotateSprite(sprite, deg):
	sprite.rotation += math.radians(deg)
	
def getRotation(sprite):
	return sprite.rotation * 57.2957795
		
	
# -- sensing

def getDistance(a, b=None):
	if b == "mouse" and b != None:
		m = getPosition("mouse")
		arg = [(m[0] - a.position.x) * (m[0] - a.position.x), (m[1] - a.position.y) * (m[1] - a.position.y)]
		return math.sqrt(arg[0] + arg[1])
	elif b != None:
		arg = [(b.position.x - a.position.x) * (b.position.x - a.position.x), (b.position.y - a.position.y) * (b.position.y - a.position.y)]
		return math.sqrt(arg[0] + arg[1])
	
def getClicked(sprite):
	return sprite.clicked
	
def checkCollide(a, b):
	return a.frame.intersects(b.frame) and not a.removedFromParent and not b.removedFromParent
	
def getScreenTouched():
	global myScene
	return myScene.touching
	
# -- effects
	
def setOpacity(sprite, percent):
	sprite.alpha = percent / 100
	if sprite.alpha < 0:
		sprite.alpha = 0
	elif sprite.alpha > 1:
		sprite.alpha = 1
	
def getOpacity(sprite):
	return sprite.alpha * 100
	
def changeOpacity(sprite, percent):
	sprite.alpha += percent / 100
	if sprite.alpha < 0:
		sprite.alpha = 0
	elif sprite.alpha > 1:
		sprite.alpha = 1
		
# -- bg

def setBgColor(c):
	global bg_color
	bg_color = c
	
def setBgImg(imgSrc):
	global bg_img
	bg_img = imgSrc
	
# -- clear cache
	
def clearCache():
	importlib.reload(SimpleScene)
	
# -- run Scene
	
def runScene(fps=60, show_fps=True, multiTouch=True, doForever=""):
	global sprites
	global bg_color
	global mx, my
	global bg_img, bgGenerated
	global myScene
	
	class app(scene.Scene):
		def setup(self):
			global bg_color
			
			self.ground = scene.Node(parent=self)
			self.background_color = "blue"
			self.touching = False
			self.pos = [0, 0]
				
		def stop(self):
			global sprites
			sprites = []
			sound.stop_all_effects()
				
		def touch_began(self, touch):
			
			self.touching = True
			for obj in sprites:
				if touch.location in obj.frame:
					obj.clicked = True
					 
			self.touch_moved(touch)
							
		def touch_moved(self, touch):
			global mx, my
			
			mx = touch.location.x
			my = touch.location.y
			self.pos = [touch.location.x, touch.location.y]
		
		def update(self):
			self.ground = scene.Node(parent=self)
			
			global bg_color, bgGenerated
			self.background_color = bg_color
			
			if doForever != "":
				doForever()
				
			scene.Vector2(getScreenSize()[0] / 2, getScreenSize()[1] / 2) #use Vect2 Obj
			
			scene.BLEND_MULTIPLY, scene.BLEND_ADD = 0, 0 #set blend mode and type
			
			scene.Rect(-1,-1, getScreenSize()[0], getScreenSize()[1]).inset(-1,getScreenSize()[0]/2, -1, getScreenSize()[0]/2) #inset hitbox
			
						
			if bg_img != None and not bgGenerated:
				self.bgImageSprite = scene.SpriteNode(bg_img)
				self.bgImageSprite.position = (self.size.w / 2, self.size.h / 2)
				self.bgImageSprite.size = (self.size.w, self.size.h)
				self.bgImageSprite.z_position = -2
				self.ground.add_child(self.bgImageSprite)
				bgGenerated = True
				
			for i in sprites:
				i.remove_from_parent()
				
			for i in sprites:
				self.ground.add_child(i)
				
			if self.touching:
				self.runOptions(scene.Touch(self.pos[0], self.pos[1], self.pos[0], self.pos[1], 1).location)
				
		def runOptions(self, touch):
			for i in sprites:
				self.ground.add_child(i)
				
			for s in sprites:
				if s.options != []:
					for i in s.options:
						if i == "followMouse":
							s.position = (touch.x, touch.y)
						elif i == "followMouseX":
							s.position = (touch.x, s.position.y)
						elif i == "followMouseY":
							s.position = (s.position.x, touch.y)
						
							
		def touch_ended(self, touch):
			
			self.touching = False
			for obj in sprites:
				obj.clicked = False
				
			self.touch_moved(touch)
			
	myScene = app()
	
	scene.run(myScene, scene.DEFAULT_ORIENTATION, show_fps=show_fps, frame_interval=60/fps, multi_touch=multiTouch)
