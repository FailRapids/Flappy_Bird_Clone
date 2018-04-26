extends Control


func _on_Play_pressed():
	get_tree().change_scene_to(load('res://Node2D.tscn'))


func _on_Play_Test_Level_pressed():
	get_tree().change_scene_to(load('res://Scenes/Test_Level.tscn'))


func _on_Exit_pressed():
	get_tree().quit()