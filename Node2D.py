from godot import exposed, export
from godot.bindings import *


@exposed
class Node2D(Node2D):
	def _process(self,delta):
#		print(f'{self.get_name()}:{self.get_position()}')
#		for i in self.get_children():
#			print(f'{i.get_name()}:{i.get_position()}')
		pass
	def _on_World_area_exited(self,area):
		for i in self.get_children():
			for j in i.get_children():
				if area == j:
					i.set_position(Vector2(1000,-300))
					print(f'{self.get_position()}')