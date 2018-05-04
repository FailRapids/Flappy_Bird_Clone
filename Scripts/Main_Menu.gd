extends Control


func _on_Mouse_Play_pressed():
	get_tree().change_scene_to(load('res://Scenes/Level/Level.tscn'))


func _on_Touch_Play_released():
	get_tree().change_scene_to(load('res://Scenes/Level/Level.tscn'))
