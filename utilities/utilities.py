def validate_inputs(*args):
    for arg in args:
        if not arg:
            return False
    return True

def convert_to_floats(*args):
    float_args = list()
    for arg in args:
        float_args.append(float(arg))
    return float_args