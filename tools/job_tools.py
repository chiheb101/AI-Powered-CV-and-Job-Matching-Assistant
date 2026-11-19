
from langchain_core.tools import tool
from services.openai_service import client


@tool
def job_posting_tool(job_link: str) -> str:
    """
    Analyze a job posting URL and extract its main information.
    """

    try:
        response = client.responses.create(
            model="gpt-4.1",
            tools=[
                {
                    "type": "web_search",
                    "search_context_size": "medium"
                }
            ],
            
input=f"""
Analyze this job posting: {job_link}

Extract the following information in a concise format:

1. Job title
2. Company
3. Location
4. Employment type
5. Salary
6. Required qualifications and skills
7. Main responsibilities
8. Benefits
9. Application process
10. Posting date


Instructions:
- Use short bullet points.
- Include only important information.
- Avoid repeating the same information.
- Keep qualifications and responsibilities clear and specific.
- Do not invent missing information. Write "Not specified" when necessary.
- Keep the complete analysis concise (maximum 400 words and don't mention that in the answer given).
- Do not include URLs or citations after individual bullet points.
- Include the original job posting URL only once at the end, under "Source".
- If the job posting contains conflicting information, report the
  different values clearly instead of combining or choosing one.
- Include only information explicitly supported by the job posting.
"""

        )

        return response.output_text or (
            "Job posting unavailable or contains no job details."
        )

    except Exception as e:
        return f"Unable to retrieve job posting: {e}"
