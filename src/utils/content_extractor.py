import wikipedia
from collections import Counter

def get_content_frequency(topic:str, n_value:int):
    controlled_topic = topic+" (word)"
    page_data = wikipedia.page(controlled_topic)
    content= page_data.content
    words = content.split()
    word_counts = Counter(words)
    top_n_words = word_counts.most_common(n_value)
    return top_n_words

