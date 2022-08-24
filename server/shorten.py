from nltk.tokenize import sent_tokenize

def shortenText(text):
    sentences = sent_tokenize(text)
    return "\n".join(sentences[0:20])
