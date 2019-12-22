import random


class GeneticAlgorithm:
    def __init__(self):
        self.VERTICES_LEN = 5
        # Название вершин.
        self.VERTICES = [chr(i) for i in range(65, 65 + self.VERTICES_LEN)]
        self.graph = dict()
        self.populations = [0] * 5

        self.init_graph()
        self.init_shuffle_populations()

    # Инициализация графа со случайными ребрами.
    def init_graph(self):
        for i in range(self.VERTICES_LEN-1):
            self.graph[self.VERTICES[i]] = dict()
            for j in range(i+1, len(self.VERTICES)):
                self.graph[self.VERTICES[i]][self.VERTICES[j]] = random.randint(1, 10)

    # Инициализация случайных популяций.
    def init_shuffle_populations(self):
        for i in range(len(self.populations)):
            self.populations[i] = self.VERTICES.copy()
            random.shuffle(self.populations[i])

    # Метод для вывода длины ребер.
    def get_edges_length(self, vx_list: list) -> int:
        length = 0
        for i in range(len(vx_list)-1):
            vx = vx_list[i]
            vx_next = vx_list[i+1]
            length += self.graph[min(vx, vx_next)][max(vx, vx_next)]

        vx_last = vx_list[-1]
        vx_first = vx_list[0]
        length += self.graph[min(vx_last, vx_first)][max(vx_last, vx_first)]
        return length

    # Метод для вывода графа.
    def print_graph(self):
        print(f'{"-"*8} GRAPH {"-"*8}')
        print(f'    {"   ".join(self.VERTICES)}')
        gap = 1
        for vx_row in self.graph:
            edges = [f' {vx_row} {" -  "*gap}']
            for vertex_col in self.graph[vx_row]:
                edges.append(f'{self.graph[vx_row][vertex_col]:^3} ')
            print(''.join(edges))
            gap += 1

    # Метод для вывода популяций.
    def print_populations(self):
        for pop in self.populations:
            print(' -> '.join(pop))


if __name__ == '__main__':
    ga = GeneticAlgorithm()
    ga.print_graph()
    path = ['A', 'B', 'C']
    print(ga.get_edges_length(path))
    ga.print_populations()