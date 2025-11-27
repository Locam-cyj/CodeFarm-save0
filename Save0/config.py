size = get_world_size() // 2
conf = [
	[Entities.Tree, 0, 0, size + 1, size - 1],
	[Entities.Carrot, size + 2, 0, size * 2 - 1, size + 1],
	[Entities.Pumpkin, 0, size, size + 1, size * 2 - 1],
	[Entities.Sunflower, size + 2, size + 2, size * 2 - 1, size * 2 - 1]
]