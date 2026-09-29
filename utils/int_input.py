def int_input(content: str | None):
    prompt = "" if content is None else content
    return int(input(prompt))