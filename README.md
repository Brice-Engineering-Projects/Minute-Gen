# 📝 MinuteGen – AI-Powered Meeting Minutes Generator

**MinuteGen** is a Python-based AI tool that converts meeting recordings into structured meeting minutes. It uses **Whisper** for speech-to-text transcription and **Ollama** for summarization, ensuring clear, concise, and well-formatted minutes.

---

## 🚀 Features
✅ **Automated Transcription** – Converts `.mp3` audio files to text  
✅ **AI-Powered Summarization** – Generates structured meeting minutes  
✅ **Professional Formatting** – Sections like **Agenda, Discussion, Decisions, Action Items**  
✅ **Multi-Format Output** – Saves minutes as `.txt` and `.docx`  
✅ **Simple & Fast** – Works with a single command  

---

## 📂 Project Structure

MinuteGen/ │── meeting_minutes/ │ ├── voice_input/ # Stores audio files (.mp3) │ ├── input/ # Stores transcribed text files │ ├── output/ # Stores meeting minutes (.txt, .docx) │── transcribe_meeting.py # Converts audio to text │── transcript_to_minutes.py # Summarizes transcript into minutes │── README.md # Project documentation │── requirements.txt # Dependencies list


---

## 🛠️ Installation & Setup
### **Install Ollama (Global Install)**
Before proceeding, **you must install Ollama globally** because:
- Ollama serves as the **AI inference backend**.
- The Python package **only acts as a connector** to the globally installed Ollama.
- Without a global install, **the Python package will not work**.

#### **Install Ollama (Windows, Mac, or Linux)**
🔗 **[Ollama Installation Guide](https://ollama.com/)**  

For **Linux / WSL**, run:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
For **Mac (Homebrew):
```
brew install ollama
```
For Windows, download from [Ollama Installation Guide](https://ollama.com/) and install it.

**Verify Ollama Installation**
Run:
```
ollama --version
```
If you see a version number, Ollama is correctly installed.

### **Clone the Repository**
```bash
git clone https://github.com/Brice-Engineering-Projects/Minute-Gen.git
cd Minute-Gen
```

## Set Up a Virtual Environment
```
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```
## Install Dependencies
```
pip install -r requirements.txt
```
## 🎙️ Usage
1️⃣ Place Your Audio File in the voice_input/ Folder

**Voice Input: Audio file saved in:**
- Update the defined paths to fit your file structure.

2️⃣ Convert Audio to Text
python3 transcribe_meeting.py

**Input: Input file saved in:**
- Update the defined paths to fit your file structure.

3️⃣ Generate Meeting Minutes
python3 transcript_to_minutes.py

**Output: Minutes saved in:**
- Update the defined paths to fit your file structure.

## Example Output

### Meeting Minutes

**Meeting Date:** March 5, 2024  
**Attendees:** John Doe, Jane Smith, Alex Johnson  

---

### **Agenda:**
- Project timeline updates
- Budget discussion
- Task assignments

---

### **Discussion Points:**
- The new project deadline was proposed as **April 15, 2024**.
- Budget constraints require **reducing marketing spend by 10%**.
- The dev team is facing **delays due to API integration issues**.

---

### **Decisions Made:**
✅ **Deadline extended** to April 15.  
✅ **Budget reallocation approved** by finance.  

---

### **Action Items:**
📌 **Alex** → Fix API issue by March 10  
📌 **Jane** → Adjust marketing budget by next week  
📌 **John** → Send timeline update to stakeholders  

---

### **Next Steps:**
- Follow up on task completion by next meeting.
- Confirm new budget allocations with finance.

## 💡 Customization
Want to adjust the formatting? Modify the prompt inside transcript_to_minutes.py:
```
"content": f"""Convert this meeting transcript into professional meeting minutes.
- Use section headings: **Meeting Date, Attendees, Agenda, Discussion, Decisions, Action Items**.
- Format action items as bullet points with assignees and deadlines.
"""
```
## 🛠️ Troubleshooting

### Ollama Errors (Summarization Issues)
If Ollama does not return structured output, try:
```
- ollama pull phi3  # Ensure model is installed
```
### Whisper Issues (Transcription Errors)
If Whisper fails, ensure ffmpeg is installed:
```
- sudo apt install ffmpeg -y  # On Linux
- brew install ffmpeg         # On Mac
```
### 🚀 Future Enhancements

✅ Support for More Audio Formats (.wav, .m4a, .mp4)
✅ Multi-Speaker Identification
✅ Web Interface for Uploading & Downloading Files

## 📜 License

This project is licensed under the MIT License.

## 🤝 Contributing

Pull requests are welcome! Open an issue for feature suggestions.

📧 Contact: [brice.web.development](brice.web.development@gmail.com) 

### 🚀 Turn your meetings into structured insights with MinuteGen! 📝✨
