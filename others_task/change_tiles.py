side_playground_n = int(input())
width_tile_w = float(input())
length_tile_l = float(input())
width_bench_m = int(input())
length_bench_o = int(input())
time_for_one_tile = 0.2
area_playground = side_playground_n * side_playground_n
area_tile = width_tile_w * length_tile_l
area_bench = width_bench_m * length_bench_o
area_playground -= area_bench
count_tile = area_playground / area_tile
needed_time = count_tile * time_for_one_tile
print(f'{count_tile}')
print(f'{needed_time}')