from spawn import Spawn
import random

class Population:

    def __init__(self, target, size=200):

        self.target = target
        self.size = size
        self.spawns = [Spawn(self.target) for x in range(size)]
        self.mating_pool = []
        self.generation = 0
        self.evolved = 0
        self.fitness = 0
