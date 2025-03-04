"""Summarizes transcripts into meeting minutes"""

import ollama
import os
from docx import Document

# Define paths
transcript_file = os.path.expanduser("~/mckim_creed/projects/meeting_minutes/input/meeting_transcript.txt")
output_txt = os.path.expanduser("~/mckim_creed/projects/meeting_minutes/output/output.txt")
output_docx = os.path.expanduser("~/mckim_creed/projects/meeting_minutes/output/output.docx")

# Ensure output directory exists
os.makedirs(os.path.dirname(output_txt), exist_ok=True)

# Read the transcript
def read_transcript_txt(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

# Load transcript
transcript = read_transcript_txt(transcript_file)

# Summarize using Ollama
def summarize_transcript(transcript):
    print("📝 Sending transcript to Ollama for structured meeting minutes...")

    response = ollama.chat(
        model="phi3",
        messages=[{
            "role": "user",
            "content": f"""Convert this meeting transcript into professional meeting minutes.
            
            ### Formatting Instructions:
            - Use clear section headings like **Meeting Date, Attendees, Agenda, Discussion Points, Decisions Made, Action Items, Next Steps**.
            - Format each section in **bullet points** where applicable.
            - Ensure clarity and conciseness; avoid run-on sentences.
            - Include action items with assignees and deadlines if mentioned.

            ### Meeting Transcript:
            {transcript}
            """
        }]
    )

    print(f"📨 Ollama raw response type: {type(response)}")  # Debug
    print(f"📨 Ollama response attributes: {dir(response)}")  # Debug

    # Ensure we extract the message content correctly
    if hasattr(response, "message") and hasattr(response.message, "content"):
        message_text = response.message.content
    else:
        raise TypeError(f"Unexpected Ollama response format: {type(response)} - {response}")

    print(f"📨 Ollama response content (first 300 chars): {message_text[:300]}...")  # Preview output

    return message_text  # Ensure we return a string




meeting_minutes = summarize_transcript(transcript)

# Save output
def save_to_txt(output_text, file_path):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(str(output_text))  # Ensure it's a string
    print(f"✅ Saved meeting minutes to: {file_path}")

def save_to_docx(output_text, file_path):
    doc = Document()
    doc.add_paragraph(str(output_text))  # Ensure it's a string
    doc.save(file_path)
    print(f"✅ Saved meeting minutes to: {file_path}")


save_to_txt(meeting_minutes, output_txt)
save_to_docx(meeting_minutes, output_docx)

print("Meeting minutes saved successfully!")
