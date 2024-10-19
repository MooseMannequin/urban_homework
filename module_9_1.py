def apply_all_func(int_list, *functions):
    results = {}
    for function in functions:
        results[function.__name__] = function(int_list)
    return results

print(apply_all_func([1,5,6,7,3,4], min, max, len, sum, sorted))