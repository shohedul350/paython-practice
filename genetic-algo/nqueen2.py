import random

def random_chromosome(size):
    return [random.randint(1, size) for _ in range(size)]

def fitness(chromosome):
    size = len(chromosome)
    horizontal_collisions = sum(chromosome.count(queen) - 1 for queen in chromosome) // 2

    left_diagonal = [0] * (2 * size)
    right_diagonal = [0] * (2 * size)

    for i in range(size):
        left_diagonal[i + chromosome[i] - 1] += 1
        right_diagonal[size - i + chromosome[i] - 2] += 1

    diagonal_collisions = sum((counter - 1) / (size - abs(i - size + 1)) for i, counter in enumerate(left_diagonal + right_diagonal))

    return int((size * (size - 1)) / 2 - (horizontal_collisions + diagonal_collisions))

def probability(chromosome, fitness):
    return fitness(chromosome) / maxFitness

def random_pick(population, probabilities):
    total = sum(probabilities)
    r = random.uniform(0, total)
    upto = 0

    for chromosome, prob in zip(population, probabilities):
        if upto + prob >= r:
            return chromosome
        upto += prob

def reproduce(x, y):
    n = len(x)
    c = random.randint(0, n - 1)
    return x[:c] + y[c:]

def mutate(x):
    n = len(x)
    c = random.randint(0, n - 1)
    m = random.randint(1, n)
    x[c] = m
    return x

def genetic_queen(population, fitness):
    mutation_probability = 0.03
    new_population = []
    probabilities = [probability(chrom, fitness) for chrom in population]

    for _ in range(len(population)):
        x = random_pick(population, probabilities)
        y = random_pick(population, probabilities)
        child = reproduce(x, y)

        if random.random() < mutation_probability:
            child = mutate(child)

        print_chromosome(child)
        new_population.append(child)

        if fitness(child) == maxFitness:
            break

    return new_population

def print_chromosome(chrom):
    print("Chromosome = {}, Fitness = {}".format(chrom, fitness(chrom)))

if __name__ == "__main__":
    nq = int(input("Enter Number of Queens: "))
    maxFitness = (nq * (nq - 1)) // 2
    population = [random_chromosome(nq) for _ in range(100)]
    generation = 1

    while maxFitness not in [fitness(chrom) for chrom in population]:
        print(f"=== Generation {generation} ===")
        population = genetic_queen(population, fitness)
        print("\nMaximum Fitness = {}".format(max(fitness(n) for n in population)))
        generation += 1

    chrom_out = [chrom for chrom in population if fitness(chrom) == maxFitness][0]
    print("\nSolved in Generation {}!".format(generation - 1))
    print("\nOne of the solutions:")
    print_chromosome(chrom_out)

    board = [["x"] * nq for _ in range(nq)]

    for i, j in enumerate(chrom_out):
        board[nq - j][i] = "Q"

    def print_board(board):
        for row in board:
            print(" ".join(row))

    print("\nFinal Chessboard Configuration:")
    print_board(board)