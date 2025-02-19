import timeit

coins = [50, 25, 10, 5, 2, 1]

# A greedy algorithm for finding coins
def find_coins_greedy(amount):
    result = {}
    
    for coin in coins:
        count = amount // coin  # Calculate the number of coins of the current denomination
        
        if count > 0:
            result[coin] = count

            # Subtract the amount that has already been covered
            amount -= count * coin  
        
    return result

# A dynamic programming algorithm for finding the minimum number of coins
def find_min_coins(amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    # Array to store the coin used for each amount
    coins_used = [[] for _ in range(amount + 1)]
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if dp[i - coin] + 1 < dp[i]:
                    dp[i] = dp[i - coin] + 1
                    coins_used[i] = coins_used[i - coin].copy()
                    coins_used[i].append(coin)
    
    result = {}

    # Reconstruct the result
    for coin in coins_used[amount]:
        result[coin] = result.get(coin, 0) + 1
    
    return result

if __name__ == "__main__":

    # Test case
    amount = 113

    # Measure time for the greedy algorithm
    greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1)

    # Measure time for the dynamic programming algorithm
    min_coins_time = timeit.timeit(lambda: find_min_coins(amount), number=1)

    greedy_result = find_coins_greedy(amount)
    min_coins_result = find_min_coins(amount)

    print(f"\nCase when amount = {amount}:")
    print(f"A greedy algorithm for {amount}: {greedy_result} (Time taken: {greedy_time:.6f} seconds)")
    print(f"A dynamic programming algorithm for {amount}: {min_coins_result} (Time taken: {min_coins_time:.6f} seconds)")