def transform(legacy_data: dict):

    return {m.lower(): i for i, j in legacy_data.items() for m in j}
