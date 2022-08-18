count_queries = int(input())
num_stack = []
for _ in range(count_queries):
    query = input()
    if query.startswith("1"):
        name_query, number = query.split()
        num_stack.append(int(number))
    elif query == "2" and num_stack:
        num_stack.pop()
    elif query == "3" and num_stack:
        print(max(num_stack))
    elif query == "4" and num_stack:
        print(min(num_stack))
reversed_num_stack = []
while num_stack:
    reversed_num_stack.append(str(num_stack.pop()))
print(", ".join(reversed_num_stack))
