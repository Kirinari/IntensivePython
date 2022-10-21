def f_generator(f, words):
    for line in f:
        arr = line.strip().lower().split()
        for i in words:
            if i in arr:
                yield line
                break
