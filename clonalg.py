import matplotlib.pyplot as plt
import numpy as np
import math
import random

class Clonalg:
    def __init__(self, max_it, n1, n2, b, limits, evaluation):
        self.max_it = max_it;
        self.N = n1;
        self.n1 = n1;
        self.n2 = n2;
        self.b = b;
        self.nc = b * self.N;
        self.evaluation = evaluation

        # initialize population
        random.seed()

        self.population = np.random.randint(limits[0], limits[1], size=(self.N, 2))

    def roulette(self):
        new_population = np.empty((self.N, 2))
        new_fitness = np.empty((self.N, 1))

        t = np.sum(self.fitness);
        for i in range(0, self.N):
            n = random.uniform(0, t)
            s = 0;
            for j in range(0, self.N):
                s += self.fitness[j];
                if(s >= n):
                    new_population[i] = self.population[j]
                    new_fitness[i]    = self.fitness[j]
                    break

        self.population = new_population
        self.fitness = new_fitness

    def clone(self):
        pass

    def mutation(self):
        pass

    def replace(self):
        pass

    def clonalg_opt(self):
        t = 1
        while t <= self.max_it:
            self.fitness = np.apply_along_axis(self.evaluation, 1, self.population)
            self.roulette()
            self.clone()
            self.mutation()
            np.apply_along_axis(self.evaluation, 1, self.population)
            self.roulette()
            self.replace()
            t = t + 1


def eggholder(args):
        x1 = args[0]; x2 = args[1];
        y = -(x2 + 47)*math.sin(math.sqrt(abs(x2 + x1/2 + 47))) - x1*math.sin(math.sqrt(abs(x1 - (x2 + 47))))
        return y*(-1) + 1500

clonalg = Clonalg(50, 50, 0, 0.1, (-600, 600), eggholder)
clonalg.clonalg_opt()
    
