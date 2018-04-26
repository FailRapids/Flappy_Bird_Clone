extends KinematicBody2D



func _ready():
	pass
func _physics_process(delta):
	move_and_slide(Vector2(-2000*delta,0))

func _on_World_body_exited(body):
	if body == self:
		print('movein to the other_side')
		print(get_name())
		set_position(Vector2(1500,self.get_position().y))
		print(get_position())
		