safe_reports = 0

with open("day2_input.txt") as f:
    for line in f:
        levels = [int(level) for level in line.split()]
        is_decreasing = levels[0] > levels[1]
        is_safe = True

        for current, next_num in zip(levels, levels[1:]):
            if is_decreasing and (current < next_num or abs(current - next_num) > 3 or current == next_num):
                is_safe = False
                break
            
            if not is_decreasing and (current > next_num or abs(current - next_num) > 3 or current == next_num):
                is_safe = False
                break
        
        if is_safe:
            safe_reports += 1

print(safe_reports)
