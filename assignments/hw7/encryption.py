def encode(message, key):
    acc = ""
    for i in message:
        var = ord(i)
        shift = var + key
        switch = chr(shift)
        acc = acc + switch
    return acc


def encode_better(message, key):
    message = message.upper()
    key = key.upper()
    keyindex = 0
    acc = ""
    for i in range(len(message)):
        messageval = ord(message[i]) - ord("A")
        keyval = ord(key[keyindex]) - ord("A")
        subtotal = messageval + keyval
        total = subtotal % 26  # modding by 26 so it looks back to A after Z
        total = total + ord("A")  # restoring ascii values that were subtracted line 65-66
        total = chr(total)  # converting ascii values back to characters
        acc = acc + total  # adding total to accumulator
        keyindex = keyindex + 1
        keyindex = keyindex % len(key)
    print(acc)