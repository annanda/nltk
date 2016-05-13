import nltk, re


class Process:

    path = None

    def __init__(self, path):
        self.path = path

    def read(self):
        with open(self.path, 'r') as text_file:
            regex = re.compile(r'<doc.*?>(.*?)</doc>', flags=re.DOTALL)
            artigos = re.findall(regex, text_file.read())
            for i, artigo in enumerate(artigos):
                article_name = re.findall(r'(.*?)\n', artigo.strip())
                article_name = article_name[0]
                print(article_name)
                with open(article_name, 'w') as text_article:
                    text_article.write(artigo.strip())
        return artigos

    def segment(self):
        text = self.read()[0]
        sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        segmentado = sent_tokenizer.span_tokenize(text)

        # for seg in segmentado:
        #     print(seg)
        #     print(text[seg[0]:seg[1]+1])
        # print('segmentado', len(segmentado))

p = Process('wiki_01')
p.read()
p.segment()