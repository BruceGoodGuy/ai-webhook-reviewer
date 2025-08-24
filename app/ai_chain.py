from .config import settings
from langchain.chat_models import init_chat_model
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


def review_changes(diff: str):
    model = init_chat_model(
        "gpt-5-nano",
        model_provider="openai",
        api_key=settings.OPEN_AI_API_KEY,
    )

    prompt_string = """
    You are a senior software engineer reviewing a GitHub Pull Request. 
    You will be given file changes in unified diff format (`patch`).

    Your tasks:
    1. Review **all code changes** (added, deleted, or modified).
    2. Identify issues such as:
    - Bugs or syntax errors
    - Security issues
    - Performance problems
    - Style/PSR-4 violations
    - Maintainability concerns
    3. Suggest a short, clear fix or improvement.

    ⚠️ STRICT OUTPUT RULES:
    - Return a JSON array only.
    - Each element must be in this shape:
    {{
        "filename": "<string>",
        "line": <integer>,
        "content": "<string>",
        "category": "<string>"
    }}
    - `category` must be one of: ["bug", "security", "performance", "style", "maintainability", "documentation"].
    - `line` should be the line number in the **new file version** where the comment applies.
    - If no issues, return `[]`.

    Here are the file changes to review:

    {file_changes}
    """
    
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", prompt_string)]
    )
    
    prompt = prompt_template.invoke(
        {"file_changes": diff}
    )

    response = model.invoke(prompt)

    return response.content


async def test_ai_chain():
    model = init_chat_model(
        "gpt-5-nano",
        model_provider="openai",
        api_key=settings.OPEN_AI_API_KEY,
    )

    system_template = "Translate the following from English into {language}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )

    prompt = prompt_template.invoke(
        {"language": "French", "text": "Hello, how are you?"}
    )

    response = model.invoke(prompt)
