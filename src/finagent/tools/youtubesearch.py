from crewai_tools import BaseTool, PDFSearchTool,  YoutubeVideoSearchTool

class MyCustomTool(BaseTool):
    name: str = "YouTube Search "
    description: str = (
        "This tool allows for searching PDF content using a Retrieval-Augmented Generation approach."
    )

    def _run(self, argument: str) -> str:
        # Initialize the PDFSearchTool with the given configuration
        tool = YoutubeVideoSearchTool(
            config=dict(
                llm=dict(
            provider="groq", # or google, openai, anthropic, llama2, ...
            config=dict(
                model="llama3-8b-8192",
                # temperature=0.5,
                # top_p=1,
                # stream=true,
            ),
        ),
        embedder=dict(
            provider="google", # or openai, ollama, ...
            config=dict(
                model="models/embedding-001",
                task_type="retrieval_document",
                # title="Embeddings",
            ),
        ),
    )
)
        
        # Perform the search with the provided argument
        search_result = tool.search(argument)

        # Process the result and return the output
        return f"Search results: {search_result}"

# Example usage
#if __name__ == "__main__":
 #   my_tool = MyCustomTool()
  #  result = my_tool._run("Sample query to search in PDF")
   # print(result)
