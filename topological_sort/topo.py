from collections import defaultdict  # used so that no key error comes...


def topological_sort(vertices, edges):

    # create graph
    graph = create_graph(edges)

    # pre_req dict
    pre_req_dict = {vertex: 0 for vertex in range(vertices)}

    # fill pre_req_dict with graph..
    for vertex in graph:
        for pre_vertex in graph[vertex]:
            pre_req_dict[pre_vertex] += 1

    # create que for vertices who have 0 prerequist
    # jo kisi ke dependency nahin usko hatao
    que = [vertex for vertex in pre_req_dict if pre_req_dict[vertex] == 0]

    topological_order = []

    while que:
        cur_vertex = que.pop(0)
        topological_order.append(cur_vertex)

        for neighbour in graph[cur_vertex]:
            pre_req_dict[neighbour] -= 1
            if pre_req_dict[neighbour] == 0:
                que.append(neighbour)

    if len(topological_order) == vertices:
        return topological_order

    else:
        []


def create_graph(edges):
    graph = defaultdict(list)

    for vertex, pre_vertex in edges:
        graph[vertex].append(pre_vertex)
    return graph


def main():
    print("Topological sort: " +
          str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
          str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
          str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))


main()
