# AI-Powered CV and Job-Matching Assistant

A Python-based AI assistant that helps users analyze their CVs, understand job requirements, and compare their profiles with online job opportunities.

The project uses **LangGraph**, **LangChain**, and **OpenAI** to create an interactive assistant capable of extracting information from CV documents, analyzing job postings, and providing personalized career-related feedback.

## Features

- **CV Text Extraction:** Extracts text from CV documents in PDF and DOCX formats.
- **Legacy DOC Support:** Converts older `.doc` files into DOCX using LibreOffice.
- **Job Posting Analysis:** Uses OpenAI GPT-4.1 with web search to retrieve and analyze information from job-posting URLs.
- **Structured Job Information:** Extracts job title, company, location, employment type, salary, qualifications, responsibilities, benefits, application instructions, and posting date.
- **CV and Job Matching:** Compares CV information with job requirements to identify relevant skills, strengths, and gaps.
- **CV Improvement Suggestions:** Provides recommendations to improve and tailor a CV for specific job opportunities.
- **Tool-Using AI Agent:** Uses LangGraph to connect the assistant to the CV extraction and job-posting tools.
- **Conversation Memory:** Uses LangGraph's `MemorySaver` checkpointer to maintain conversation state while the application is running.

## Project Structure

```text
CV-Job-Matching-Assistant/
│
├── agent/
│   ├── __init__.py
│   └── graph.py
│
├── tools/
│   ├── __init__.py
│   ├── cv_tools.py
│   └── job_tools.py
│
├── services/
│   ├── __init__.py
│   └── openai_service.py
│
├── config/
│   └── __init__.py
│
├── notebooks/
│   └── cv_job_matching_assistant.ipynb
│
├── test_files/
│   └── my_cv.pdf
│
├── .env
├── .env.example
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

**Main folders:**

- `agent/`: Contains the LangGraph workflow and assistant logic.
- `tools/`: Contains the CV extraction and job-posting analysis tools.
- `services/`: Handles OpenAI client and language model initialization.
- `config/`: Reserved for project configuration.
- `notebooks/`: Contains the original Jupyter Notebook used as a reference.
- `test_files/`: Contains local files used for testing.

## Technologies

- Python
- LangGraph
- LangChain
- LangChain OpenAI
- OpenAI API
- OpenAI GPT-4.1
- OpenAI Web Search
- Python-dotenv
- LangSmith (optional)
- pdfplumber
- python-docx
- LibreOffice (for legacy DOC conversion)

## Requirements

- Python installed on your computer.
- An OpenAI API key with access to GPT-4.1 and the required API capabilities.
- Internet connection for OpenAI API requests and job-posting retrieval.
- LibreOffice installed and available through the `soffice` command if you need to process legacy `.doc` files.

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/chiheb101/AI-Powered-CV-and-Job-Matching-Assistant.git

cd AI-Powered-CV-and-Job-Matching-Assistant
```

### 2. Create a virtual environment

**Windows (PowerShell):**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key
```

An optional LangSmith configuration can also be added:

```env
LANGSMITH_TRACING=false
LANGSMITH_API_KEY=
LANGSMITH_PROJECT=CV-Job-Matching-Assistant
```

Keep your actual `.env` file private. Never upload API keys to a public repository.

## How to Run the Assistant

Make sure your virtual environment is activated and your `.env` file is configured.

Start the application from the project root:

```bash
python main.py
```

The assistant will start in the terminal and wait for user messages.

To stop the application, type:

```text
exit
```

or:

```text
done
```

## How to Use

### 1. General Questions

You can ask the assistant general questions about CVs, careers, and job applications.

Example:

```text
Hello, what can you help me with?
```

### 2. CV Analysis

Provide the path to your CV and ask the assistant to analyze it.

Example:

```text
Please analyze my CV.

The file is located at:
test_files/my_cv.pdf
```

The assistant can extract and summarize your education, work experience, technical skills, and languages.

### 3. Job Posting Analysis

Provide a job-posting URL and ask the assistant to extract its main information.

Example:

```text
Analyze this job posting:
https://example.com/job-posting
```

The assistant retrieves and organizes the available job details.

### 4. CV and Job Matching

You can ask the assistant to compare your CV with a specific job opportunity.

Example:

```text
Compare my CV with this job posting.

CV file path: test_files/my_cv.pdf

Job posting URL: https://example.com/job-posting

Identify my matching skills, missing requirements,
relevant experience, and recommendations for improvement.
```

The assistant uses the available tools to collect information before generating its comparison.

## Implemented Tools

| Tool | Purpose |
|---|---|
| `extract_cv_text(file_path)` | Extracts text from PDF, DOCX, or DOC CV files. |
| `job_posting_tool(job_link)` | Analyzes a job-posting URL using OpenAI web search. |

The LangGraph workflow manages the interaction between the language model and these tools. When a tool is needed, the assistant calls it, receives its result, and continues generating the response.

## Conversation Memory

The application uses LangGraph's `MemorySaver` checkpointer to maintain conversation state.

The same conversation thread can retain previous messages while the application is running. However, conversation state is stored in memory and is lost when the Python process is restarted.

## Current Limitations

- PDF extraction uses `pdfplumber`. Scanned or image-only PDFs may not produce usable text because OCR is not implemented.
- Legacy `.doc` conversion requires LibreOffice.
- Some job-posting websites may block automated access, require authentication, or make job details unavailable.
- Conversation memory is temporary and is not saved permanently.
- AI-generated responses may contain inaccuracies. Important CV and job details should be verified before using them in applications.
- OpenAI API requests are subject to account billing, model availability, and rate limits.

## Security and Privacy

- Never upload API keys, passwords, or `.env` files to GitHub.
- Do not publish personal CV documents without the owner's permission.
- Keep personal test documents inside the local `test_files/` folder.
- Review notebook outputs before sharing the original notebook, as they may contain personal information or API responses.
- Check `git status` before committing files to make sure sensitive information is not included.

## Possible Future Improvements

- Develop a web interface for CV uploads and job-posting URLs.
- Add permanent conversation storage.
- Implement OCR for scanned CV documents.
- Improve error handling and validation.
- Add automated tests.
- Introduce a configurable CV and job compatibility scoring system.
- Improve the accuracy and consistency of CV and job-matching responses.

## License

No license has been selected yet. Unless a license is added, others should not assume they have permission to reuse, modify, or distribute this project.