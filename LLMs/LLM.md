The lifetime of an LLM is composed of 3 phases:
1. Pre-training is used to get a background knowledge ( base knowledge ) 
	1. It doesn't focus on _a_ specific topic; it learns _everything_ broadly. However, it doesn't know how to be a helpful assistant yet. If you type "What is capital of France?", a pre-trained base model might just output a list of random geography questions because it's just trying to predict the next word.
2. Post-training /  Supervised fine-tuning stage is where the model is trained on demonstrated examples
	1. This teaches the model how to follow instructions or behave in a specific domain/style.
	2. The main goal of SFT is teaching the model **how to act like an AI assistant**. It learns to see a question and give a direct, helpful answer instead of just completing text. While you _can_ use it to specialize a model on a specific topic (like medical data), its primary job is teaching the model format, tone, and safety restrictions.
3. Practise & Feedback stage uses Reinforcement Learning where instead of showing the AI examples of perfect answers to copy, we let the AI try to solve a problem on its own, and then we **reward it** for good answers and **penalize it** for bad ones.
	1. In modern "reasoning" models, RL is what teaches the AI to double-check its own math, notice its own mistakes, and try a different method before showing you the final answer. It is purely **learning through trial and error.**
## Pre-training stage
**Pre-training stage** which is composed by:
1. Download and pre-process internet ( tons of data in internet are taken , filtered and then cleaned in order to be transformed in file and used for training the llm ). FineWeb is an open source dataset of internet which has been produced by following these steps
![[Screenshot 2026-06-23 alle 17.44.50.png]]
	1. URL filtering -> we don't want webpages related to some dangerous themes.
	2. Text Extraction -> raw html from the webpages are processed to take only good content ( text/images )
	3. Language filtering -> we want just to remove some text based on its language ( e.g. spanish, italian ecc...)
	4. PII Removal ( Personal Identifible Information ) -> remove all the sensible data like SSN or password or anything
	5. All these filters are used to reduce and clean the dataset in order to full cover what we want our ai to be specialized.
2. Tokenization: letters are bit which can be grouped in bytes ( 8 bits are 1 byte ) and they can be represented with numbers from 0 to 255 ( think of it as IDs : text is encoded using UTF-8 ). LLMs do not usually process raw letters one by one. That would make sequences too long. Common byte sequences are merged into larger **tokens** and assigned new token IDs. This increases the vocabulary size but decreases the number of tokens needed to represent common text. **The tradeoff is: bigger vocabulary, shorter sequences.**
	1. Tokens are just text chunk represented with an id i order to reduce the length of the input to the llm. 
3. Neural Network Training: the data are divided into windows of tokens ( called contexts ) and the window length ( context length ) can change from 0 to a maximum length that we can decide. Very long windows are computational expensive. The input of the nn is the context ( the window ) which is used to predict the next token in the sequence.
![[Screenshot 2026-06-23 alle 18.35.59.png|559]]
The neural network outputs a probability distribution over the whole vocabulary, meaning it assigns a probability to each possible next token.
Training the nn means adjusting the weights so that its predictions match up the correct answers of the training dataset.
General Structure:
![[Screenshot 2026-06-23 alle 19.17.52.png|416]]
Let's explore model **nano-gpt** model with 85,000 parameters:
![[Screenshot 2026-06-23 alle 19.29.55.png|202]]
	1. Tokenizer: transform letters/words to token indices using a vocabulary.
	![[Screenshot 2026-06-23 alle 19.38.57.png|313]]
	2. Embeddings: each token id in the sequence gets turned into a 48 element vector ( a specific number for this model ) and the position information is then added to each token vector ( the model must know token order )
		1. We get a distributed representation of the token.
![[Screenshot 2026-06-23 alle 19.26.50.png|331]]
	3. Many Transformer Blocks
	4. Final Output Layer
		1. After many Transformer blocks, each token has a final vector. To predict the next token, the model uses the final vector at the last position and converts it into scores for every token in the vocabulary.
		2. If vocabulary size is 50,000, it outputs 50,000 numbers.
		3. Then softmax turns those numbers into probabilities and the model chooses or samples the next token.
A **base model** ( text completion behaviour ) is trained to predict the next token from huge amounts of text. It learns language, facts, code patterns, reasoning patterns, and styles, but its default behavior is basically: “continue this text.”
**Regurgitation**: A base model can answer to a prompt with an exact section of a document that has been used for training.
An **instruct model** ( assistant behaviour ) starts from a base model, then is further trained to follow user instructions. Usually this uses supervised fine-tuning on instruction/answer examples, and often preference training or RLHF/RLAIF so it becomes more helpful, conversational, and safer.
**base model = raw engine**, **instruct model = engine tuned into an assistant**.

Some of the company release the **base model** as Open ai with GPT-2 (1.6 billion of parameters trained on 100 billions of token ): they release the code which is quite standard and the parameters.

LLMs have **in-context learning** ability, meaning they can adapt their responses based on examples, instructions, and information provided in the current prompt/context, without updating their model weights.
The model’s parameters do **not** change during in-context learning. It is more like temporary pattern adaptation inside the current conversation or prompt. Once the context is gone, that adaptation is gone too.

**Summary:**
The objective of pre-training is to build a **base model** that learns general patterns of language, facts, reasoning skills, and domain knowledge from large amounts of text by compressing statistical regularities into its parameters

## Post-training / Supervised fine tuning SFT stage
We want to build a model which is able to act as an assistant: chat with people.
We train the model on new datasets of conversations ( it is an implicit way of programming llms, through specific datasets ).
The pre-training stage requires 3 months on a large set of GPUs while just 3 hours for the post-training stage.
The conversation dataset has a different structure of data: conversation are encoded using specific data structure which is then encoded in tokens. In this way the model understands the difference between normal text and conversation.
![[Screenshot 2026-06-28 alle 12.04.33.png|514]]
im_start is a new token that the model never saw before.
They build the datasets by hiring people or using synthetic data ( building conversations using other llms )

There are different type of mitigation strategies to reduce allucination ( model does not know an answer and it makes stuff up ):
1. The model answer is compared with the correct answer of a judge llm, if the answer is wrong than a new item in the data set is created where the answer to that question becomes " i don't know ".
2. The model is allowed to search/ use tools
	1. The model can output some specific tokens that can execute/call specific tools as web search: the result of the tools are then incorporated into the context window ( the memory of the llm for that conversation ). The information in the context window are then used to answer the question.
		1. **It is important to underlying the difference between knowledge in the parameters and in the tokens/context window**
			1. Knowledge in the parameters is a vague recollection 
			2. Knowledge in the context window is the working memory
	2. The model knows how to use these specific tools/tokens by feeding specific datasets for that
In LLMs, we should not expect all meaning or computation to be concentrated in a single token. **Meaning is usually distributed across multiple tokens**, their relationships, and the model’s internal representations
![[Screenshot 2026-06-28 alle 16.53.48.png|587]]
In this example the left answer is wrong because the answer is given in the third token which is dangerous: it is already in the context window and everything after is just a justification. The right answer is perfect: the computation is taken step by step and the reason is spread out on multiple tokens.

LLMs are bad in counting ( too few tokens that require a lot of computation, the workload is not spread out ), we should use explicitly tools (e.g. code ).
LLMs are bad in spelling ( models do not see characters but tokens )

**Summary:**
A base model is trained to become an assistant using a dataset of conversations and trying to reduce allucination.

## Practice & Feedback Stage ( RL )
Feedback is the judgment about the model’s output. The signal is the numeric training value derived from that feedback, used to update the model.
This stage can be a substage/subphase of the Supervised fine tuning stage.

What we do with Reinforcement Learning is to sample a lot of times an answer to a question and we want to encourage the kinds of solutions that are correct: the top solution is taken and the model is trained on that. This process is repeated for may many times.

DeepSeek was one of the first major companies to very publicly emphasize **large-scale RL for reasoning**, especially with DeepSeek-R1/R1-Zero in 2025: the model can generate explicit reasoning traces, including self-checking and backtracking-like revisions, but this is learned behavior in text generation rather than a guaranteed explicit search algorithm.

Many thinking models are post-trained with SFT plus RL, but not every thinking model must use RL.