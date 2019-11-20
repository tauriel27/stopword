__version__='0.0.1'
__name__='stopword'

def _read_stopwords():
    stopwords = set()
    with open('stopwords-cn.txt') as f:
        for line in f:
            stopwords.add(line[:-1])
    return stopwords

def filter(input_list):
    return [i for i in input_list if i not in stopwords]

stopwords = _read_stopwords()
