import matplotlib.pyplot as plt
import numpy as np
import math
import random

class Clonalg:
    def __init__(self, max_it, n1, n2, beta, limits, evaluation):
        self.max_it = max_it
        self.N = n1
        self.n1 = n1
        self.n2 = n2
        self.beta = beta
        self.nc = int(beta * self.N)  # Number of clones to be generate for each antibody
        self.evaluation = evaluation

        # initialize population
        random.seed()

        self.population = np.random.randint(limits[0], limits[1], size=(self.N, 2))

    def select(self):
        # if n1 is equal N, then no selection is required
        if self.N == self.n1:
            return self.population

        # select the n1 highest fitness
        return self.population[self.fitness.argsort()[-self.n1::][::-1]]

    def clone(self, antibodies):
        clones = []
        for antibody in antibodies:
            clones_antibody = []
            for i in range(0,self.nc):
                clones_antibody.append(antibody)
            clones.append(clones_antibody)

        return clones

    def mutation(self):
        pass

    def replace(self):
        pass

    def clonalg_opt(self):
        t = 1
        while t <= self.max_it:
            self.fitness = np.apply_along_axis(self.evaluation, 1, self.population)
            population_select = self.select()
            clones = self.clone(population_select)
            self.mutation()
            np.apply_along_axis(self.evaluation, 1, self.population)
            self.select()
            self.replace()
            t = t + 1


def eggholder(args):
        x1 = args[0]; x2 = args[1];
        y = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
        return y*(-1) + 1500

clonalg = Clonalg(50, 50, 0, 0.1, (-512, 512), eggholder)
clonalg.clonalg_opt()
    
