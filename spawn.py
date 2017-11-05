from DNA import DNA
import random
import string

class Spawn:

    def __init__(self, target, genes=None, mutation_rate=10):

        self.target = target
        if genes is None:
            self.dna = DNA(size=len(target))
        else:
            self.dna = DNA(genes=genes)
        self.fitness = 0
        self.mutation_rate = mutation_rate

    def speak(self):
        return "".join(self.dna.genes)

    def calculate_fitness(self):
        matches = 0
        for x in range(len(self.dna.genes)):
            if self.dna.genes[x] == self.target[x]:
                matches += 1
        self.fitness = int(matches/len(self.target)*100)
        return matches

    def give_birth(self, other):
        new_genes =  []
        for x in range(len(self.dna.genes)):
            new_genes.append(random.choice([self.dna.genes[x], other.dna.genes[x]]))
        child_spawn = Spawn(self.target, genes=new_genes)
        child_spawn.mutate()
        return child_spawn

    def mutate(self):
        for index in range(len(self.dna.genes)):
            mutation_happened = random.randint(0, 10000) < self.mutation_rate
            if mutation_happened:
                self.dna.genes[index] = random.choice(string.ascii_letters + " ")
