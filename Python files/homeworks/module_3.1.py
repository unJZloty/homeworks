calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    tuple = (len(string), string.upper(), string.lower())
    return tuple
def is_contains (string, list_to_search):
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() in list_to_search[i].lower():
            return True
    return False

print(string_info('Universe'))
print(string_info('Puzzle'))
print(string_info('Сороконожка'))
print(is_contains('Universe', ['UniVErsuM', 'University', 'UnIvErSe']))
print(is_contains('Ball', ['Football', 'BaseBall']))
print(is_contains('BaseBall', ['Football', 'Ball']))
print(is_contains('Автобус', ['Электробус', 'Бус']))
print(calls)