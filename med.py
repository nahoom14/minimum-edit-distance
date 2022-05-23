#returns minimum edit distance of two words
def min_edit_distance(source, target):
    n = len(source)
    m = len(target)

    #create 2d matrix adding extra cell for empty string
    distance = [[0 for i in range(n+1)] for j in range(m+1)]

    #assign values to first row and column
    for k in range(n + 1):
        distance[k][0] = k
        distance[0][k] = k
    
    #print matrix
    for row in distance:
        print(row)


# print("Enter source word:")
# t = input()

# print("Enter target word:")
# s = input()

#client code
t, s = "intention", "detention"

min_edit_distance(t, s)