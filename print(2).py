from tqdm import tqdm

import matplotlib.pyplot as plt

max = int(input("Enter the maximum value of i: "))+1



def hi(max):
    sum1_list = []
    sum2_list = []
    intersection_point = None



    for i in tqdm(range(1, max), desc="Calculating sums"):
        sum1 = sum(range(1, i))
        sum2 = sum(range(i, max))
        sum1_list.append(sum1)
        sum2_list.append(sum2)

    for i in tqdm(range(len(sum1_list) - 1), desc="Finding intersection"):
        if sum1_list[i] <= sum2_list[i] and sum1_list[i + 1] >= sum2_list[i + 1]:
            x1, y1 = i + 1, sum1_list[i]
            x2, y2 = i + 2, sum1_list[i + 1]
            x3, y3 = i + 1, sum2_list[i]
            x4, y4 = i + 2, sum2_list[i + 1]
            
            intersection_point = x1 + (x2 - x1) * (y3 - y1) / ((y2 - y1) - (y4 - y3))
            break

    plt.plot(range(1, max), sum1_list, label='Sum1 (1 to i-1)')
    plt.plot(range(1, max), sum2_list, label='Sum2 (i to max-1)')
    plt.axvline(x=intersection_point, color='r', linestyle='--', label=f'Intersection at i={intersection_point}')
    plt.xlabel('i')
    plt.ylabel('Sum')
    plt.title('Cumulative Sums Comparison')
    plt.legend()
    plt.show()
    return intersection_point


hi(max)
