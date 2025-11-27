size = get_world_size()
# x1, y1: bottom-left corner
# x2, y2: top-right corner
def plant_pumpkins(x1, y1, x2, y2):
	for _ in range(size):
		for _ in range(size):
			if x1 <= get_pos_x() <= x2 and y1 <= get_pos_y() <= y2:
				till()
				plant(Entities.Pumpkin)
			move(East)
		move(North)

def plant_carrots(x1, y1, x2, y2):
	for _ in range(size):
		for _ in range(size):
			if x1 <= get_pos_x() <= x2 and y1 <= get_pos_y() <= y2:
				till()
				plant(Entities.Carrot)
			move(East)
		move(North)

def plant_trees(x1, y1, x2, y2):
	for _ in range(size):
		for _ in range(size):
			if x1 <= get_pos_x() <= x2 and y1 <= get_pos_y() <= y2 and get_pos_x() % 2 == get_pos_y() % 2:
				till()
				plant(Entities.Tree)
			move(East)
		move(North)

def plant_sunflowers(x1, y1, x2, y2):
	for _ in range(size):
		for _ in range(size):
			if x1 <= get_pos_x() <= x2 and y1 <= get_pos_y() <= y2:
				till()
				plant(Entities.Sunflower)
			move(East)
		move(North)

def collect_pumpkin():
	item = get_entity_type()
	if item != Entities.Pumpkin:
		plant(Entities.Pumpkin)
	if can_harvest():
		harvest()
		plant(Entities.Pumpkin)

def collect_carrot():
	if can_harvest():
		harvest()
		plant(Entities.Carrot)

def collect_tree():
	if can_harvest():
		harvest()
		plant(Entities.Tree)

def collect_grass():
	if can_harvest():
		harvest()
		plant(Entities.Grass)

def collect_sunflower():
	if can_harvest():
		harvest()
		plant(Entities.Sunflower)

def collect(item):
	if item in [Entities.Pumpkin, Entities.Dead_Pumpkin, None]:
		collect_pumpkin()
	elif item == Entities.Carrot:
		collect_carrot()
	elif item == Entities.Tree:
		collect_tree()
	elif item == Entities.Grass:
		collect_grass()
	elif item == Entities.Sunflower:
		collect_sunflower()
	if item != Entities.Grass:
		watering()


def watering():
	if get_water() <= 0.5:
		use_item(Items.Water)
