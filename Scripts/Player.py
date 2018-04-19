from godot import exposed, export
from godot.bindings import *


@exposed
class Player(KinematicBody2D):
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<<
	
	def _enter_tree(self):
		self._pos = self.get_position()
		pass
		
	def _ready(self):
		pass
	
	def _process(self,delta):
		#print(delta)
		if Input.is_action_pressed('Player_Up'):
			print(f'UP was Pressed and Caught by {self}')
		elif Input.is_action_pressed('Player_Down'):
			print(f'DOWN was Pressed and Caught By {self}')
		if Input.is_action_pressed('Player_Left'):
			print(f'LEFT was Pressed and Caught By {self}')
		elif Input.is_action_pressed('Player_Right'):
			print(f'RIGHT was Pressed and Caught By {self}')
		
	def _physics_process(self,delta):
		pass
		
	def _input(self,event):
		pass
	
	def _exit_tree(self):
		pass
  #####Data Model#####
	def __repr__(self):
		return f'Player at (x:{self._pos.x},y:{self._pos.y})'
	
=======
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
<<<<<<< HEAD
    _STATES = ["IDLE","MOVE"]
    def _enter_tree():
        self._max_walk = 450 #pix
        self._max_run = 700 #pix
        
    def _ready(self):
        self._state = 0
        

    def _process(self,delta):
        pass
    
    def _physics_process(self,delta):
        self._look_direction = self._input_direction  
        if (self.State == "IDLE") and (self.Input_Direction == Vector2(0,0)):
            self.State = 1
        elif self.State == "WALK":
            #Are We Walking
            if self.Input_Direction != Vector2(0,0):
                self.State = 0
                return
            self.move(self._max_walk,self.Input_Direction)
    
    def move(self, speed, direction):
	velocity = direction.normalized() * speed
	self.move_and_slide(velocity, Vector2(), 5, 2)
    
    @property
    def Input_Direction(self):
        self._input_direction = Vector2(0,0)
        if Input.is_action_pressed("Player_Up"):
            self._input_direction = Vector2(0,-1)
        elif Input.is_action_pressed("Player_Down"):
            self._input_direction = Vector2(0,1)
        elif Input.is_action_pressed("Player_Left"):
            self._input_direction = Vector2(-1,0)
        elif Input.is_action_pressed("Player_Right"):
            self._input_direction = Vector2(1,0)
        return self._input_direction

    @property
    def Look_Direction(self)
        return self._look_direction
    
    @Look_Direction.setter
    def Look_Direction(self,direction):
        if isinstance(direction,Vector2):
            self._look_direction = direction.normalized()
        self.get_node(NodePath("BodyPivot")).set_scale(Vector2(direction.x,1))
                      
    @property
    def State(self):
        return self._state

    @State.setter
    def State(self value:int=0)
        if value < 2 and value >=0:
            self._state = _STATES[value]
            self.get_node("AnimationPlayer").play(self._state)
        else:
            raise ValueError("{self._STATES}")
=======
	
	def _enter_tree(self):
		self._pos = self.get_position()
		pass
		
	def _ready(self):
		pass
	
	def _process(self,delta):
		#print(delta)
		if Input.is_action_pressed('Player_Up'):
			print(f'UP was Pressed and Caught by {self}')
		elif Input.is_action_pressed('Player_Down'):
			print(f'DOWN was Pressed and Caught By {self}')
		if Input.is_action_pressed('Player_Left'):
			print(f'LEFT was Pressed and Caught By {self}')
		elif Input.is_action_pressed('Player_Right'):
			print(f'RIGHT was Pressed and Caught By {self}')
		
	def _physics_process(self,delta):
		pass
		
	def _input(self,event):
		pass
	
	def _exit_tree(self):
		pass
<<<<<<< HEAD
  
>>>>>>> parent of 216e28f... Input testing in python
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream
<<<<<<< Updated upstream

>>>>>>>
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
>>>>>>> Stashed changes
=======
  #####Data Model#####
	def __repr__(self):
		return f'Player at (x:{self._pos.x},y:{self._pos.y})'
	
>>>>>>> build_player
