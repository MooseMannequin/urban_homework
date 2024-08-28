calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    tuple = (len(string), string.upper(), string.lower())
    print(tuple)

def is_contains(string, list_to_search):
    count_calls()
    given_string = string.lower()
    given_list = 'list'
    list_index = 0
    true_false = True
    for id in range(len(list_to_search)):
        given_list = list_to_search[list_index].lower()
        if given_string == given_list:
            true_false = True
            break
        elif given_string != given_list and list_index == len(list_to_search) - 1:
            true_false = False
            break
        elif given_string != given_list:
            list_index += 1

    print(true_false)

string_info(str('ultraviOlence'))
string_info(str("what's_up'"))

is_contains('Baby',['Byab', 'lol', 'rooKLyn'])
is_contains('winner', ['winer', 'yes', 'dump', 'Lana', '136', 'whAt'])
is_contains('blUe', ['14', 'BluE', 'wow'])

print(calls)