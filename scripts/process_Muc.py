import spacy

def extract_coreference_clusters(sentences):
    # Load spaCy model
    nlp = spacy.load("en_core_web_sm")

    # Process the sentences
    doc = nlp(" ".join([" ".join(sentence) for sentence in sentences]))

    # Extract coreference clusters
    coreference_clusters = []
    for cluster in doc._.coref_clusters:
        cluster_spans = []
        for mention in cluster.mentions:
            start = mention.start
            end = mention.end - 1  # Adjust end index to be inclusive
            cluster_spans.append([start, end])
        coreference_clusters.append(cluster_spans)

    return coreference_clusters

# Example usage
sentences = [
    ["Seattle", "is", "a", "rainy", "city", "."],
    ["Jenny", "Durkan", "is", "the", "city's", "mayor", "."],
    ["She", "was", "elected", "in", "2017", "."]
]

result = extract_coreference_clusters(sentences)
print(result)