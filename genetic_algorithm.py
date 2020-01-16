import random
import copy

from TaskPackage.genetic_algorithm.data import inputMatrix


class GeneticAlgorithm:
    def __init__(self, vertices_len):
        self.VERTICES_LEN = vertices_len
        # Название вершин.
        self.VERTICES = [chr(i) for i in range(65, 65 + self.VERTICES_LEN)]
        self.graph = dict()
        self.POPULATIONS_LEN = 10
        self.populations = [0] * self.POPULATIONS_LEN

        self.init_graph()
        self.init_shuffle_populations()

    # Инициализация графа со случайными ребрами.
    # def init_graph(self):
    #     for i in range(self.VERTICES_LEN-1):
    #         self.graph[self.VERTICES[i]] = dict()
    #         for j in range(i+1, len(self.VERTICES)):
    #             self.graph[self.VERTICES[i]][self.VERTICES[j]] = random.randint(1, 10)

    def init_graph(self):
        for i in range(self.VERTICES_LEN-1):
            self.graph[self.VERTICES[i]] = dict()
            for j in range(i+1, len(self.VERTICES)):
                self.graph[self.VERTICES[i]][self.VERTICES[j]] = inputMatrix[i][j]

    # Инициализация случайных популяций.
    def init_shuffle_populations(self):
        for i in range(self.POPULATIONS_LEN):
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

    def mutation_populations(self):
        pops_temp = copy.deepcopy(self.populations)
        for i in range(self.VERTICES_LEN-1):
            vx1_i = random.randint(0, self.VERTICES_LEN-1)
            while True:
                vx2_i = random.randint(0, self.VERTICES_LEN-1)
                if vx1_i != vx2_i:
                    break
            pops_temp[i][vx1_i], pops_temp[i][vx2_i] = pops_temp[i][vx2_i], pops_temp[i][vx1_i]
        self.populations.extend(pops_temp)
        self.populations.sort(key=lambda k: self.get_edges_length(k))
        self.populations = self.populations[:self.POPULATIONS_LEN]

    def cycle_populations(self, count):
        for i in range(count):
            self.mutation_populations()
            self.print_populations()

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
        for popul in self.populations:
            print(f'{" -> ".join(popul)} | all = {self.get_edges_length(popul)}')
        print('-'*25)


if __name__ == '__main__':
    ga = GeneticAlgorithm(11)
    ga.print_graph()
    ga.print_populations()
    ga.cycle_populations(50)
