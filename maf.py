import re

class InapplicableAlgorithm(Exception):
    pass

def MA(algorithm, word, inf = 65536):

    for i in range(inf):
        for t in algorithm:
            b = word.find(t[0])
            if b >= 0:
                word = word[0:b] + t[1] + word[b + len(t[0]):]
                if len(t) > 2 and t[2] == '.':
                    return word;
                break
        else:
            return word
        
    raise InapplicableAlgorithm(f"Number of rule applications exceeded infinity threshold ({inf})")

def string_algorithm(algorithm):

    s = ""

    for rule in algorithm:
        s += "{0}->{2}{1}".format(rule[0],
                                  rule[1],
                                  rule[2] if len(rule) > 2 else '') + '\n'

    return s

class InvalidRuleSyntax(Exception):
    pass

def parse_algorithm(f):

    algorithm = []
    count = 0
    for l in f:
        count += 1
        r = re.fullmatch("(\S*)->(\.?)(\S*)\n|\s*\n", l)
        if r == None:
            raise InvalidRuleSyntax(f"Line {count}, Rule {l}")
        if r.lastindex == None:
            continue
        algorithm.append(r.group(1, 3, 2))

    return algorithm
    
