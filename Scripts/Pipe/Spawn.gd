extends Position2D

export(PackedScene) var Pipe


func _on_Timer_timeout():
	var new_pipe = Pipe.instance()
	add_child(new_pipe)
	print("spawn")


func start():
	$Timer.start()
