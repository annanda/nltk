import nltk, re

class SentenceExtractor:
    
    def __init__(self, article):
        self.article = article
    
    def sentence_spans(self):
        
        sentence_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        spans = sentence_tokenizer.span_tokenize(self.article)
        
        #variaveis criadas para aumentar a legibilidade
        start = 0
        end = 1
        
        # devemos remover da primeira sentenca o titulo do artigo
        first_sentence = self.article[spans[0][start]:spans[0][end]+1]
        titulo = re.findall(r'(\n*.*\n\n)', first_sentence)[0]
        new_first_span_beginning = len(titulo)
        spans[0] = (new_first_span_beginning, spans[0][end])
        
        return spans
        
    def sentence_spans_as_strings(self):
        return [str(span) for span in self.sentence_spans()]