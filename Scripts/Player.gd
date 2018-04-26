extends KinematicBody2D

export(Vector2) var _Gravity = Vector2(0,900)
export(int) var Jump_Speed = 400 

onready var pPos = get_position()

var force_on_player = Vector2()

func _ready():
	set_physics_process(false)

func _process(delta):
	if Input.is_action_just_pressed("Player_Jump"):
		set_physics_process(true)
		set_process(false)
	
func _physics_process(delta):
	force_on_player += delta * _Gravity
	if Input.is_action_just_pressed("Player_Jump") and is_Falling():
		force_on_player.y = -Jump_Speed
#		$AnimationPlayer.play("Flapping")
	elif $AnimationPlayer.is_playing():
#		$AnimationPlayer.queue("Falling")
		pass
	pPos = get_position()
	force_on_player = move_and_slide(force_on_player)

func is_Falling():
	return pPos.y < get_position().y

func _on_World_body_exited(body):
	if body == self:
		queue_free()

func _on_HitBox_body_entered(body):
	if body.is_in_group("Pipes"):
		queue_free()
