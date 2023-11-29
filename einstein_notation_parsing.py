def validate_matrix_multiplication(exp, ope):
    input_indices, output_indices = exp.split('->')
    input_indices = input_indices.split(',')
    output_indices = output_indices.strip()
    pred_output = f"{input_indices[0][0]}{input_indices[-1][-1]}"
    if len(input_indices) != len(ope):
        return False
    if pred_output != output_indices:
        return False
    for ind in range(len(input_indices)):
        if ind:
            if nxt_i != input_indices[ind][0]:
                return False
        nxt_i = input_indices[ind][1]
    return True


def validate_transpose(exp):
    if '->' not in exp:
        print("Output missing! ")
        return False
    input_indices, output_indices = exp.split('->')
    input_indices = input_indices.split(',')[0]
    output_indices = output_indices.strip()
    if len(output_indices) == 1:
        return False
    return input_indices == output_indices[::-1]


def validate_diagonal_sum(exp):
    if "->" not in exp:
        print("Output missing! ")
        return False
    input_indices, output_indices = exp.split('->')
    input_indices = input_indices.split(',')[0]
    output_indices = output_indices.strip()
    if len(output_indices) == len(input_indices) == 1:
        return False
    return input_indices[1] == input_indices[0] and len(output_indices) == 0


def validate_sum(exp):
    if "->" not in exp:
        print("Output missing! ")
        return False
    input_indices, output_indices = exp.split('->')
    input_indices = input_indices.split(',')[0]
    output_indices = output_indices.strip()
    return (len(input_indices) == 2 and
            len(output_indices) == 0 and
            len(input_indices) == len((set(input_indices))))


def validate_row_sum(exp):
    if "->" not in exp:
        print("Output missing! ")
        return False
    input_indices, output_indices = exp.split('->')
    input_indices = input_indices.split(',')[0]
    output_indices = output_indices.strip()
    if len(input_indices) == 1:
        return False
    return input_indices[1] == input_indices[0] and output_indices == input_indices[0]
