def data_read():
    with open("data/operation_sindoor.txt", "r", encoding="utf-8") as f:
        raw_text = f.read()

    return raw_text

#     print(raw_text)
# data_read()