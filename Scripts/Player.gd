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
			
		Flapping:
			if (pPos.y < get_position().y) and $AnimationPlayer.get_current_animation_position() > .5:
				_change_state(Falling)
		Falling:
			_change_state(Idle)
		Stagger:
			if not($AnimationPlayer.is_playing()):
				force_on_player.x = 100
				force_on_player.y = 0
				_change_state(Idle)
			else:
				force_on_player.x = force_on_player.x - 10*delta
				
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
			force_on_player.x = -200
			force_on_player.y = -Jump_Speed
		Death:
			$AnimationPlayer.play("Death")
			queue_free()

func _on_Area2D_body_entered(body):
	if body.get_name() == "Pipe":
		_change_state(Stagger)
