
from lamini_langchain.mistral_runner import MistralRunner

def main():
    llm = MistralRunner(model_name="halhigdon-1")

    result = llm.invoke("tell me a joke about llamas")

    print(result)


main()

