from deap import base
from deap import creator
from deap import tools

import random
import numpy

import elitism
import scheduler

import time

# problem constants:
HARD_CONSTRAINT_PENALTY = 10  # the penalty factor for a hard-constraint violation

# Genetic Algorithm constants:
POPULATION_SIZE = 300
P_CROSSOVER = 0.8  # probability for crossover
P_MUTATION = 0.35   # probability for mutating an individual
MAX_GENERATIONS = 1500
#MAX_GENERATIONS = 15
HALL_OF_FAME_SIZE = 20

# set the random seed:
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

toolbox = base.Toolbox()

# create the nurse scheduling problem instance to be used:
nsp = scheduler.SchedulingClass(HARD_CONSTRAINT_PENALTY,'data.db')

# define a single objective, maximizing fitness strategy:
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))

# create the Individual class based on list:
creator.create("Individual", list, fitness=creator.FitnessMin)

# create an operator that randomly returns 0 or 1:
toolbox.register("zeroOrOne", random.randint, 0, 1)

# create the individual operator to fill up an Individual instance:
toolbox.register("individualCreator", tools.initRepeat, creator.Individual, toolbox.zeroOrOne, len(nsp))
# create the population operator to generate a list of individuals:
toolbox.register("populationCreator", tools.initRepeat, list, toolbox.individualCreator)


# fitness calculation
def getCost(individual):
    return nsp.getCost(individual),  # return a tuple


toolbox.register("evaluate", getCost)

# genetic operators:
toolbox.register("select", tools.selTournament, tournsize=2)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=1.0/len(nsp))

# Genetic Algorithm flow:
def main():
    start = time.time()

    # create initial population (generation 0):
    population = toolbox.populationCreator(n=POPULATION_SIZE)

	#Set up initial population to total avalibility
    popsub = []
    for act in nsp.Avalibility:
        for item in act[0]:
            popsub.append(item)
    pop = []
    for i in range(0,POPULATION_SIZE):
        pop.append(popsub)

	#Copy known avalibility to initial pop
    for i in range(0,HALL_OF_FAME_SIZE+1):
    	for j in range(0,len(population[0])):
            population[i][j] = pop[i][j]


    # prepare the statistics object:
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("min", numpy.min)
    stats.register("avg", numpy.mean)

    # define the hall-of-fame object:
    hof = tools.HallOfFame(HALL_OF_FAME_SIZE)

    # perform the Genetic Algorithm flow with hof feature added:
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox, cxpb=P_CROSSOVER, mutpb=P_MUTATION,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)


    # perform 2nd Set Genetic Algorithm flow with hof feature added:
    population, logbook = elitism.eaSimpleWithElitism(population, toolbox, cxpb=.9, mutpb=.1,
                                              ngen=MAX_GENERATIONS, stats=stats, halloffame=hof, verbose=True)

    end=time.time()-start
    print ("Time Elapsed: " + str(end) + " seconds")

    # print best solution found:
    best = hof.items[0]
    #print("-- Best Individual = ", best)
    #print("-- Best Fitness = ", best.fitness.values[0])
    #print()
    #print("-- Schedule = ")
    nsp.printScheduleInfo(best)


if __name__ == "__main__":
    main()
