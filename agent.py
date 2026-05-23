import json
import time
import requests
from openai import OpenAI
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# OPENROUTER API CONFIG
# =========================
API_KEY = "YOUR_OPENROUTER_API_KEY"
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY,
)

# =========================
# MEMORY FUNCTIONS
# =========================

MEMORY_FILE = "sessions.json"


def load_memory():
    try:
        with open(MEMORY_FILE, "r") as file:
            return json.load(file)
    except:
        return {}


def save_memory(memory):
    with open(MEMORY_FILE, "w") as file:
        json.dump(memory, file, indent=4)


# =========================
# CUSTOM TOOL
# =========================

def get_wikipedia_summary(topic):

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"

    try:

        response = requests.get(url)

        if response.status_code == 200:

            data = response.json()

            return data.get(
                "extract",
                "No summary found."
            )

        return "Wikipedia information not found."

    except Exception as e:

        return f"Error fetching Wikipedia summary: {e}"


# =========================
# STREAMING EFFECT
# =========================

def stream_text(text):

    for char in text:

        print(char, end="", flush=True)

        time.sleep(0.01)

    print()


# =========================
# RESPONSE GENERATION
# =========================

def generate_response(question, history):

    messages = [
        {
            "role": "system",
            "content": """
You are a research assistant.

Provide responses in this format:

Summary:
Key Points:
Open Questions:
Recommended Next Steps:
"""
        }
    ]

    for item in history:

        messages.append(item)

    messages.append({
        "role": "user",
        "content": question
    })

    retries = 3

    for attempt in range(retries):

        try:

            completion = client.chat.completions.create(
                model="openai/gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
            )

            return completion.choices[0].message.content

        except Exception as e:

            print(
                Fore.RED +
                f"\nAPI Error: {e}"
            )

            if attempt < retries - 1:

                print(
                    Fore.YELLOW +
                    "Retrying..."
                )

                time.sleep(2)

            else:

                return "Failed to get response after retries."


# =========================
# MAIN PROGRAM
# =========================

def main():

    memory = load_memory()

    print(
        Fore.CYAN +
        "\n=== Research Agent ==="
    )

    topic = input(
        "\nEnter research topic: "
    )

    if topic in memory:

        load_old = input(
            "Previous session found. Load context? (yes/no): "
        )

        if load_old.lower() == "yes":

            print(
                Fore.GREEN +
                "\nPrevious Summary:\n"
            )

            print(memory[topic])

    wiki = get_wikipedia_summary(topic)

    print(
        Fore.YELLOW +
        "\nWikipedia Summary:\n"
    )

    stream_text(wiki)

    history = []

    while True:

        question = input(
            Fore.CYAN +
            "\nAsk question (or type exit): "
        )

        if question.lower() == "exit":

            break

        response = generate_response(
            question,
            history
        )

        print(
            Fore.GREEN +
            "\nResearch Response:\n"
        )

        stream_text(response)

        history.append({
            "role": "user",
            "content": question
        })

        history.append({
            "role": "assistant",
            "content": response
        })

        memory[topic] = response

        save_memory(memory)

    print(
        Fore.MAGENTA +
        "\nSession Saved."
    )


if __name__ == "__main__":
    main()