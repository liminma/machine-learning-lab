B_INST, E_INST = "[INST]", "[/INST]"
B_SYS, E_SYS = "<<SYS>>\n", "\n<</SYS>>\n\n"
BOS, EOS = "<s>", "</s>"

DEFAULT_SYSTEM_PROMPT = """\
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe. Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.

If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information."""


def construct_llama2_prompt(dialog: list[dict]) -> str:
    """
    Construct prompt for single turn or multi-turn conversation.

    Refer to https://github.com/facebookresearch/llama/blob/main/llama/generation.py#L213 for
    the default prompt template of Llama 2.

    A single turn prompt:
    ---------------------------
        <s>[INST] <<SYS>>
        {system_prompt}
        <</SYS>>

        {user_message} [/INST]

    A multi-turn prompt:
    ---------------------------
        <s>[INST] <<SYS>>
        {system_prompt}
        <</SYS>>

        {user_message_1} [/INST] {model_response_1} </s>\
        <s>[INST] {user_message_2} [/INST] {model_response_2} </s>\
        <s>[INST] {user_message_3} [/INST]

    Parameters:
        dialog: a list of dictionary with keys of 'role' and 'content'.
                Valid roles are: system, user, assistant.
    Return:
        constructed prompt.
    """
    if dialog[0]['role'] != 'system':
        # insert the system prompt as the first message
        dialog = [{'role': 'system', 'content': DEFAULT_SYSTEM_PROMPT}] + dialog

    # merge the first 2 messages
    dialog = [{'role': dialog[1]['role'],
               'content': B_SYS + dialog[0]['content'] + E_SYS + dialog[1]['content']}
             ] + dialog[2:]

    # construct prompt using chat history
    prompt_buffer = [
        f'{BOS}{B_INST} {(prompt["content"]).strip()} {E_INST} {(answer["content"]).strip()} {EOS}'
         for prompt, answer in zip(dialog[::2], dialog[1::2])
        ]

    if len(dialog) % 2 != 0:
        # add the last message (the current user input)
        prompt_buffer += [f'{BOS}{B_INST} {(dialog[-1]["content"]).strip()} {E_INST}']

    return ''.join(prompt_buffer)
