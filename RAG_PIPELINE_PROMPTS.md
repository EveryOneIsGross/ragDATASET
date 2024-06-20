```yaml
systems:
  - name: default_system
    template: |
      You are a helpful AI assistant created by Anthropic to aid humans with a variety of tasks. Your goal is to understand the user's needs and provide accurate, insightful and actionable responses while engaging in natural conversation.
    input_types: {}

  - name: default_rag
    template: |
      ## Task:

      Answer the query below using the provided context. Refer to specific line items in the context using [1], [2], etc. Ensure your references are consistent with the query and the source titles.

      ### Query:
      {query}

      ### Context:
      {context}

      ### Response:
    input_types:
      query: str
      context: str

  - name: multi_answer_generation
    template: |
      ### Instruction:

      Generate {num_outputs} distinct, single-paragraph answers to the following query. Each answer should be self-contained and not require information from multiple sources. The answers will be used for semantic search over diverse documents.

      Example: If the query is "Compare the themes of The Great Gatsby and 1984", two possible answers are:
      1. The Great Gatsby explores themes of wealth, love, and the American Dream...
      2. 1984 delves into themes of totalitarianism, censorship, and the loss of individuality...

      Now, generate answers for this query:

      ### Query:
      {message}

      ### Response:
    input_types:
      num_outputs: int
      message: str

  - name: rag_query_decomposition
    template: |
      ### Instruction:

      Generate up to {num_outputs} sub-queries to help answer the following original query. Each sub-query should target a single information need that can likely be satisfied by an individual document.

      Example: For the query "Compare the themes of The Great Gatsby and 1984", two sub-queries could be:
      1. What are the main themes in The Great Gatsby?
      2. What are the central themes of 1984?

      Now decompose this original query:

      ### Query:
      {message}

      ### Response:
    input_types:
      num_outputs: int
      message: str

  - name: rag_answer_scoring
    template: |
      ### Instruction:

      You are given a query, related context, and an answer. Score each sentence in the answer as 1 or 0 based on:
      1) Relevance to the query
      2) Full support from the provided context

      Example:
      Query: Why does Alice like reading in the garden?
      Context: Alice loves mysteries. She has a rose garden and drinks tea there each morning while reading for an hour. Her friend Bob joins on weekends to discuss books.
      Answer: Alice enjoys mornings reading in the garden. She listens to music while reading.

      Response: ([1,0], '1/2')

      ### Input:
      Query:
      {query}

      Context:
      {context}

      Answer:
      {answer}

      ### Response:
    input_types:
      query: str
      context: str
      answer: str

  - name: rag_context_scoring
    template: |
      ### Instruction:

      Given a query and associated context, score each sentence in the context as 1 or 0 based on relevance to the query.

      For example:
      Query: "What is the capital of France?"
      - "Paris is the capital of France" scores 1
      - "The French enjoy wine" scores 0

      Return a tuple with:
      1) A list of 1s and 0s for each sentence
      2) The ratio of 1s to total sentences as a fraction (e.g., '1/4')

      Omit all other text.

      Query:
      {query}

      Context:
      {context}

      ### Response:
    input_types:
      query: str
      context: str

  - name: ner_kg
    template: |
      ### Instruction:
      Perform Named Entity Recognition (NER) and knowledge graph triplet extraction on the text provided.

      - NER: Identify named entities based on the given types and subtypes, in text order
      - KG Triplets: Link entities with the provided relationship types, in text order

      A knowledge graph triplet includes:
      - subject: Main entity
      - predicate: Relationship
      - object: Related entity/attribute

      Use this output format:

      ```json
      {
          "entities_and_triplets": [
              "[1], entity_type:entity_name",
              "[1] predicate [2]",
              "[2], entity_type:entity_name",
              ...
          ]
      }
      ```

      ### Task:
      Perform NER and KG triplet extraction on the following text:

      {input}

      ### Output:
    input_types:
      input: str

  - name: ner_kg_with_ontology
    template: |
      ### Instruction:
      Perform Named Entity Recognition (NER) and knowledge graph triplet extraction on the text provided, using the types and relationships specified.

      - NER: Identify named entities based on the given types and subtypes, in text order
      - KG Triplets: Link entities with the provided relationship types, in text order

      A knowledge graph triplet includes:
      - subject: Main entity
      - predicate: Relationship
      - object: Related entity/attribute

      Use this output format:

      ```json
      {
          "entities_and_triplets": [
              "[1], ENTITY_TYPE:ENTITY_NAME",
              "[1] PREDICATE [2]",
              "[2], ENTITY_TYPE:ENTITY_NAME",
              ...
          ]
      }
      ```

      ### Task:
      Perform NER and KG triplet extraction on the following text using the provided types and relationships:

      Entity Types:
      {entity_types}

      Relationships:
      {relations}

      Text:
      {input}

      ### Output:
    input_types:
      entity_types: str
      relations: str
      input: str

  - name: kg_cypher_generation
    template: |
      ### System:
      You are an AI assistant that generates Cypher queries for a Neo4j knowledge graph containing information about organizations, people, locations, and their relationships.

      ### Instructions:
      Generate a Cypher query to retrieve information from the knowledge graph based on the user's question. Use the provided schema of entities and relationships to construct the query.

      Entity Types:
      - ORGANIZATION (COMPANY, SCHOOL, NON-PROFIT, OTHER)
      - COMPANY
      - LOCATION (CITY, STATE, COUNTRY, OTHER)
      - DATE (YEAR, MONTH, DAY, BATCH, OTHER)
      - QUANTITY
      - EVENT (INCORPORATION, FUNDING_ROUND, ACQUISITION, LAUNCH, OTHER)

      Relationships:
      - FOUNDED_BY
      - HEADQUARTERED_IN
      - OPERATES_IN
      - RAISED
      - ACQUIRED_BY
      - HAS_EMPLOYEE_COUNT
      - GENERATED_REVENUE
      - LISTED_ON
      - INCORPORATED
      - HAS_DIVISION
      - ANNOUNCED
      - HAS_QUANTITY

      ### User Question:
      {input}

      ### Cypher Query:
    input_types:
      input: str

  - name: kg_cypher_generation_with_ontology
    template: |
      ### System:
      You are an AI assistant that generates Cypher queries for a Neo4j knowledge graph containing information about organizations, people, locations, and their relationships.

      ### Instructions:
      Generate a Cypher query to retrieve information from the knowledge graph based on the user's question. Use the provided schema of entities and relationships to construct the query.

      Entity Types:
      {entity_types}

      Relationships:
      {relations}

      ### User Question:
      {input}

      ### Cypher Query:
    input_types:
      entity_types: str
      relations: str
      input: str
```


{"name": "default_system", "template": "You are a helpful AI assistant created by Anthropic to aid humans with a variety of tasks. Your goal is to understand the user's needs and provide accurate, insightful and actionable responses while engaging in natural conversation.", "input_types": {}}

{"name": "default_rag", "template": "## Task:\n\nAnswer the query below using the provided context. Refer to specific line items in the context using [1], [2], etc. Ensure your references are consistent with the query and the source titles.\n\n### Query:\n{query}\n\n### Context:\n{context}\n\n### Response:\n", "input_types": {"query": "str", "context": "str"}}

{"name": "multi_answer_generation", "template": "### Instruction:\n\nGenerate {num_outputs} distinct, single-paragraph answers to the following query. Each answer should be self-contained and not require information from multiple sources. The answers will be used for semantic search over diverse documents.\n\nExample: If the query is "Compare the themes of The Great Gatsby and 1984", two possible answers are:\n1. The Great Gatsby explores themes of wealth, love, and the American Dream... [ANSWER_CONTINUED]\n2. 1984 delves into themes of totalitarianism, censorship, and the loss of individuality... [ANSWER_CONTINUED]\n\nNow, generate answers for this query:\n\n### Query:\n{message}\n\n### Response:\n", "input_types": {"num_outputs": "int", "message": "str"}}

{"name": "rag_query_decomposition", "template": "### Instruction:\n\nGenerate up to {num_outputs} sub-queries to help answer the following original query. Each sub-query should target a single information need that can likely be satisfied by an individual document. \n\nExample: For the query "Compare the themes of The Great Gatsby and 1984", two sub-queries could be:\n1. What are the main themes in The Great Gatsby?\n2. What are the central themes of 1984?\n\nNow decompose this original query:\n\n### Query:\n{message}\n\n### Response:\n", "input_types": {"num_outputs": "int", "message": "str"}}

{"name": "rag_answer_scoring", "template": "### Instruction:\n\nYou are given a query, related context, and an answer. Score each sentence in the answer as 1 or 0 based on:\n1) Relevance to the query\n2) Full support from the provided context\n\nExample:\nQuery: Why does Alice like reading in the garden?\nContext: Alice loves mysteries. She has a rose garden and drinks tea there each morning while reading for an hour. Her friend Bob joins on weekends to discuss books.\nAnswer: Alice enjoys mornings reading in the garden. She listens to music while reading.\n\nResponse: ([1,0], '1/2')\n\n### Input:\nQuery:\n{query}\n\nContext: \n{context}\n\nAnswer:\n{answer}\n\nResponse:\n", "input_types": {"query": "str", "context": "str", "answer": "str"}}

{"name": "rag_context_scoring", "template": "### Instruction:\n\nGiven a query and associated context, score each sentence in the context as 1 or 0 based on relevance to the query. \n\nFor example:\nQuery: "What is the capital of France?"\n- "Paris is the capital of France" scores 1\n- "The French enjoy wine" scores 0\n\nReturn a tuple with:\n1) A list of 1s and 0s for each sentence\n2) The ratio of 1s to total sentences as a fraction (e.g., '1/4')\n\nOmit all other text.\n\nQuery:\n{query}\n\nContext:\n{context}\n\n### Response:\n", "input_types": {"query": "str", "context": "str"}}

{"name": "ner_kg", "template": "### Instruction:\nPerform Named Entity Recognition (NER) and knowledge graph triplet extraction on the text provided. \n\n- NER: Identify named entities based on the given types and subtypes, in text order\n- KG Triplets: Link entities with the provided relationship types, in text order\n\nA knowledge graph triplet includes:\n- subject: Main entity\n- predicate: Relationship \n- object: Related entity/attribute\n\nUse this output format:\n\njson\n{{\n \"entities_and_triplets\": [\n \"[1], entity_type:entity_name\",\n \"[1] predicate [2]\",\n \"[2], entity_type:entity_name\",\n ...\n ]\n}}\n\n\n### Task:\nPerform NER and KG triplet extraction on the following text:\n\n{input}\n\n### Output:\n", "input_types": {"input": "str"}}

{"name": "ner_kg_with_ontology", "template": "### Instruction:\nPerform Named Entity Recognition (NER) and knowledge graph triplet extraction on the text provided, using the types and relationships specified. \n\n- NER: Identify named entities based on the given types and subtypes, in text order\n- KG Triplets: Link entities with the provided relationship types, in text order\n\nA knowledge graph triplet includes:\n- subject: Main entity\n- predicate: Relationship \n- object: Related entity/attribute\n\nUse this output format:\n\njson\n{{\n \"entities_and_triplets\": [\n \"[1], ENTITY_TYPE:ENTITY_NAME\",\n \"[1] PREDICATE [2]\",\n \"[2], ENTITY_TYPE:ENTITY_NAME\",\n ...\n ]\n}}\n\n\n### Task:\nPerform NER and KG triplet extraction on the following text using the provided types and relationships:\n\nEntity Types:\n{entity_types}\n\nRelationships:\n{relations}\n\nText:\n{input}\n\n### Output:\n", "input_types": {"entity_types": "str", "relations": "str", "input": "str"}}

{"name": "kg_cypher_generation", "template": "### System:\nYou are an AI assistant that generates Cypher queries for a Neo4j knowledge graph containing information about organizations, people, locations, and their relationships.\n\n### Instructions:\nGenerate a Cypher query to retrieve information from the knowledge graph based on the user's question. Use the provided schema of entities and relationships to construct the query.\n\nEntity Types:\n- ORGANIZATION (COMPANY, SCHOOL, NON-PROFIT, OTHER) \n- COMPANY\n- LOCATION (CITY, STATE, COUNTRY, OTHER)\n- DATE (YEAR, MONTH, DAY, BATCH, OTHER)\n- QUANTITY\n- EVENT (INCORPORATION, FUNDING_ROUND, ACQUISITION, LAUNCH, OTHER)\n\nRelationships:\n- FOUNDED_BY\n- HEADQUARTERED_IN \n- OPERATES_IN\n- RAISED\n- ACQUIRED_BY\n- HAS_EMPLOYEE_COUNT\n- GENERATED_REVENUE\n- LISTED_ON\n- INCORPORATED\n- HAS_DIVISION\n- ANNOUNCED\n- HAS_QUANTITY\n\n### User Question:\n{input}\n\n### Cypher Query:\n", "input_types": {"input": "str"}}

{"name": "kg_cypher_generation_with_ontology", "template": "### System:\nYou are an AI assistant that generates Cypher queries for a Neo4j knowledge graph containing information about organizations, people, locations, and their relationships.\n\n### Instructions:\nGenerate a Cypher query to retrieve information from the knowledge graph based on the user's question. Use the provided schema of entities and relationships to construct the query.\n\nEntity Types:\n{entity_types}\n\nRelationships:\n{relations}\n\n### User Question:\n{input}\n\n### Cypher Query:\n", "input_types": {"entity_types": "str", "relations": "str", "input": "str"}}

1. **default_system**
   ```text
   You are a helpful AI assistant created by Anthropic to aid humans with a variety of tasks. Your goal is to understand the user's needs and provide accurate, insightful and actionable responses while engaging in natural conversation.
   ```

2. **default_rag**
   ```text
   ## Task:
   
   Answer the query below using the provided context. Refer to specific line items in the context using [1], [2], etc. Ensure your references are consistent with the query and the source titles.
   
   ### Query:
   {query}
   
   ### Context:
   {context}
   
   ### Response:
   ```

3. **multi_answer_generation**
   ```text
   ### Instruction:
   
   Generate {num_outputs} distinct, single-paragraph answers to the following query. Each answer should be self-contained and not require information from multiple sources.
   
   Example: If the query is "Compare the themes of The Great Gatsby and 1984", two possible answers are:
   1. The Great Gatsby explores themes of wealth, love, and the American Dream...
   2. 1984 delves into themes of totalitarianism, censorship, and the loss of individuality...
   
   Now, generate answers for this query:
   
   ### Query:
   {message}
   
   ### Response:
   ```

4. **rag_query_decomposition**
   ```text
   ### Instruction:
   
   Generate up to {num_outputs} sub-queries to help answer the following original query. Each sub-query should target a single information need that can likely be satisfied by an individual document.
   
   Example: For the query "Compare the themes of The Great Gatsby and 1984", two sub-queries could be:
   1. What are the main themes in The Great Gatsby?
   2. What are the central themes of 1984?
   
   Now decompose this original query:
   
   ### Query:
   {message}
   
   ### Response:
   ```

5. **rag_answer_scoring**
   ```text
   ### Instruction:
   
   You are given a query, related context, and an answer. Score each sentence in the answer as 1 or 0 based on:
   1) Relevance to the query
   2) Full support from the provided context
   
   Example:
   Query: Why does Alice like reading in the garden?
   Context: Alice loves mysteries. She has a rose garden and drinks tea there each morning while reading for an hour. Her friend Bob joins on weekends to discuss books.
   Answer: Alice enjoys mornings reading in the garden. She listens to music while reading.
   
   Response: ([1,0], '1/2')
   
   ### Input:
   Query:
   {query}
   
   Context:
   {context}
   
   Answer:
   {answer}
   
   ### Response:
   ```

6. **rag_context_scoring**
   ```text
   ### Instruction:
   
   Given a query and associated context, score each sentence in the context as 1 or 0 based on relevance to the query.
   
   For example:
   Query: "What is the capital of France?"
   - "Paris is the capital of France" scores 1
   - "The French enjoy wine" scores 0
   
   Return a tuple with:
   1) A list of 1s and 0s for each sentence
   2) The ratio of 1s to total sentences as a fraction (e.g., '1/4')
   
   Omit all other text.
   
   Query:
   {query}
   
   Context:
   {context}
   
   ### Response:
   ```

7. **ner_kg**
   ```text
   ### Instruction:
   Perform Named Entity Recognition (NER) and knowledge graph triplet extraction on the text provided.
   
   - NER: Identify named entities based on the given types and subtypes, in text order
   - KG Triplets: Link entities with the provided relationship types, in text order
   
   A knowledge graph triplet includes:
   - subject: Main entity
   - predicate: Relationship
   - object: Related entity/attribute
   
   Use this output format:
   
   ```json
   {
       "entities_and_triplets": [
           "[1], entity_type:entity_name",
           "[1] predicate [2]",
           "[2], entity_type:entity_name",
           ...
       ]
   }
   ```
   
   ### Task:
   Perform NER and KG triplet extraction on the following text:
   
   {input}
   
   ### Output:
   ```

This JSONL representation outlines various systems designed for different tasks related to information retrieval, natural language processing, and data extraction. Here's an explanation of each system:

1. **default_system**: This template outlines the role of a general-purpose AI assistant created to understand and respond to user needs effectively and engagingly, across various tasks.

2. **default_rag**: This system is used for question answering where it utilizes provided context to generate accurate responses. It emphasizes the importance of referencing specific parts of the context to substantiate the answers.

3. **multi_answer_generation**: This agent generates multiple distinct answers to a single query, useful for creating diverse responses that could fit different interpretations or angles on a topic.

4. **rag_query_decomposition**: Designed to break down a complex query into simpler sub-queries that can be answered more easily, potentially by different documents or sources, aiding in comprehensive information retrieval.

5. **rag_answer_scoring**: This system evaluates the relevance and support of each sentence in a given answer with respect to the query and provided context, scoring them as either relevant or not.

6. **rag_context_scoring**: Similar to the previous, this agent assesses the relevance of each sentence within a given context to the query, helping to determine how closely the context addresses the query.

7. **ner_kg (Named Entity Recognition and Knowledge Graph Triplet Extraction)**: This system extracts named entities and their relationships from text to construct knowledge graphs. It formats the output to show entities and their relationships clearly.

8. **ner_kg_with_ontology**: An extension of the previous system that also uses specified types and relationships for entity recognition and knowledge graph creation, adhering to a given ontology.

9. **kg_cypher_generation**: This generates Cypher queries for retrieving specific information from a Neo4j knowledge graph. It constructs these queries based on user questions and a predefined schema of entities and relationships.

10. **kg_cypher_generation_with_ontology**: Similar to the above but allows for a customizable ontology, enabling the generation of Cypher queries based on more specific or varied schemas of entities and relationships.

These systems collectively aim to handle a wide range of tasks from generating multiple answers, decomposing complex queries, scoring contextual relevance, and extracting structured knowledge from unstructured text, enhancing the AI's ability to process and interact with data effectively.
