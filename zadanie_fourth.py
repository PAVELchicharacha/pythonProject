def to_set(input_data):
    set_data = set(input_data)
    power: int = len(set_data)

    print("Множество: ", set_data)
    print("Мощность: ", power)


input_data = ['1', '2', '3', '4', '5']
to_set(input_data)
