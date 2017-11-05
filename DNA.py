import string
import random

class DNA:

    def __init__(self, size=None, genes=None):

        if genes is None:
            self.genes = [random.choice(string.ascii_letters + " ") for x in range(size)]
        else:
            self.genes = genes
