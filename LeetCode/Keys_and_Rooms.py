'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
Your goal is to visit all the rooms. 
However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it. 
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.
'''

def canVisitAllRooms(rooms):
    visited = [0 for i in range(len(rooms))]
    visited[0] = 1


    def dfs(node):
        visited[node] = 1
        
        for key in rooms[node]:
            if visited[key] == 0:
                dfs(key)

    dfs(0)

    for i in visited:
        if i == 0:
            return False
    return True

print(canVisitAllRooms([[1],[2],[3],[]]))
print(canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))