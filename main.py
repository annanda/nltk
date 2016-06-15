from ArticleReader import ArticleReader
from SentenceExtractor import SentenceExtractor
from NEExtractor import NEExtractor

reader = ArticleReader(from_path='resources/wiki_01')

for (i, article) in enumerate(reader.articles):
    with_newline = '\n'
    
    sentence_extractor = SentenceExtractor(article)
    spans_text = with_newline.join(sentence_extractor.sentence_spans_as_strings())
    spans_text = with_newline.join(["Sentence Spans:", '', spans_text])
    reader.add_to_article(i, spans_text)
    
    ne_extractor = NEExtractor(article)
    ne_text = with_newline.join(["Nomined Entities:", ''] + ne_extractor.nominated_entities())
    reader.add_to_article(i, ne_text)
    
reader.save_articles(to="articles")