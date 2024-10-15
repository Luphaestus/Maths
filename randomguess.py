import random
import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--trusted-host", "pypi.org", "--trusted-host", "files.pythonhosted.org"])

def simulate(total):
    max_value = 10000000000000000
    correct = 0
    for i in range(total):
        num1 = random.randint(0, max_value)
        num2 = random.randint(0, max_value)

        numbers = [num1, num2]
        random.shuffle(numbers)

        first_value = numbers[0]

        guess = random.randint(0, max_value)

        if (guess < first_value) == (numbers[0] > numbers[1]):
            correct += 1
    return correct

def plot_ratio(max=100):
    import matplotlib.pyplot as plt
    import tqdm
    import numpy as np

    totals = np.logspace(np.log10(max * 1000), 0, num=max).astype(int)
    ratios = []

    for total in tqdm.tqdm(totals):
        correct = simulate(total)
        ratios.append(correct / total)
    plt.plot(totals, ratios, marker='o')
    plt.xlabel('Total')
    plt.ylabel('Ratio')
    plt.title('Ratio of Correct Guesses vs Total')
    plt.suptitle(f"Percentage of correct guesses after {totals[-1]} simulations is {ratios[0] * 100:.4f}%")
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

        max_value = input("Enter the maximum number of points for the graph function (default is 100): ").strip()
        if not max_value:
            max_value = 100
        else:
            max_value = int(max_value)

        plot_ratio(max=max_value)
    else:
        num_iterations = input("Enter the number of iterations for the main simulation (default is 1000000): ").strip()
        if not num_iterations:
            num_iterations = 1000000
        else:
            num_iterations = int(num_iterations)
        main_simulation(total=num_iterations)

def main_simulation(total=100):
    correct = simulate(total)
    print(correct / total)

if __name__ == "__main__":
    main()
