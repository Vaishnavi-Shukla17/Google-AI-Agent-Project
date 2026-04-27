def research_prompt(query: str, context: str) -> str:
    return f"""
Create a professional research report on: "{query}"

Use the following research context:
{context}

Format EXACTLY:

## Abstract
2-3 sentences summary.

## Key Findings
- Bullet 1 with facts
- Bullet 2 with data
- Bullet 3 with insights

## Conclusion
1-2 sentences final thoughts.
"""
def pdf_chunk_summary_prompt(chunk: str, chunk_number: int) -> str:
    return f"""
You are analyzing chunk {chunk_number} of a PDF document.

Summarize this chunk in bullet points.
Focus on:
- main topic
- important findings
- technical details
- useful insights

TEXT:
{chunk}
"""

def pdf_final_summary_prompt(chunk_summaries: str) -> str:
    return f"""
You are given summaries of multiple chunks from one PDF.

Create a final structured analysis in this format:

## Title
## Main Points
## Findings
## Conclusion

Use only the information from the chunk summaries below.

CHUNK SUMMARIES:
{chunk_summaries}
"""
def summary_prompt(text: str) -> str:
    return f"Summarize in 3-5 bullets:\n\n{text[:4000]}"

def pdf_analysis_prompt(text: str) -> str:
    return f"""
Analyze this research paper and return:

## Title
## Key Points
## Findings
## Conclusion

Content:
{text[:4000]}
"""
