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
    input_indices, output_indices = exp.split('->')
    input_indices = input_indices.split(',')[0]
    output_indices = output_indices.strip()
    x = input_indices == output_indices[::-1]
    return x
