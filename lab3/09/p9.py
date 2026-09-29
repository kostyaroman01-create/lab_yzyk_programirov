def check_chain(x, y, z):
    result = (x == y == z)
    print(f"Python: x={x}, y={y}, z={z} -> x == y == z is {result}")

if name == "main":
    check_chain(1, 1, 0)  
    check_chain(1, 1, 1)  
    check_chain(5, 5, 1)  
  