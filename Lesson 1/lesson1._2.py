def buggy_function(a, b):
    print(">>> enteringbuggy_function")          # entry
    result = a * (b +1)                          # suspicious line
    print(f"result after suspicious line:{result}")  # inspect
    print("=== before return===")                # checkpoint
    return result

buggy_function(1,2)
print(buggy_function(1,2))