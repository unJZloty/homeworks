data_structure = [[1, 2, 3],{'a': 4, 'b': 5},(6, {'cube': 7, 'drum': 8}),"Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]

def calculate_structure_sum (ds):
    result = []
    for i in ds:
        if isinstance(i, int):
            result.append(i)
        elif isinstance(i, str):
            result.append(len(i))
        elif isinstance(i, dict):
            result.append(calculate_structure_sum(list(i.keys())))
            result.append(calculate_structure_sum(list(i.values())))
        else:
            if len(i) > 0:
                result.append(calculate_structure_sum(i))
    else:
        return sum(result)

print(calculate_structure_sum(data_structure))