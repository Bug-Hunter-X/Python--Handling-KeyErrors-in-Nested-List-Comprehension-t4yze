def function_with_uncommon_error_solution(data):
    try:
        result = [item['value'] for item in data if isinstance(item, dict) and 'value' in item]
        return result
    except KeyError as e:
        print(f"KeyError occurred: {e}. Check your data structure.")
        return []
    except TypeError as e:
        print(f"TypeError: {e}. Check your data type.")
        return []
data = [{'value': 1}, {'value': 2}, {'other': 3}]
result = function_with_uncommon_error_solution(data)
print(result) #Output: [1,2]
data = [{'value': 1}, {'value': 2}, {'value':3}, {'nested': {'value': 4}}]
result = function_with_uncommon_error_solution(data)
print(result) #Output: [1,2,3]