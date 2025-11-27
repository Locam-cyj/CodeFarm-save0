def f():
	clear()
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			till()
			plant(Entities.Pumpkin)
			move(East)
		move(South)
	while True:
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				print(get_entity_type())
				if can_harvest():
					harvest()
					plant(Entities.Pumpkin)
				move(East)
			move(South)
# GitHub推送测试