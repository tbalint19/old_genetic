from population import Population
from spawn import Spawn
import random
import time
import os

population = Population(target="Whatever whatever")

spawns = population.spawns

while population.evolved < 170:

    population.evolved = 0
    population.fitness = 0
    mating_pool = []
    current_fittest = None
    best_fit = 0
    for spawn in spawns:
        fitness = spawn.calculate_fitness()
        population.fitness += fitness
        if fitness > best_fit:
            current_fittest = spawn
        if fitness == len(population.target):
            population.evolved += 1
        for x in range(spawn.fitness):
            mating_pool.append(spawn)

    new_spawns = []
    for x in range(population.size):
        spawn = random.choice(mating_pool).give_birth(random.choice(mating_pool))
        new_spawns.append(spawn)

    spawns = new_spawns
    population.generation += 1
    os.system('clear')
    print("\n\n\n\t\t" + str(current_fittest.speak()))
    print("\n\n\n\t\tGeneration: " + str(population.generation) + " -----> " + str(population.evolved/2) + "%" + " is evolved.")
    print("\t\tOverall fitness: " + str((population.fitness/200)/len(population.target)))
