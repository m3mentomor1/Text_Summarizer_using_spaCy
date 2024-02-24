import spacy
from collections import Counter

# Load English tokenizer, tagger, parser, and NER
nlp = spacy.load("en_core_web_sm")

def extractive_summarization(text, num_sentences=3):
    # Process the text with SpaCy
    doc = nlp(text)

    # Tokenize the text and remove stopwords
    words = [token.text.lower() for token in doc if not token.is_stop and token.is_alpha]

    # Calculate word frequencies
    word_freq = Counter(words)

    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sent in doc.sents:
        score = sum(word_freq[token.text.lower()] for token in sent if token.text.lower() in word_freq)
        sentence_scores[sent] = score

    # Select top sentences based on scores
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:num_sentences]
    summary = ' '.join(str(sent) for sent in top_sentences)
    return summary

# Accept text input from the console
def main():
    text = input("Enter the text you want to summarize:\n")
    summary = extractive_summarization(text)
    print("\nExtractive Summary:")
    print(summary)

if __name__ == "__main__":
    main()
