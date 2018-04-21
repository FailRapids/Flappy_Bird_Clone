extends Control

# class member variables go here, for example:
# var a = 2
# var b = "textvar"

func _ready():
	# Called every time the node is added to the scene.
	# Initialization here
	pass


func _on_Button2_pressed():
	pass # replace with function body


func _on_Button_pressed():
	get_tree().change_scene_to(load('res://Scenes/Test_Level.tscn'))


func _on_Button3_pressed():
	get_tree().quit()
