data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
  ]
def calculate_structure_sum(data_structure):
  list_ = []
  for i in data_structure:
    if isinstance(i, int):
      list_.append(i)
    elif isinstance(i, str):
      list_.append(len(i))
    elif isinstance(i, dict):
      list_.append(calculate_structure_sum(list(i.keys())))
      list_.append(calculate_structure_sum(list(i.values())))
    else:
      if len(i) > 0:
        list_.append(calculate_structure_sum(i))
  else:
    return sum(list_)

print(calculate_structure_sum(data_structure))