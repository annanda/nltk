import re

class ArticleReader:
    
    def __init__(self, from_path):
        with open(from_path, 'r') as text_file:
            
            regex = re.compile(r'<doc.*?>(.*?)</doc>', flags=re.DOTALL)
            articles = re.findall(regex, text_file.read())
            
            self.articles = [article.strip() for article in articles]
        
    def save_articles(self, to):
        for (i, article) in enumerate(self.articles):
            article_name = re.findall(r'(.*?)\n', article)[0]
            
            with open(to+"/"+article_name, 'w') as article_file:
                article_file.write(article)
        
    def add_to_article(self, index, text):
        self.articles[index] += "\n\n" + text