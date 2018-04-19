extends KinematicBody2D


const GRAVITY_VEC = Vector2(0, 900)
const JUMP_SPEED = 480

var linear_vel = Vector2()

func _physics_process(delta):
	linear_vel += delta * GRAVITY_VEC
	linear_vel = move_and_slide(linear_vel, Vector2(0, -1), 0)
	if Input.is_action_just_pressed("Player_Jump"):
		linear_vel.y = -JUMP_SPEED




