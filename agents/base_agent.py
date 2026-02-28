from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
import os
import json
import re
import json
import re


class BaseAgent:

    def __init__(self, system_prompt):

        self.llm = ChatCohere(
            model="command-a-03-2025",
            cohere_api_key=os.getenv("COHERE_API_KEY"),
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_template(system_prompt)
        self.chain = self.prompt | self.llm



    def run(self, context, data):
        response = self.llm.invoke(
            self.prompt.format(context=context, data=data)
        )

        raw = response.content if hasattr(response, "content") else str(response)

        print("🔎 Raw model output:", raw)

    
        match = re.search(r"\{.*\}", raw, re.DOTALL)

        if not match:
            raise ValueError("No JSON found in model output")

        cleaned = match.group(0)

        return json.loads(cleaned)