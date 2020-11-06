def generate_valid_parentheses(num):
    result = []
    helper(num, num, "", result)
    return result


def helper(left_remain, right_remian, cur, result):
    if left_remain > right_remian or left_remain < 0 or right_remian < 0:
        return

    if right_remian == 0:
        result.append(cur)
        return

    helper(left_remain-1, right_remian, cur + "(", result)
    helper(left_remain, right_remian-1, cur+")", result)


print("All combinations of balanced parentheses are: " +
      str(generate_valid_parentheses(2)))
print("All combinations of balanced parentheses are: " +
      str(generate_valid_parentheses(3)))
