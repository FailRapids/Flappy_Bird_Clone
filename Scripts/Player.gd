extends KinematicBody2D
#######
#Changed to a State Based Player
#
#
########
export(Vector2) var _Gravity = Vector2(40,600)
export(int) var Jump_Speed = 480 

enum STATES {Idle,Flapping,Falling,Stagger,Death}

var current_state = null
var previous_state = null
onready var pPos = get_position()

var force_on_player = Vector2()

func _ready():
	_change_state(Idle)
	
func _physics_process(delta):
	
	if force_on_player.x > 200:
		force_on_player.x = 200
	else:
		_Gravity.x = 40
	force_on_player += delta * _Gravity
	match current_state:
		Idle:
			if Input.is_action_just_pressed("Player_Jump"):
				force_on_player.y = -Jump_Speed
				_change_state(Flapping)
			elif (pPos.y < get_position().y) and $AnimationPlayer.get_current_animation_position() > .5:
					_change_state(Falling)
		Flapping:
			if $AnimationPlayer.get_current_animation() == "Flapping" and $AnimationPlayer.get_current_animation_position() > .25:
				_change_state(Idle)
		Falling:
			_change_state(Idle)
			
	pPos = get_position()
	force_on_player = move_and_slide(force_on_player)

func _change_state(new_state):
	previous_state = current_state
	current_state = new_state
	match new_state:
		Idle:
			return
		Flapping:
			$AnimationPlayer.play("Flapping")
		Falling:
			$AnimationPlayer.play("Falling")
		Stagger:
			$AnimationPlayer.play("Stagger")
		Death:
			$AnimationPlayer.play("Death")
			queue_free()

