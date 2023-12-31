# Дан невзвешенный/взвешенный неориентированный/ориентированный граф,
# содержащий N вершин и M ребер, представленный множеством ребер/матрицей
# смежности/списком смежности/матрицей инцидентности.

# Составить список ребер/матрицу смежности/список
# смежности/матрицу инцидентности данного графа.



# Тут надо знать только какие есть виде представлений
# https://github.com/zernovga/Algorithms_and_Data_Structures_Course/blob/main/Lections/Lection_6.pdf


# множества ребёр - [(от какой вершины), (к какой вершине)]
# (
#     [1, 2],
#     [1, 3],
#     [2, 3],
# )

# Матрица смежности - (Eсли ориентирован)
# [
#     [1, 1, 1],
#     [0, 1, 1],
#     [0, 0, 1],
# ]

# Список смежности - (Eсли ориентирован)
# [
#     [2, 3],
#     [3],
#     [],
# ]

# Матрица инцидентности - (Eсли ориентирован) (смотрим по рёбрам)
# [
#     [1, 1, 0],
#     [0, -1, 1],
#     [-1, 0, -1],
# ]
