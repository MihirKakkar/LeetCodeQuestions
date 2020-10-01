# You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from cityAi to cityBi. 
# Return the destination city, that is, the city without any path outgoing to another city.

# It is guaranteed that the graph of paths forms a line without any loop, therefore, there will be exactly one destination city.

def destCity(paths):
    starts = {}
    for i in paths:
        starts[i[0]] = i[1]

    return [i[1] for i in paths if i[1] not in starts][0]

print(destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
