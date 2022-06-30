count_electrons = int(input())
shell_list = []
count_shells = 0
while count_electrons > 0:
    count_shells += 1
    max_electrons_in_current_shell = 2 * count_shells ** 2
    if count_electrons < max_electrons_in_current_shell:
        max_electrons_in_current_shell = count_electrons
    count_electrons -= max_electrons_in_current_shell
    shell_list.append(max_electrons_in_current_shell)
print(shell_list)