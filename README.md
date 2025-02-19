# Cash Register System: Algorithms for Change Calculation

This project implements two functions for a cash register system that determines the optimal way to give change to a customer using two different algorithms: a greedy algorithm and a dynamic programming algorithm.

## Algorithm Descriptions

1. **Greedy Algorithm (`find_coins_greedy`)**:

   - The algorithm starts with the largest coin and subtracts it from the remaining amount until the desired sum is reached.
   - This algorithm doesn't always guarantee the optimal solution, but it often gives a good result for coin systems like this one (50, 25, 10, 5, 2, 1).

2. **Dynamic Programming Algorithm (`find_min_coins`)**:
   - This approach uses dynamic programming to find the minimum number of coins required to make the desired sum.
   - The algorithm calculates the optimal solution for each amount from 0 to the desired amount, storing the number of coins for each possibility. In the end, we get the minimum number of coins for the desired amount.
   - Dynamic programming always guarantees the minimum number of coins, but its time complexity might be higher compared to the greedy algorithm.

```

### Output:

```

Case when amount = 113:
A greedy algorithm for 113: {50: 2, 10: 1, 2: 1, 1: 1} (Time taken: 0.000010 seconds)
A dynamic programming algorithm for 113: {1: 1, 2: 1, 10: 1, 50: 2} (Time taken: 0.000449 seconds)

```

## Time Complexity

1. **Greedy Algorithm**:
   - **Time Complexity**: O(n), where `n` is the number of different coin denominations.
   - The algorithm runs quickly since it just iterates through the coin list and performs a few division and subtraction operations.

2. **Dynamic Programming Algorithm**:
   - **Time Complexity**: O(amount * n), where `amount` is the amount to be returned, and `n` is the number of different coin denominations.
   - Dynamic programming requires storing additional information for each amount, which significantly increases the runtime for larger sums.

## Performance Comparison

- **Greedy Algorithm** has the advantage in speed, especially for smaller amounts. However, it might not always provide the minimal coin count in cases with specific coin denominations.
- **Dynamic Programming Algorithm** is slower due to the need to compute values for each amount, but it always provides the optimal result for the minimal coin count.

## Conclusions

- The greedy algorithm is more time-efficient but does not guarantee the optimal result. It is suitable for scenarios where speed is essential, and the coin denominations do not lead to situations where the algorithm might fail.
- Dynamic programming guarantees the optimal result, but its time complexity can be significant for large amounts, making it less efficient than the greedy algorithm for larger sums.

```
