from google import genai

GOOGLE_BOOKS_API = "https://www.googleapis.com/books/v1/volumes?q={}&maxResults=1"
YOUTUBE_API_KEY = "AIzaSyBDzRTvcPpqDFYehd8jo90VJLld4JDysW8"
TAVILY_API_KEY = "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"
UPLOAD_DIR = "uploads"
FACULTY_DATASET_PATH = "faculty_dataset.json"
client = genai.Client(api_key="AIzaSyCijt8NxzuMa4ROq-Z_basaWHtECy05bqs")

# Set up Gemini
# from google import genai as genai2
import google.generativeai as genai2
API_KEY2 = "AIzaSyCijt8NxzuMa4ROq-Z_basaWHtECy05bqs"
genai2.configure(api_key=API_KEY2)
model = genai2.GenerativeModel("gemma-3-27b-it")