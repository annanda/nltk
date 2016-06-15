import nltk

class NEExtractor:
    
    def __init__(self, article):
        self.article = article
        
    def nominated_entities(self):
        
        sentences = nltk.sent_tokenize(self.article)
        tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
        tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
        chunked_sentences = nltk.ne_chunk_sents(tagged_sentences, binary=True)
        
        entity_names = []
        for chunked_sentence in chunked_sentences:
            entity_names.extend(self._extract_entity_names(chunked_sentence))
        
        return list(set(entity_names))
        
    def _extract_entity_names(self, tree):
        entity_names = []
    
        if hasattr(tree, 'label') and tree.label:
            if tree.label() == 'NE':
                entity_names.append(self._get_name_from(tree))
            else:
                for child in tree:
                    entity_names.extend(self._extract_entity_names(child))
    
        return entity_names
        
    def _get_name_from(self, tree):
        return ' '.join([child[0] for child in tree])