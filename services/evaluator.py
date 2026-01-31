import types

class CodeExecutionError(Exception):
    pass


def evaluate_code(code: str, function_name: str, test_cases: list):
    restricted_globals = {
        "__builtins__": {}
    }

    restricted_locals = {}

    try:
        exec(code, restricted_globals, restricted_locals)
    except Exception as e:
        raise CodeExecutionError(f"Code execution failed: {str(e)}")

    if function_name not in restricted_locals:
        raise CodeExecutionError("Required function not found")

    func = restricted_locals[function_name]

    if not isinstance(func, types.FunctionType):
        raise CodeExecutionError("Submitted object is not a function")

    passed = 0

    for case in test_cases:
        try:
            result = func(**case["input"])
        except Exception:
            return {
                "status": "runtime_error",
                "passed": passed,
                "total": len(test_cases)
            }

        if result == case["output"]:
            passed += 1

    if passed == len(test_cases):
        status = "correct"
    elif passed > 0:
        status = "partially_correct"
    else:
        status = "incorrect"

    return {
        "status": status,
        "passed": passed,
        "total": len(test_cases)
    }
