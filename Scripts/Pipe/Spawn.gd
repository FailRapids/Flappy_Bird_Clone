extends Position2D

export(PackedScene) var Pipe
export(int) var start_x
func _on_Pipe_spawn_new():
	var new_pipe = Pipe.instance()
	set_position(Vector2(start_x,-(randi() % 300)))
	add_child(new_pipe)

