def min_edit_distance(target, source):
    n = len(target)
    m = len(source)

    distance = [[0 for i in range(n+1)] for j in range(m+1)]

    
    for k in range(n + 1):
        distance[k][0] = k
        distance[0][k] = k
    
    for row in distance:
        print(row)


# print("Enter source word:")
# t = input()

# print("Enter target word:")
# s = input()

t, s = "intention", "detention"

min_edit_distance(t, s)