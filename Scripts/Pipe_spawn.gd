extends Node2D

var pipe = preload("res://Scenes/Obstacle/Pipe.tscn")

func _ready():
	pass


func _on_World_body_exited(body):
	if body != $Player:
		var new_pipe = pipe.instance()
		add_child(new_pipe)
		for i in get_children():
			print(i.get_position())
