extends KinematicBody2D

export(Vector2) var Force_Grav = Vector2(0,900)
export(int) var Jump_Speed = 480 
var _linear_vel = Vector2()
var _prev_vel = Vector2()
func _physics_process(delta):
	_prev_vel = _linear_vel
	#calc New force
	_linear_vel += delta * Force_Grav
	if Input.is_action_just_pressed("Player_Jump"):
		#apply force of Jump rember godot y-axis is inverted
		_linear_vel.y = -Jump_Speed
		$AnimationPlayer.play("Flap",-1,1.0,false)
	elif _prev_vel.y < _linear_vel.y: 
		set_rotation(clamp(_linear_vel.angle(),0,35))

	if OS.is_debug_build():
		if Input.is_action_just_pressed("Player_Right"):
			self.Force_Grav.x = 100
		elif Input.is_action_just_pressed("Player_Left"):
			self.Force_Grav.x = -100
		if Input.is_action_just_pressed("DEBUG_GRAV_SWITCH_Y"):
			print("Invert Y Grav")
			Force_Grav = Force_Grav.reflect(Vector2(1,0))
		elif Input.is_action_just_pressed("DEBUG_GRAV_SWITCH_X"):
			print("Invert X Grav")
			Force_Grav = Force_Grav.reflect(Vector2(0,1))
	_linear_vel = move_and_slide(_linear_vel)