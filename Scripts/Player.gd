extends KinematicBody2D

export(Vector2) var Force_Grav = Vector2(0,900)
export(int) var Jump_Speed = 480 
var _linear_vel = Vector2()

func _physics_process(delta):
	#calc New force
	_linear_vel += delta * Force_Grav
	#apply Grav
	_linear_vel = move_and_slide(_linear_vel)
	if Input.is_action_just_pressed("Player_Jump"):
		#apply force of Jump rember godot y-axis is inverted
		_linear_vel.y = -Jump_Speed
		$AnimationPlayer.play("Flap",-1,1.0,false)