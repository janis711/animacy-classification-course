from transformers import AutoTokenizer, AutoModel
import torch
import numpy as np
from sklearn.base import BaseEstimator

class BertEmbeddings(BaseEstimator):
    def __init__(self, model_name="severinsimmler/literary-german-bert"):
        """
        Extract features using a fine-tuned BERT model.

        Parameters:
        - model_name: The name of the BERT model to use.
        """
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModel.from_pretrained(model_name)

    def fit(self, X, y=None):
        return self

    

    def transform(self, X):
        embeddings = []
        max_length = 512  # Maximum number of tokens for BERT

        for j, doc in enumerate(X):
            # print(f'Doc number: {j}')
            tokens = [word[0] for word in doc]  # Extract tokens

            # Tokenize the document
            inputs = self.tokenizer(tokens, is_split_into_words=True, return_tensors="pt", padding=False, truncation=False)
            word_ids = inputs.word_ids()

            # Split into batches
            input_batches = []
            word_ids_batches = []
            for i in range(0, len(inputs['input_ids'][0]), max_length):
                batch_input_ids = inputs['input_ids'][:, i:i + max_length]
                batch_attention_mask = inputs['attention_mask'][:, i:i + max_length]
                batch_word_ids = word_ids[i:i + max_length]
                
                # If the batch size is less than max_length, pad the batch
                if batch_input_ids.shape[1] < max_length:
                    padding_length = max_length - batch_input_ids.shape[1]
                    
                    # Pad input_ids, attention_mask, and word_ids
                    batch_input_ids = torch.cat([batch_input_ids, torch.zeros((batch_input_ids.shape[0], padding_length), dtype=torch.long)], dim=1)
                    batch_attention_mask = torch.cat([batch_attention_mask, torch.zeros((batch_attention_mask.shape[0], padding_length), dtype=torch.long)], dim=1)
                    batch_word_ids = batch_word_ids + [None] * padding_length  # Adjust word_ids for padding

                batch = {
                    'input_ids': batch_input_ids,
                    'attention_mask': batch_attention_mask
                }
                input_batches.append(batch)
                word_ids_batches.append(batch_word_ids)

            # Process batches
            all_token_embeddings = []
            current_token_idx = None
            current_embedding = []

            for batch, word_ids in zip(input_batches, word_ids_batches):
                with torch.no_grad():
                    outputs = self.model(**batch)

                hidden_states = outputs.last_hidden_state.cpu().numpy()

                for i, word_id in enumerate(word_ids):
                    if word_id != current_token_idx:
                        # Finish the previous token
                        if current_token_idx is not None:
                            all_token_embeddings.append(np.mean(current_embedding, axis=0))
                        # Start a new token
                        current_token_idx = word_id
                        current_embedding = [hidden_states[0, i]] if word_id is not None else []
                    else:
                        # Continue aggregating the current token
                        if word_id is not None:
                            current_embedding.append(hidden_states[0, i])

            # Finish the last token
            if current_token_idx is not None and current_embedding:
                all_token_embeddings.append(np.mean(current_embedding, axis=0))

            # print(f'Length of token embeddings: {len(all_token_embeddings)}')
            # print(f'Length of tokens: {len(tokens)}')

            embeddings.append(np.array(all_token_embeddings))  # Add embeddings for the current document
            # print(f'Doc {j} finished')
        embeddings = np.vstack(embeddings)  # Stack embeddings from all documents
        # print(f'Shape of Bert Features: {embeddings.shape}')
        return embeddings




    def fit_transform(self, X, y=None):
        self.fit(X, y)
        return self.transform(X)
