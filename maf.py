def MA(algorithm, word, sup = 65536):

    for i in range(sup):
        for t in algorithm:
            b = word.find(t[0])
            if b >= 0:
                word = word[0:b] + t[1] + word[b + len(t[0]):]
                if len(t) > 2 and t[2] == '.':
                    return word;
                break
        else:
            return word
        
    return None

