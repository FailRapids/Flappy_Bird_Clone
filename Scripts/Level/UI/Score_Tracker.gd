extends Control




func _on_Player_Score_Changed(Score):
	$Label.set_text("%s"%Score)