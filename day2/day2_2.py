safe_reports = 0

with open("day2_input.txt") as f:
    for line in f:
        levels = [int(level) for level in line.split()]

        for i in range(len(levels)):
            truncated = levels[:i] + levels[i+1:]

            is_safe = True
            is_decreasing = truncated[0] > truncated[1]
            
            for current, next_num in zip(truncated, truncated[1:]):
                if is_decreasing and (current < next_num or abs(current - next_num) > 3 or current == next_num):
                    is_safe = False
                    break

                if not is_decreasing and (current > next_num or abs(current - next_num) > 3 or current == next_num):
                    is_safe = False
                    break
            
            if is_safe:
                safe_reports += 1
                break

print(safe_reports)
