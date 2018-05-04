extends KinematicBody2D

export(int) var speed = 20
signal spawn_new
func _ready():
	connect("spawn_new",get_parent(),"_on_Pipe_spawn_new")
	get_parent().get_parent().connect("body_exited",self,"_on_World_body_exited")

func _physics_process(delta):
	move_and_slide(Vector2(-speed,0))

func _on_World_body_exited(body):
	if body == self:
		emit_signal("spawn_new")
		queue_free()