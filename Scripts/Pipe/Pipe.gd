extends KinematicBody2D

export(int) var speed = 20


func _ready():
	set_position(Vector2(0,-(randi() % 300)))
	get_parent().get_parent().connect("body_exited",self,"_on_World_body_exited")

func _physics_process(delta):
	move_and_slide(Vector2(-speed,0))

func _on_World_body_exited(body):
	if body == self:
		queue_free()