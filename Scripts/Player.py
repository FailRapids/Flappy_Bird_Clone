from godot import exposed, export
from godot.bindings import *
from godot.node_path import NodePath
from godot.vector2 import Vector2

@exposed
class Player(KinematicBody2D):
    _GRAVITY_VEC = Vector2(0,900)#pix/sec
    _JUMP_SPEED = -480
    _linear_vel = Vector2(0,0)
    _time = 0
    def _enter_tree(self):
        pass

    def _ready(self):
        pass

    def _process(self,delta):
#        self._time += delta
#        if self._time > 5:
#            print(self)
#            self._time = 0
#        else:
#            self._time += delta
         pass

    def _physics_process(self,delta):
        #UGH MATH
        self._linear_vel += self._GRAVITY_VEC * delta
        self._linear_vel = self.move_and_slide(self._linear_vel,Vector2(0,-1),0,4,0.78)
        if Input.is_action_just_pressed("Player_Jump"):
            self._linear_vel.y = self._JUMP_SPEED

    def __repr__(self):
        return f'Player:{self.get_position()}:{self._linear_vel.y}:{self._JUMP_SPEED}'
