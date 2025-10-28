from src.ner import ner_spacy, ner_transformers
from fastapi import FastAPI
import uvicorn

app = FastAPI()
@app.get("/extract/")
def extract_entities(text: str, method: str = "spacy"):
    if method == "spacy":
        results = ner_spacy(text)
    else:
        results = ner_transformers(text)
    return {
        "method": method,
        "results": results
    }

def main():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main()
