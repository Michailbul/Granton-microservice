from langchain_openai import ChatOpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import os
from src import config
from typing import List, Optional
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

app = FastAPI()


if not config.OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set. Please set it before running the application.")



class Query(BaseModel):
    text: str

class StructuredData(BaseModel):
    name: str = Field(description="The name of the Pokémon", default="Unknown")
    description: str = Field(description="The overall description of the Pokémon", default= " Unknown")
    abilities: List[str] = Field(description="Special abilities of the Pokémon", default_factory= lambda : ["No abilities specified"] )
    colors: List[str] = Field(description= "Colors of the pokemon", default_factory= lambda : [" No color specified"] )
    size : Optional[str] = Field(description= "A size o the pokemon", default = "Unknown size")


llm = ChatOpenAI(api_key=config.OPENAI_API_KEY, model_name="gpt-3.5-turbo-0125")

@app.post("/process", response_model=StructuredData)
def process_data(query: Query):
    try:
        # Define the output parser
        parser = JsonOutputParser(pydantic_object=StructuredData)

        # Define the prompt template
        prompt = PromptTemplate(
            template=
            """
            You are a helpful assistant that generates description of a Pokemon, describing it and it's abilities.\
            The description should include its colors, abilities, size and name. \
            If the provided name is not matching to any pokemon of your knowledge, make up the description of it on your own \
            \n{format_instructions}\n{query}\n
            """,
            input_variables=["query"],
            partial_variables={"format_instructions": parser.get_format_instructions()},
        )

        chain = prompt | llm | parser

        result = chain.invoke({"query": query.text}) 
        return result
        #return StructuredData(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)
