def get_matching_brackets(expression):
    opening_bracket_indexes = []
    sub_expression = []
    for i in range(len(expression)):
        ch = expression[i]
        if ch == '(':
            opening_bracket_indexes.append(i)
        elif ch == ')':
            start_index = opening_bracket_indexes.pop()
            end_index = i
            sub_expression.append(
                expression[start_index:end_index + 1]
            )
    return sub_expression


sub_expressions = get_matching_brackets(input())
[print(exp) for exp in sub_expressions]

# Test Input
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5