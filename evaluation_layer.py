def evaluate(result, reason):
    if result == "PASS":
        return "Test passed. Observed behavior matches the requirement."
    else:
        return f"Test failed. {reason}. This indicates incorrect application behavior."