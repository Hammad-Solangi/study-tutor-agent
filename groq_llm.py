from crewai import LLM


class GroqLLM(LLM):
    def call(self, messages, **kwargs):
        if isinstance(messages, list):
            messages = [
                {
                    key: value
                    for key, value in message.items()
                    if key != "cache_breakpoint"
                }
                for message in messages
            ]

        return super().call(messages, **kwargs)
