extends Node2D

var pipe = preload("res://Scenes/Obstacle/Pipe.tscn")

export(String) var group = "Top"

func _ready():
	get_parent().connect("body_exited",self,"_on_World_body_exited")


func _on_World_body_exited(body):
	if body.is_in_group(group):
		var new_pipe = pipe.instance()
		add_child(new_pipe)

