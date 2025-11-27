import service, config

size = get_world_size()
def init():
	clear()
	for item, x1, y1, x2, y2 in config.conf:
		if item == Entities.Pumpkin:
			service.plant_pumpkins(x1, y1, x2, y2)
		elif item == Entities.Carrot:
			service.plant_carrots(x1, y1, x2, y2)
		elif item == Entities.Tree:
			service.plant_trees(x1, y1, x2, y2)
		elif item == Entities.Sunflower:
			service.plant_sunflowers(x1, y1, x2, y2)


def run():
	while True:
		for _ in range(size):
			for _ in range(size):
				item = get_entity_type()
				service.collect(item)
				move(East)
			move(North)