from google import genai
import os
import argparse

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


def main():
    argparser = argparse.ArgumentParser(description="Summarize text using Gemini API")
    argparser.add_argument("text", type=str, help="Text to summarize")
    args = argparser.parse_args()
    summary = summarize_text(args.text)
    print(summary)
if __name__ == "__main__":
   main()
