"""
Sample Input:
3 50
60 20
100 50
120 30
"""

W = 50
c1, w1 = 60, 20
c2, w2 = 100, 50
c3, w3 = 120, 30

k_weight = 0
k_contents = []
cost = 0

data = [(c1, w1), (c2, w2), (c3, w3)]
cw = []

for i in range(len(data)):
    cw.append(data[i][0] / data [i][1])
print(cw)

while k_weight < W:
    print("k_weight beginning: ", k_weight)
    print("data beginning: ", data)
    max_cw_item = data[cw.index(max(cw))]
    # adding the weight of max value item to a knapsack
    k_weight += max_cw_item[1]
    cost +=  max_cw_item[0]
    # popping out of data the item with max c/w value
    data.pop(data.index(max_cw_item))
    # popping out of cw the highest item
    cw.pop(cw.index(max(cw)))

    print("k_weight end: ", k_weight)
    print("data end: ", data, '\n')

    

# print("The following items are in the knapsack: ")
# print(item for item in k_contents)
print (cost)


