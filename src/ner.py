import spacy
from transformers import pipeline
import argparse
from google import genai
import os


def summarize_text(text):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Provide a tag list (3-5 max)  and a summary from following text:\n\n{text} in this fromat:\nTags: [tag1, tag2, tag3] \nSummary: summary text",
    )

    try:
        tags= response.text.split("Tags:")[1].split("Summary:")[0].strip()
        summary = response.text.split("Summary:")[1].strip()
        return {"tags": tags, "summary": summary}
    except Exception as e:
        print(f"Error occurred: {e}")
        return {"tags": response.text, "summary": response.text}


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
