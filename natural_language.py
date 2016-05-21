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
                # print(article_name)
                with open('articles/'+article_name, 'w') as text_article:
                    text_article.write(artigo.strip())
        return artigos

    def segment(self):
        artigos = self.read()
        segmentos = []
        for artigo in artigos:
            sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
            segmentado = sent_tokenizer.span_tokenize(artigo)
            # primeiro_segmento = artigo[segmentado[0][0]:segmentado[0][1]+1]
            titulo = re.findall(r'(\n*.*\n\n)', artigo[segmentado[0][0]:segmentado[0][1]+1])
            # print("titulo", titulo)
            len_titulo = len(titulo[0])
            seg_2 = segmentado[0][1]
            segmentado[0] = (len_titulo, seg_2)
            segmentos.append(segmentado)
        return segmentos

p = Process('resources/wiki_01')
p.read()
p.segment()[2]