import random
import sys
import subprocess




def plot_ratio():

    ratios = []
    for total in tqdm.tqdm(range(1, 1000000, 10000)):
        correct = 0
        max = 10000000000000000

        for i in range(total):
            num1 = random.randint(0, max)
            num2 = random.randint(0, max)

            numbers = [num1, num2]
            random.shuffle(numbers)

            first_value = numbers[0]

            guess = random.randint(0, max)

            if (guess < first_value) == (numbers[0] > numbers[1]):
                correct += 1

        ratios.append(correct / total)

    plt.plot(totals, ratios, marker='o')
    plt.xlabel('Total')
    plt.ylabel('Ratio')
    plt.title('Ratio of Correct Guesses vs Total')
    plt.xscale('log')
    plt.yscale('linear')
    plt.grid(True)
    plt.show()



def main():
    print("""
    This is a simple simulation to show that the probability of guessing the correct number is 50%.

    The simulation is as follows:
    1. Two random numbers are generated.
    2. The two numbers are shuffled.
    3. The first number is selected.
    4. A random guess is made.
    """)

    choice = input("Do you want to run the graph function? (yes/no): ").strip().lower()

    if choice == 'yes':
        try:
            import matplotlib.pyplot as plt
                import tqdm
        except ImportError:
            print("Required packages not found. Installing...")
            install('matplotlib')
            install('tqdm')
            import matplotlib.pyplot as plt
            import tqdm


        plot_ratio()
    else:
        main_simulation()

def main_simulation():
    correct = 0
    total = 1000000
    max = 10000000000000000

    for i in range(total):
        num1 = random.randint(0, max)
        num2 = random.randint(0, max)

        numbers = [num1, num2]
        random.shuffle(numbers)

        first_value = numbers[0]

        guess = random.randint(0, max)

        if (guess < first_value) == (numbers[0] > numbers[1]):
            correct += 1
    print(correct / total)

if __name__ == "__main__":
    main()