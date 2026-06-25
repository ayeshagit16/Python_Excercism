def response(hey_bob: str) -> str:
    message = hey_bob.strip()

    if not message:
        return "Fine. Be that way!"

    is_question = message.endswith("?")
    has_letters = any(c.isalpha() for c in message)
    is_yelling = has_letters and message.upper() == message

    if is_question and is_yelling:
        return "Calm down, I know what I'm doing!"
    if is_yelling:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    return "Whatever."


        