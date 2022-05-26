def distribute_the_wealth(population, min_wealth):
    for i in range(len(population)):
        if population[i] < min_wealth:
            max_num_index = population.index(max(population))
            diff = minimum_wealth - population[i]
            population[i] += diff
            population[max_num_index] -= diff
    return population

def check_for_equal_distribution(first_function, min_wealth):
    for number in first_function:
        if number < min_wealth:
            return "No equal distribution possible"
    return population


population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
popultaion_with_distributed_wealth = distribute_the_wealth(population, minimum_wealth)
print(check_for_equal_distribution(popultaion_with_distributed_wealth, minimum_wealth))