
def error_calculator(array_value):
    new_values_list = [-5, -3, -2, -1, 1, 2, 3, 5]
    bitsum = 0
    counter = 0

    for index in range(len(array_value)):
        if array_value[index] == "1":
            bitsum += new_values_list[index]
            counter += 1

    if counter == 0 or counter == 8:
        raise ValueError
    elif 3 <= counter <= 5:
        error = bitsum
    else:
        error = bitsum / counter

    return error


def pid_controller(error, integral, prev_error, delta_time, kp, ki, kd):
    # Since target is 0, the error is actual (arr position).
    # Proportional:
    p = kp * error

    # Integral:
    integral += error * delta_time
    i = ki * integral

    # Clamp integral to avoid wind-up
    i = min(max(i, -1), 1)
    if error == 0:
        i = 0

    # Derivative:
    d = kd * ((error - previous_error) / delta_time)

    pid = min(max(p + i + d, -0.7), 0.7)
    return pid, i, error