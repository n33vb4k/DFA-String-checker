class Node:
    def __init__(self, state):
        self.state = state
        self.connections = {} # {character: Node} 
        self.acceptance = False

    def add_connections(self, neighbour, characters):
        for c in characters:
            self.connections[c] = neighbour
        self.neighbours.append(neighbour)

    def get_connection(self, character):
        return self.connections.get(character) 
    

def check_string(allNodes, string):
    current = allNodes[0]
    for c in string:
        s = c + ": " + str(current.state) + " -> "
        if c not in current.connections:
            return False 
        current = current.get_connection(c)
        s += str(current.state)
        print(s)
    return current.acceptance


allNodes = []
n = int(input("Enter the number of states: "))
for i in range(n):
    allNodes.append(Node(i + 1))

print('state(1 is start) _ characters(, separated) _ neighbour. Type "e" to finish.')
while True:
    entry = input()
    if entry == "e":
        break
    state, characters, neighbour = entry.split()
    characters = characters.split(",")
    node = allNodes[int(state) - 1]
    node.add_connections(allNodes[int(neighbour) - 1], characters)

acceptance = list(map(int, input("Enter the acceptance states (, separated): ").split(",")))
for i in acceptance:
    allNodes[i - 1].acceptance = True

while True:
    check = input("Enter the string to check: ")
    if check == "":  
        print("String cannot be empty. Try again.")
        continue
    print("Accepted" if check_string(allNodes, check) else "Rejected")
    if input("Do you want to check another string? (y/n): ").lower() == "n":
        break
