from godot import exposed, export
from godot.bindings import *


@exposed
class Player(KinematicBody2D):
	
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
	