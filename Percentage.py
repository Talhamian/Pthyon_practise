total_sale = float(input("Enter sales in rupees (-1 to end): "))
while total_sale != -1:
    print("Salary is :Rs. {}".format((total_sale * 0.09) + 200))
    total_sale = float(input("Enter sales in rupees (-1 to end): "))
