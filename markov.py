import random

class Markov:
    
    def __init__(self,depth):
        self.depth = depth
        self.dic = {}

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

    def update(self,sentence):
        if isinstance(sentence,str):
            sentence = sentence.rstrip('\n').split(' ')
        for i in range(len(sentence)-self.depth):
            sequence = tuple(sentence[i:i+self.depth])
            if sequence not in self.dic:
                self.dic[sequence] = []
            self.dic[sequence].append(sentence[i+self.depth])


if __name__ == '__main__':
    ex_sentence = ['それ','が','彼','の','最後','の','言葉','でし','た','。','彼','が','本当に','無神論者','だっ','た','のか','どうか','が','気がかり','です','。',]
    m = Markov(1)
    m.update(ex_sentence)
    m.update(ex_sentence)
    print(m.make_salad())
