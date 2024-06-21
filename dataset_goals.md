RAG/Long Context Reasoning Dataset


Objectives:

Develop a model that can effectively utilize external (long) context for various tasks, including recall, reasoning, summarization, extraction, function calling, and agentic frameworks.
Improve the model's ability to reason over lengthy external context.
Ensure the model can generate structured outputs (e.g., JSON, markdown, lists, tables, code) when required.
Train the model to cite sources and identify relevant spans within the context (json object of citations).
Allow the model to fill in gaps and extrapolate using its own knowledge, unless explicitly instructed not to: modes such as “grounded-in-context”

Requirements:

Use a 7B model for open-source fine-tuning to balance performance and computational resources.
Optimize for low latency (100-250ms) to match the RAG pipeline.
Incorporate function calling for multi-turn extraction and recursive input processing.
Prioritize recall with reasoning over just recall.
Include a relevance score for context-query pairs – metadata such as similarity scores may be useful
Add a "response mode" to switch between verbose and structured outputs.
Use a <scratchpad> as part of the system prompt to jot down thought process/reasoning/planning for extraction tasks.
Allow the model to generate outputs in various formats, not just markdown.
Cite sources such as URL, document, page, speaker, or author when applicable.

Syntax:


Input:

        Possible input syntax:

XML delimitation of sections such as <query>, <scratchpad>, <instructions>. <documents>, <examples> etc.
Semi-structured: markdown/csv for tabular data
Graph DB: chunk documents into parent/child nodes
Tool retrieval
Process:

        RAG frameworks:

Hypothetical Document Embeddings (HyDE)
Self-query (Query decomposition)
Hybrid search (RAG fusion: Reciprocal Rank Fusion)
Multi-turn extraction (Map-reduce?)
Hierarchical embeddings (summary->chunks, RAPTOR)
Full text search query generation
DB metadata guidance
        

Output:

        Variations for structured output:

Output in markdown syntax
Mixed syntax with xml for evidences (Claude), json for citations (Command-R)

Added Tokens:

INPUTS:

<query> </query>

<documents> </documents>

<style_guide> </style_guide>

<examples> </examples>

<schema> </schema>

<response_mode> </response_mode>

OUTPUTS:

<scratch_pad> </scratch_pad>

<citations> </citations>

<metrics> </metrics>

        

Getting up to speed:


Approach in a simple manner and get an overview:
https://speakerdeck.com/pamelafox/building-a-rag-app-to-chat-with-your-data-on-azure

A lot of comparisons and good practices for RAG systems:
https://techcommunity.microsoft.com/t5/ai-azure-ai-services-blog/azure-ai-search-outperforming-vector-search-with-hybrid/ba-p/3929167

