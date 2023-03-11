def sum_provisions(default_provisions: dict, provisions_modifiers: dict):
    summed_provisions = {}

    for key, provision in provisions_modifiers.items():
        if provision == None:
            summed_provisions[key] = 0
        else:
            summed_provisions[key] = default_provisions[key] + provision

    return summed_provisions
