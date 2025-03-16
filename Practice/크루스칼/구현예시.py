def make_graph():
  graph = {
    "vertices": ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    "edges": [
      (7, 'A', 'B'),
      (5, 'A', 'D'),
      (7, 'B', 'A'),
      (9, 'B', 'D'),
      (8, 'B', 'C'),
      (7, 'B', 'E'),
      (8, 'C', 'B'),
      (5, 'C', 'E'),
      (5, 'D', 'A'),
      (9, 'D', 'B'),
      (7, 'D', 'E'),
      (6, 'D', 'F'),
      (5, 'E', 'C'),
      (7, 'E', 'D'),
      (8, 'E', 'F'),
      (9, 'E', 'G'),
      (7, 'E', 'B'),
      (6, 'F', 'D'),
      (8, 'F', 'E'),
      (11, 'F', 'G'),
      (11, 'G', 'F'),
      (9, 'G', 'E')
      ]
    }
  return graph


parent = dict()
rank = dict()

def make_set(node):
  parent[node] = node
  rank[node] = 0

def find(node):
  if parent[node] == node:
    return node
  root = find(parent[node])
  # path-compression기법을 사용하여 한번 find하면 parent를 root로 바꿔버림
  parent[node] = root
  return root


def union(u,v):
  # root의 랭크를 비교하고 짧은쪽이 긴쪽에 붙어야함
  # rank를 ++ 해주는 경우도 추가해야함
  root_u = find(u)
  root_v = find(v)
  
  # union-by-rank 기법
  if rank[root_u] > rank[root_v]:
    parent[root_v] = root_u
    rank[root_u] += 1
  else:
    parent[root_u] = root_v
    rank[root_v] += 1

def kruskal(graph):
  mst = list()

  # 부분집합 확인을 위한 set 만들기
  for node in graph["vertices"]:
    make_set(node)

  # 노드들 연결시켜주기
  edges = sorted(graph["edges"])

  for edge in edges:
    weight, vertex_u, vertex_v = edge

    if find(vertex_u) != find(vertex_v):
      mst.append(edge)
      union(vertex_u,vertex_v)

  return mst


if __name__ == '__main__':
  graph = make_graph()
  answer = kruskal(graph)
  print(answer)