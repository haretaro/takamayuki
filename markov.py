import random

class Markov:
    
    def __init__(self,sentence,depth):
        self.depth = depth
        dic = {}
        for i in range(len(sentence)-depth):
            sequence = tuple(sentence[i:i+depth])
            if sequence not in dic:
                dic[sequence] = []
            dic[sequence].append(sentence[i+depth])
        self.dic = dic

    def make_salad(self,limit=100):
        key = random.choice(list(self.dic.keys()))
        sentence = [word for word in key]
        count = 0
        while key in self.dic and count < limit:
            sentence.append(random.choice(self.dic[key]))
            key = tuple(sentence[-self.depth:])
            count += 1
        result = ''
        for word in sentence:
            result += word
        return result

if __name__ == '__main__':
    ex_sentence = ['それ','が','彼','の','最後','の','言葉','でし','た','。','彼','が','本当に','無神論者','だっ','た','のか','どうか','が','気がかり','です','。',]
    m = Markov(ex_sentence,1)
    print(m.create())
