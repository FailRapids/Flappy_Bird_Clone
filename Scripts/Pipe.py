from godot import exposed, export
from godot.bindings import KinematicBody2D
from godot.vector2 import Vector2
from godot.array import Array


#Vector2 move_and_slide( Vector2 linear_velocity, Vector2 floor_normal=Vector2( 0, 0 ), float slope_stop_min_velocity=5, int max_bounces=4, float floor_max_angle=0.785398 )

@exposed
class Pipe(KinematicBody2D):
	World = None

	def _ready(self):
		self.World = self.get_node("../../../World")
		self.World.connect("body_exited",self,"_on_World_body_exited",Array(),0)
		self.add_to_group(str(self.get_parent().group),False)

	def _physics_process(self,delta):
		self.move_and_slide(Vector2(-200,0),Vector2(0,0),5,4,.78)

	def _on_World_body_exited(self,body):
		if body == self:
			self.queue_free()