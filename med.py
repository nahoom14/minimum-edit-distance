#returns minimum edit distance of two words
def min_edit_distance(source, target, display, ins_cost, del_cost, subs_cost):
    n = len(source)
    m = len(target)

    #create 2d matrix adding extra cell for empty string
    distance = [[0 for i in range(n+1)] for j in range(m+1)]

    #assign values to first row and column
    for k in range(len(distance)):
        distance[k][0] = k

    for j in range(len(distance[0])):
            distance[0][j] = j

    for row in range(1, len(distance)):
        for col in range(1, len(distance[0])):
            if(source[col - 1] == target[row - 1]):
                distance[row][col] = distance[row - 1][col - 1]
            else:
                x = min(distance[row][col - 1], distance[row - 1][col], distance[row - 1][col - 1]) #insert delete replace
                if(x == distance[row][col - 1]):
                    distance[row][col] = distance[row][col - 1] + ins_cost
                elif(x == distance[row - 1][col]):
                    distance[row][col] = distance[row - 1][col] + del_cost
                else:
                    distance[row][col] = distance[row - 1][col - 1] + subs_cost

    if(display):
        #print matrix
        for row in distance:
            print(row)

    return distance[len(distance) - 1][len(distance[0]) - 1]


#as for words
print("Enter source word:")
t = input()

print("Enter target word:")
s = input()

#ask for cost values
print("Enter insertion cost")
i = input()
print("Enter deletion cost:")
d = input()
print("Enter substitution cost:")
s = input()

#should matrix be displayed?
print("Display matrix?[Y|N]")
d = input()


if(d == "Y"):
    choice = True
else:
    choice = False

print("The minimum edit distance is: " , min_edit_distance(t, s, choice, i, d, s))