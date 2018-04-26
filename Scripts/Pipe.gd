extends KinematicBody2D



func _ready():
	get_node("../../../World").connect("body_exited",self,"_on_World_body_exited")
	
	
func _physics_process(delta):
	move_and_slide(Vector2(-200,0))

func _on_World_body_exited(body):
	if body == self:
		queue_free()