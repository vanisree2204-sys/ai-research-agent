def parse_response(text):

    sections = [
        "Summary:",
        "Key Points:",
        "Open Questions:",
        "Recommended Next Steps:"
    ]

    return all(
        section in text
        for section in sections
    )


def test_response_parser():

    sample_response = """
Summary:
AI is evolving rapidly.

Key Points:
- Healthcare
- Education

Open Questions:
- Ethical risks

Recommended Next Steps:
- Further research
"""

    assert parse_response(sample_response)