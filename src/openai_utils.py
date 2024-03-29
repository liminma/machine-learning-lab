import openai


def chat_completion(messages: list[dict],
                    model: str = "gpt-3.5-turbo",
                    temperature: float = 0.,
                    max_tokens: int = 512) -> (str, dict):
    """Call ChatGPT API and return both generated content and token usages."""

    outputs = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )

    content = outputs.choices[0].message["content"]
    usage = outputs.usage.to_dict()

    return content, usage


def run_and_print(prompt: str) -> None:
    """A helper function for a simple call to API and print the response.
    """

    messages = [
        {'role': 'user', 'content': prompt}
    ]
    response, _ = chat_completion(messages)

    print(response)