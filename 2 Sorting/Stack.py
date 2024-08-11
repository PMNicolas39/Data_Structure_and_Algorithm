def number_monster(strengths):
    battlefield = []
    result = []
    for monster in strengths:
        # remove weaker from battlefield
        while battlefield and battlefield[-1] <= monster:
            # pop the last element. At this time, new monster isn't still added in stack
            battlefield.pop()
        # Append strength in battlefield
        battlefield.append(monster)
        # append monster in result
        result.append(len(battlefield))
    return result


def stack(num_cases):
    result3 = []
    for _ in range(num_cases):
        num_monster = int(input())
        num_strength = list(map(int, input().split()))
        result2 = number_monster(num_strength)
        result2_str = " ".join(map(str,result2))
        result3.append(result2_str)
    return result3


num_case = int(input())
results = stack(num_case)
for j in results:
    print(j)
