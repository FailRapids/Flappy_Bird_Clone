from godot import exposed, export
from godot.bindings import *
from godot.node_path import NodePath
from godot.vector2 import Vector2

@exposed
class Player(KinematicBody2D):
	_GRAVITY_VEC = Vector2(20,900)#pix/sec
	_JUMP_SPEED = -480
	_linear_vel = Vector2(0,0)
	
	def _physics_process(self,delta):
		self._linear_vel += self._GRAVITY_VEC * delta
		self._linear_vel = self.move_and_slide(self._linear_vel,Vector2(0,-1),0,4,0.78)
		if Input.is_action_just_pressed("Player_Jump"):
			self._linear_vel.y = self._JUMP_SPEED
			self.get_node("AnimationPlayer").play("Flap",-1,1,False)
        #else:
             #self.get_node(NodePath("AnimationPlayer")).play("Idle",-1,1,False)
    
	def __repr__(self):
		return f'Player:{self.get_position()}:{self._linear_vel.y}:{self._JUMP_SPEED}'
