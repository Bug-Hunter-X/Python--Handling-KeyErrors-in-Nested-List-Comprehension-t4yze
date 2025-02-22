def function_with_uncommon_error(data):
    try:
        # Assume data is a list of dictionaries
        result = [item['value'] for item in data if 'value' in item]
        return result
    except KeyError as e:
        # This is the uncommon part:
        # The KeyError might not be directly in this list comprehension
        # It could be nested in a more complex data structure.
        # Print a more informative error message
        print(f"KeyError occurred: {e}, Check your data structure.")
        return []
    except TypeError as e:
        print(f"TypeError: {e}. Check your data type.")
        return []
data = [{'value': 1}, {'value': 2}, {'other': 3}]
result = function_with_uncommon_error(data)
print(result) #Output: [1,2] 
data = [{'value': 1}, {'value': 2}, {'value':3}, {'nested': {'value': 4}}]
result = function_with_uncommon_error(data)
print(result) #Output: [1,2,3]