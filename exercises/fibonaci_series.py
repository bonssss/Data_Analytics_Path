def fibonaci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        if a >n:
            break
        series.append(a)
        a, b = b, a + b
    return series

print(fibonaci_series(10))  # Example usage of the fibonaci_series function