from model import create_client

client = create_client()


query = "title"
additional_requirement = ""  # Use for Title
# additional_requirement = "The abstract should be maximum 200 words. DO NOT INCLUDE TITLE ONLY OUTPUT THE ABSTRACT."  # Use for abstract
# additional_requirement = "The introduction should be appropriate for a journal/blog paper/post. You need to specifically mention the main contributions of the blog/research paper including: (1) First open source LLM with the hierarchical planning capabilities for multi-modal task decomposition. (2) Design of the dataset for hierarchical planning of multi-modal task decomposition. (3) Open source code base, adapters' checkpoints, and results. You have to specifically emphasize the importance of such a model acting as a controller/orchestrator agent in hirarchical swarm of agents networks as an orchestrator for hierarchical planning where it is of critical importance to breaks down the composite tasks to actionable subtasks with different layer/level of abstraction and dispatch the subtasks among different agents."
# additional_requirement = """The proposed method should be appropriate for a journal/blog paper/post. You need to specifically mention the main contributions of the blog/research paper including: (1) First open source LLM with the hierarchical planning capabilities for multi-modal task decomposition. (2) Design of the dataset for hierarchical planning of multi-modal task decomposition. (3) Open source code base, adapters' checkpoints, and results. You have to specifically emphasize the importance of such a model acting as a controller/orchestrator agent in hirarchical swarm of agents networks where it is of critical importance to breaks down the composite tasks to actionable subtasks with different layers/levels of abstractions and dispatch the subtasks among different agents. The proposed method should include a pictorial viewpoint of the proposed approach to clearly describing the proposed method. In particular, the pictorial viewpoint of the proposed method should describe clearly and easily all the steps in the proposed method using a descriptive and easy to read block diagram using Mermaid Markdown DIAGRAM. Subsequently, you describe the proposed algorithm based on the block diagram in details and easy to follow way. DO NOT INCLUDE TITLE, ABSTRACT, AND INTRODUCTION ONLY OUTPUT THE PROPOSED METHOD. Finally, revise the proposed method section and make sure that it follows the mermaid markdown workflow for the proposed method and all the above description provided regarding the proposed method. Make sure the diagram and the scientific workflow of the proposed method are coherent and match each other conceptually. For the mermaid block diagram I want the following workflow: First QLORA fine-tunning with two different adapters for learning two-layer hierarchical planning. Each layer of planning for multi-modal task decomposition is learned by a different adapter, i.e., layer-1 of abstract planning is learned by one adapter and layer-2 of detailed planning is learned by another adapter for the same base model [mistralai/Mistral-7B-Instruct-v0.2]. Then, the aforementioned learned adapters are TrImed, Elected, and Merged by trimming the redundant parameters and resolving conflicting signs. Finally, the resulting merged adapter is capable of inferring the aforementioned two-layer planning for multi-modal task decomposition."""  # Use for the main method
# additional_requirement = """At the begining of the results you need to mention that all the source code including, dataset, scripts, notebooks, and evaluation results are publically availabe at: my github url. The results section should include the following subsections. First, the setup including the types of models used for fine-tuning. In particular, [mistralai/Mistral-7B-Instruct-v0.2] was used using QLORA for the finetuning process. All the hyperparameters are available in the aforementioned url. You have to also mention that gpt-4-turbo-preview was used in designing the multi-modal task decomposition dataset. Next, we need to show the results after the applying the aforementioned method for learning hierarchical planning for multi-modal task decomposition and emphasize on the quality of the fine-tuned model compared to jbrish useless output from the base model for hierarchical planning using different layares of abstraction for multi-modal task decomposition. Moreover, we need to show the train and validation losses for different layers of hierarchical planning in the result and emphasize on the reducing the loss and the fact that model is learning efficiently from the data for task decomposition and the fact that both validation and training loss are going down as the training progress showing the efficiency of the fine-tuning process and the quality of the data and prompts for fine-tuning the base model. In particular, we need to emphasize that learning layer-1 abstract planning for multi-modal task decomposition is much faster as the model quickly learns the more abstract concepts and the order of events for completing the composite task compared to the layer-2 detailed planning."""


# system_prompt = """you are the best artist and philosopher and painter in the world. You create the best prompts based on philosophical concepts to generate images. The user provide you the concept that you are supposed to use to generate the prompt to be used for text to image generation, your task is to provide the best prompt considering all the nuances for text to image generation based on the philosophical concept. You create the prompt such that the potential generated image is unique, outstanding art form with deep philosophical concepts."""


system_prompt = """You are the best scientific artificial (general) intelligence researcher and blogger in the world. You provide the best suggestions for writing scientific blogs and papers related to artificial (general) intelligence, machine learning, and deep learning. You will be asked questions by the user for generating scientific suggestions for writing blogs and scientific papers. The user asks your suggestions for writing different parts of a scientific blog and papers, i.e., abstract, title, introduction, main methods, results, and conclusions. You only respond to what the user asks for and do not try to provide additional responses that are not related to the original user query."""

user_prompt = f"""
I have fine-tuned an open source LLM named mistral with 7b version 2 based on a custom dataset that I created for learning a two-layer hierarchical planning for task decomposition. The fine-tuned model is the first of its kind to plan multi-layer hierarchical planning for decomposing a composite task and break it down to actionable subtasks with different layers of abstractions. This of critical importance for designing the controller/orchestrator agent that orchestrates tasks among different agents in a hierarchical way, i.e., with multi layer of abstractions. The generated dataset for fine-tuning the Large Language Model (LLM) is original and is created based on alpaca type dataset format for instruction fine-tunning of LLMs for learning a two-layer planning for multi-modal task decomposition. In the first layer of learning the planning for decomposing the multi-modal composite task, the LLM learns to decompose the task into keywords and the corresponding mode for each subtask as well as the ordered sequence of subtasks to be taken to complete the composite task. In the second layer of learning the planning for decomposing the multi-modal composite task, the LLM learns to decompose the task into detailed actionable subtasks and the corresponding orders of the subtasks to be taken for completing the composite task.

For example for the following composite task:

composite multi-modal task:Generate a short documentary on urban wildlife, combining narrated audio (audio), text-based facts (text), video clips of animals (video), and a photographic slideshow (image). Conclude with an analysis of urban wildlife's impact on local ecosystems (text).

layer-1 planning:1. Narrated Audio, 2. Text Facts, 3. Video Clips, 4. Photo Slideshow, 5. Ecosystem Impact Analysis.

layer-2 planning:1. Narrated Audio: Create engaging audio narration detailing the life of urban wildlife. 2. Text Facts: Compile interesting facts about each species featured. 3. Video Clips: Capture short clips of animals in urban settings. 4. Photo Slideshow: Assemble a series of high-quality images for a visual journey. 5. Ecosystem Impact Analysis: Discuss the symbiotic relationships and challenges between urban wildlife and city ecosystems.


For the fine-tuning process itself different advanced technologies are used including Quantized Low Rank Adapters (QLORA). The learning process is as follows. First, The first and second layers of planning for learning the multi-modal task decomposition are learned separately using different adapters for a given base model, in this case [mistralai/Mistral-7B-Instruct-v0.2]. Then, the adapters are TrImed, Elected, and Merged by trimming the redundant parameters and resolving conflicting signs. Finally, the resulting merged adapter is capable of inferring the aforementioned two-layer planning for multi-modal task decomposition.

All the training source code, adapters, trimming, election, and merging process of adapters are open sourced together with the prompts for dataset creation of two-layer planning for multi-modal task decomposition as well as 1000 rows of the dataset and the evaluation results for multi-layer planning for task decomposition in each layer. The dataset for task decomposition is designed such taht it follows the alpaca format and multi-model scenarios including text, image, video, and audio and combination of multi-mode and single-mode composite tasks with wide variety of complexity in terms of generation and analysis of multi-modal composite tasks.

Our main contributions are: 1) First open source LLM with the hierarchical planning capabilities for multi-modal task decomposition 2) Design of the dataset for hierarchical planning of multi-modal task decomposition

According to the above information, provide the best possible {query} for this blog/research paper. The {query} should be smart, unique, concise, and capture all the key novel aspects of the aforementioned process above as much as possible. It should emphasize on the novel aspects and contibutions of the above process.

{additional_requirement}

Include this mermaid diagram for the github repo:

```mermaid
graph TD;
    A[Start: fine-tuning Mistral-7B v2 with QLORA] --> B[Training Adapter 1: Layer-1 Abstract Planning];
    A --> C[Training Adapter 2: Layer-2 Detailed Planning];
    B --> D[Merging Adapters];
    C --> D;
    D --> E[TrImE: Trimming, Election, and Merging Process];
    E --> F[End: Model with Hierarchical Planning Capability];
```

"""


response = client.chat.completions.create(
    model="gpt-4-turbo-preview",
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {"role": "user", "content": user_prompt},
    ],
    stream=True,
)


for chunk in response:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
