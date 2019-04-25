# nodes = ('1', '2', '3', '4', '5', '6')
# distances = {
#     '1': {'6': 14, '3': 9, '2': 7},
#     '2': {'1': 7, '3': 10, '4': 15},
#     '3': {'1': 9, '2': 10, '4': 11, '6': 2},
#     '4': {'2': 15, '3': 11, '5': 6},
#     '5': {'4': 6, '6': 9},
#     '6': {'1': 14, '3': 2, '5': 9}}
nodes = []
distances = {}
with open("input3.txt", "r") as file:
  count = int(file.readline())
  nodes = [str(i) for i in range(1, count+1)]
  nodes = tuple(nodes)
  for _ in range(count):
        line = file.readline().strip().split(" ")
        tmp = len(line)//2
        distances[str(_ + 1)] = {}
        for i in range(tmp):
            distances[str(_ + 1)][line[i*2+1]] = int(line[i*2+2])


unvisited = {node: None for node in nodes} #using None as +inf
visited = {}
current = '1'
currentDistance = 0
unvisited[current] = currentDistance

while True:
    for neighbour, distance in distances[current].items():
        if neighbour not in unvisited: continue
        newDistance = currentDistance + distance
        if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
            unvisited[neighbour] = newDistance
    visited[current] = currentDistance
    del unvisited[current]
    if not unvisited: break
    candidates = [node for node in unvisited.items() if node[1]]
    current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

print(visited)
with open("output3.txt", "w") as file:
    for i in visited:
        print(visited[i], file=file)
