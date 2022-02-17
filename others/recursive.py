### From YT video "5 Simple Steps for solving Any Recursive Problem" by Reducible

# # Prob. No. 1
# # sum(n) -> (1 + 2 + 3 + ... + n)

# def sum(n):
# 	if n == 0:
# 		return 0
# 	else:
# 	    return n + sum(n-1)

# print(sum(3))

# # Prob. No. 2

# def grid_paths(n, m):
# 	if n == 1 or m == 1:
# 		return 1
# 	return grid_paths(n-1, m) + grid_paths(n, m-1)

# print(grid_paths(1, 1))
# print(grid_paths(3, 3))

# Prob. No. 3

def count_partitions(n, m):
	if n == 0:
		return 1
	if m == 0 or n < 0:
		return 0
	return count_partitions(n-m, m) + count_partitions(n, m-1)

print(count_partitions(9, 5))