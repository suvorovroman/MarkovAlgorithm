import argparse
import maf

class Algorithm:

    def __init__(self, source, inf=65536):

        if isinstance(source, list):
            self.algoritm = source
        else:
            self.algorithm = maf.parse_algorithm(open(source, 'r') if isinstance(source, str) else source)
        self.inf = inf

    def __call__(self, word):

        return maf.MA(self.algorithm, word, self.inf)
        

def parameters():
    
    parser = argparse.ArgumentParser(description = "Normal Markov Algorithm Interpreter (MA)")
    parser.add_argument("source",
                        type = argparse.FileType('r'),
                        help = "File name with MA substitution rules"
                        )
    parser.add_argument("--inf",
                        type = int,
                        default = 256,
                        help = "Infinity threshold (defaulted to %(default)s number of applications) to stop inapplicable algorithms"
                        )
    return vars(parser.parse_args())


try:

    algorithm = Algorithm(**parameters())

    while True:
        try:
            print("OUT>{}".format(algorithm(input("IN>"))))
        except maf.InapplicableAlgorithm as x:
            print(x)
            
except KeyboardInterrupt:
    print('')




