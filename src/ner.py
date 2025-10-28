import spacy
from transformers import pipeline
import argparse
from summarize import summarize_text

def ner_spacy(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    response = summarize_text(text)
    return {"entities": entities, "tags": response["tags"], "summary": response["summary"]}

def ner_transformers(text):
    ner = pipeline("ner", grouped_entities=True)
    entities = [(entity['word'], entity['entity_group']) for entity in ner(text)]
    response = summarize_text(text)
    return {"entities": entities, "tags": response["tags"], "summary": response["summary"]}

def main():
    argparser = argparse.ArgumentParser(description="Named Entity Recognition using SpaCy or Transformers")
    argparser.add_argument("text", type=str, help="Text for NER")
    argparser.add_argument("--method", type=str, choices=["spacy", "transformers"], default="spacy", help="NER method to use")
    args = argparser.parse_args()

    if args.method == "spacy":
        results = ner_spacy(args.text)
    else:
        results = ner_transformers(args.text)

    for entity, label in results:
        print(f"{entity}: {label}")

if __name__ == "__main__":
    main()
