def int_input(content: str | None = None) -> int | None:
    prompt = "" if content is None else content

    value = input(prompt)
    if not value:
        return None

    return int(value)