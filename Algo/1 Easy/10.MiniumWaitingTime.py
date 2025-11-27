def minimum_waiting_time(queries):  
    # Sort the queries to minimize waiting time
    queries.sort()
    
    total_waiting_time = 0
    n = len(queries)
    
    for i in range(n):
        # The waiting time for the current query is the sum of all previous queries
        # Since the last query has no waiting time, we multiply by (n - i - 1)
        total_waiting_time += queries[i] * (n - i - 1)
    
    return total_waiting_time


result = minimum_waiting_time([3, 2, 1, 2, 6])
print(result)  # Output: 17
