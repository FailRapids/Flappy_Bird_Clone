extends Position2D

export(PackedScene) var Pipe

func _on_Pipe_spawn_new():
	var new_pipe = Pipe.instance()
	set_position(Vector2(480,-(randi() % 300)))
	add_child(new_pipe)

