
from lamini_langchain.mistral_runner import MistralRunner

def main():
    llm = MistralRunner()

    result = llm.invoke("tell me a joke about llamas")

    print(result)


main()

