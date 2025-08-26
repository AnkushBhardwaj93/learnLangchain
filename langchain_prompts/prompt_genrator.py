from langchain_core.prompts import PromptTemplate


template = PromptTemplate(
      template="Please summarize research papers about {product} in a concise manner."
      , input_variables=["product"],
      validate_template=True,

)

template.format(product="AI")
template.save("summarize_prompt.json")