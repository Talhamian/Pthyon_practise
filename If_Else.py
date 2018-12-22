table_value = int(input("Enter Table Value: "))
start_limit = int(input("Enter Start Limit: "))
end_limit = int(input("Enter End Limit: "))
if end_limit > start_limit:
    for i in range(start_limit,end_limit+1):
        print("{} * {}  = {}".format(table_value,i,table_value*i))
else:
    print("Error, end limit must be greater than the start limit.")
