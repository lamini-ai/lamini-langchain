from typing import Any, List, Mapping, Optional

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM

import lamini

class MistralRunner(LLM):
    @property
    def _llm_type(self) -> str:
        return "lamini"

    def _call(
        self,
        prompt: str,
        stop: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        return lamini.MistralRunner().call(prompt, **kwargs)

