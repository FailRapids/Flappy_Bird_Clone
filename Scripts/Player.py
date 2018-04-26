from godot import exposed, export
from godot.bindings import *
from godot.node_path import NodePath
from godot.vector2 import Vector2

@exposed
class Player(KinematicBody2D):
	"""
		Attributes: 
			GRAVITY (Vector2): Describes the effects of gravity on the Player 
			JUMP_SPEED (int): Force of Players Jump in pix/sec
		Bugs:
			Cant Call any Methods on $AnimationPlayer
			Cant Recive Signals from up the tree
		Notes:
		
	""" 
	_JUMP_SPEED  = 480
	_GRAVITY = Vector2(0,900) 
	

	def _ready(self):
		self._force_on_player = Vector2(0,0)
		self._pPos = self.get_position()
		self.set_physics_process(False)

	def _process(self,delta):
		if Input.is_action_just_pressed("Player_Jump"):
			self.set_physics_process(True)
			self.set_process(False)
		
	def _physics_process(self,delta):
		self._force_on_player += self._GRAVITY * delta 
		if Input.is_action_just_pressed("Player_Jump") and self.is_Falling():
			self._force_on_player.y = self.JUMP_SPEED
			self.get_node("AnimationPlayer").play("Flapping",-1,1,False)
		else:
			 pass
		self._pPos = self.get_position()
		self._force_on_player = self.move_and_slide(self._force_on_player,Vector2(0,0),5,4,.78)


	def is_Falling(self):
		return self._pPos.y < self.get_position().y

	@export(Vector2)
	@property
	def GRAVITY(self):
		return self._GRAVITY

	@export(int)
	@property
	def JUMP_SPEED(self):
		return -self._JUMP_SPEED
		
		#when a physics body enters player HitBox
	#kill him
	def _on_HitBox_body_entered(self,body):
		if body.is_in_group("Pipes"):
			#self.get_node("AnimationPlayer").play("Stagger")
			self.queue_free()
	#when the player leaves levels bounds	
	def _on_World_body_exited(self,body):
		if body == self:
			#self.get_node("AnimationPlayer").play("Death")
			self.queue_free()
