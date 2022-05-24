v_pool = int(input())
flow_p1 = int(input())
flow_p2 = int(input())
hours_missing = float(input())
litres_p1 =  flow_p1 * hours_missing
litres_p2 = flow_p2 * hours_missing
total_litres = litres_p1 + litres_p2
if v_pool >= total_litres:
    full_capacity = (total_litres / v_pool) * 100
    water_p1 = (litres_p1 / total_litres) * 100
    warer_p2 = (litres_p2 / total_litres) * 100
    print(f'The pool is {full_capacity:.2f}% full.'
          f' Pipe 1: {water_p1:.2f}%. Pipe 2: {warer_p2:.2f}%.')
else:
    litre_more = total_litres - v_pool
    print(f'For {hours_missing:.2f} hours the pool overflows with {litre_more:.2f} liters.')