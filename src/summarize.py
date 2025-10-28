from google import genai
import os
import argparse

def summarize_text(text):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Summarize the following text:\n\n{text}"
    )
    return response.text


def main():
    argparser = argparse.ArgumentParser(description="Summarize text using Gemini API")
    argparser.add_argument("text", type=str, help="Text to summarize")
    args = argparser.parse_args()
    summary = summarize_text(args.text)
    print(summary)
if __name__ == "__main__":
   main()
