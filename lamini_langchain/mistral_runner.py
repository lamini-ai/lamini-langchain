from typing import Any, List, Mapping, Optional

from langchain_core.callbacks.manager import CallbackManagerForLLMRun
from langchain_core.language_models.llms import LLM

import lamini


class MistralRunner(LLM):
    model_name: Optional[str]

    @property
    def _llm_type(self) -> str:
        return "lamini"

    def _call(
        self,
        prompt: str,
        stop: Optional[str] = None,
        **kwargs: Any,
    ) -> str:
        if self.model_name is not None:
            return lamini.MistralRunner(model_name=self.model_name).call(prompt, **kwargs)
        else:
            return lamini.MistralRunner().call(prompt, **kwargs)

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        """Get the identifying parameters."""
        return {"model_name": self.model_name}
