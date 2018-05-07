extends Area2D

func _ready():
	for i in get_tree().get_nodes_in_group("Player"):
		self.connect("body_exited",i,"_on_Tracker_body_exited")

