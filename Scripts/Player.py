from godot import exposed, export
from godot.bindings import *


@exposed
class Player(KinematicBody2D):
	
	def _enter_tree(self):
		pass
		
	def _ready(self):
		pass
	
	def _process(self,delta):
		pass
		
	def _physics_process(self,delta):
		pass
		
	def _input(self,event):
		pass
	
	def _exit_tree(self):
		pass
  