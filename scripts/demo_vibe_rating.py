"""Demo module. Exists only to give vibecheck something to ask about."""

EMOJI_BONUS = {"🔥": 3, "✨": 2, "🙂": 1}


def vibe_score(message):
    # Scores a commit message from 0 to 10. Every bonus emoji adds its
    # points, shouting (all caps) costs 2, and the word "fix" without a
    # ticket number like "#12" costs 1. The result never leaves 0..10.
    score = 5
    for char in message:
        score += EMOJI_BONUS.get(char, 0)
    if message.isupper():
        score -= 2
    if "fix" in message.lower() and "#" not in message:
        score -= 1
    return max(0, min(10, score))


def vibe_label(score):
    # Turns a score into a verdict. Checked from the top, so 8 and above
    # is "immaculate" even though it is also above 4.
    if score >= 8:
        return "immaculate"
    if score >= 4:
        return "passable"
    return "cursed"
