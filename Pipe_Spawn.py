from godot import exposed, export
from godot.bindings import *


@exposed
class Pipe_Spawn(Node2D):
	pipe = ResourceLoader.load("res://Scenes/Obstacle/Pipe.tscn","",False)
	_group = None
	def _ready(self):
		self.get_parent().connect("body_exited",self,"_on_World_body_exited")

	@export(str,default="Top")
	@property
	def group(self):
		print(self._group)
		return self._group

	def _on_World_body_exited(self,body):
		if body.is_in_group(group):
			new_pipe = pipe.instance()
			self.add_child(new_pipe)
