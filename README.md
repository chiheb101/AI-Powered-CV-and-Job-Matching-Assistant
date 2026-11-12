# AI-Powered CV and Job-Matching Assistant

A Python/Jupyter Notebook project that uses **LangGraph**, **LangChain**, and **OpenAI** to help users review a CV and compare it with online job postings.

The assistant can extract text from a CV, retrieve structured information from job-posting URLs, and use the collected information to provide career-related feedback.

## Features

- **CV text extraction:** Reads CV documents in PDF and DOCX formats.
- **Legacy DOC support:** Attempts to convert `.doc` files to DOCX using LibreOffice (`soffice`).
- **Job-posting analysis:** Uses the OpenAI `gpt-4o-search-preview` model with web search to extract information from a supplied job-posting URL.
- **Structured job details:** Requests the job title, company, location, employment type, salary (if available), qualifications, responsibilities, benefits, application instructions, and posting date.
- **CV and job comparison:** The agent can use the extracted CV and job-posting information to assess suitability and identify relevant strengths or gaps.
- **CV improvement advice:** Provides suggestions for improving a CV for target roles.
- **Tool-using agent:** LangGraph connects the assistant to the CV extraction and job-posting tools.
- **Conversation state:** LangGraph's `MemorySaver` checkpointer maintains state for a conversation thread while the Python process is running.
- **Optional tracing:** LangSmith tracing can be enabled to inspect agent execution.

## Project files

```text
CV-Assistant/
├── 3.12 Connecting to LangSmith(1).ipynb
├── README.md
├── .gitignore
└── requirements.txt
```

Place any CV used for testing in your local working folder. Do not commit personal CV documents to a public repository.

## Technologies

- Python
- Jupyter Notebook
- LangGraph
- LangChain
- `langchain-openai`
- OpenAI API
- LangSmith (optional tracing)
- `pdfplumber`
- `python-docx`
- LibreOffice (only for legacy `.doc` conversion)

## Requirements

- Python 3.12 is the version used in the notebook's development environment.
- An OpenAI API key with access to the models used by the notebook:
  - `gpt-4.1` for the LangChain assistant.
  - `gpt-4o-search-preview` for job-posting search.
- Internet access for OpenAI API calls and job-posting retrieval.
- Jupyter Notebook or JupyterLab.
- LibreOffice installed and available as `soffice` on your PATH if you need to process legacy `.doc` files.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/<your-username>/<your-repository>.git
   cd <your-repository>
   ```

2. Create and activate a virtual environment.

   **Windows (PowerShell):**

   ```powershell
   py -3.12 -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **macOS / Linux:**

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set your OpenAI API key as an environment variable.

   **Windows (PowerShell):**

   ```powershell
   $env:OPENAI_API_KEY="your-openai-api-key"
   ```

   **macOS / Linux:**

   ```bash
   export OPENAI_API_KEY="your-openai-api-key"
   ```

5. Start Jupyter:

   ```bash
   jupyter notebook
   ```

6. Open `3.12 Connecting to LangSmith(1).ipynb` and run the cells in order.

## Configuration

The notebook creates an OpenAI client using the `OPENAI_API_KEY` environment variable.

LangSmith tracing is optional. To enable it, configure the following environment variables outside the notebook:

```text
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your-langsmith-api-key
LANGSMITH_PROJECT=Agents Course
LANGSMITH_ENDPOINT=https://api.smith.langchain.com
```

To run without LangSmith tracing:

```text
LANGSMITH_TRACING=false
```

**Important:** Do not hardcode API keys in the notebook. In the notebook's LangSmith configuration cell, read the key from the environment instead:

```python
os.environ["LANGSMITH_TRACING"] = os.getenv("LANGSMITH_TRACING", "false")
os.environ["LANGSMITH_API_KEY"] = os.getenv("LANGSMITH_API_KEY", "")
os.environ["LANGSMITH_PROJECT"] = os.getenv("LANGSMITH_PROJECT", "Agents Course")
os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
```

If tracing is disabled, the LangSmith API key is not needed.

## How to use

1. Put a CV file in the notebook's working directory, or provide the correct path to the CV file.
2. Run the notebook cells in order to initialize the OpenAI client, tools, LangGraph workflow, and memory checkpointer.
3. Send the assistant a request that includes the CV file path and, when relevant, the job-posting URL(s).
4. Review the assistant's response and verify important details before using them in a job application.

### Tools implemented in the notebook

| Tool | Purpose |
|---|---|
| `extract_cv_text(file_path)` | Extracts text from a PDF, DOCX, or DOC CV file. |
| `job_posting_tool(job_link)` | Uses OpenAI web search to retrieve and summarize information from a job-posting URL. |

The LangGraph workflow routes messages from the assistant to the tools when needed, then returns to the assistant to produce a response.

## Current limitations

- The notebook uses `MemorySaver`, which keeps conversation state in memory. State is not stored permanently and is lost when the Python process/kernel is restarted.
- PDF extraction uses text extraction through `pdfplumber`. Scanned/image-only PDFs may not produce usable text because OCR is not implemented.
- Legacy `.doc` conversion requires LibreOffice and the `soffice` command.
- Some job-posting websites may block automated access, require authentication, or make postings unavailable.
- API requests are subject to the OpenAI account's model access, billing, and rate limits.
- The notebook currently contains example job-posting URLs and a sample CV filename in its demonstration cells. Replace these with your own test inputs before running it.

## Security and privacy

- Never commit API keys, passwords, `.env` files, or other credentials.
- Do not publish real CVs or personal documents without the owner's explicit permission.
- Review and clear notebook outputs before pushing to GitHub. Outputs can contain CV text, personal information, job-search details, or API responses.
- Review `git status` before every commit. The `.gitignore` file helps exclude common sensitive files, but it cannot guarantee that every private file is excluded.
- If an API key has already been committed or shared, revoke it and create a new one. Removing it from the latest notebook version does not remove it from Git history.

## Possible future improvements

- Add a simple web interface for uploading a CV and entering job links.
- Add persistent conversation storage.
- Add OCR support for scanned CVs.
- Add automated tests and more robust error handling/retry logic.
- Add a configurable scoring method for comparing a CV with job requirements.

## License

No license has been selected yet. Unless a license is added, others should not assume they have permission to reuse, modify, or distribute this project.
