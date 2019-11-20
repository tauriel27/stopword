import os

module_path = os.path.dirname(__file__)
def _read_stopwords():
    stopwords = set()
    with open(os.path.join(module_path, 'stopwords.txt')) as f:
        for line in f:
            stopwords.add(line[:-1])
    return stopwords

def filter(input_list):
    return [i for i in input_list if i not in stopwords]

stopwords = _read_stopwords()
