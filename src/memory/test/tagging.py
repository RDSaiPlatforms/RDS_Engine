class Tagging:
    def __init__(self, memory_file="memory.json"):
        self.memory_file = memory_file
        self.memory_storage = self.load_memory()

    def load_memory(self):
        """
        Load memory from the memory file if it exists.
        """
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        else:
            return []

    def save_memory(self):
        """
        Save the current state of memory to the memory file.
        """
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory_storage, f, indent=4)

    def store_interaction(self, user_input, ai_reflection, ai_response, metadata):
        """
        Store a new interaction in memory, tagging it with more detailed metadata.
        """
        timestamp = str(datetime.now())
        memory_entry = {
            'user_input': user_input,
            'ai_reflection': ai_reflection,
            'ai_response': ai_response,
            'weight': 1,  
            'lifetime': 100, 
            'timestamp': timestamp,
            'metadata': {
                'sentiment': metadata.get('sentiment'),
                'category': metadata.get('category'),
                'strategy': metadata.get('strategy'),
                'context': metadata.get('context'), 
                'intent': metadata.get('intent'),    
                'importance': metadata.get('importance', 1)
            }
        }

        if not self.memory_storage or self.memory_storage[-1] != memory_entry:
            self.memory_storage.append(memory_entry)
            self.save_memory()

    def retrieve_relevant_memory(self, emotion=None, category=None, context=None, intent=None):
        """
        Retrieve the most relevant memory based on emotion, category, context, intent, and weight.
        """
        relevant_memories = [
            memory for memory in reversed(self.memory_storage)
            if (emotion and memory['metadata'].get('sentiment') == emotion) or
               (category and memory['metadata'].get('category') == category) or
               (context and memory['metadata'].get('context') == context) or
               (intent and memory['metadata'].get('intent') == intent)
        ]

        if relevant_memories:
            relevant_memories.sort(key=lambda x: (x['weight'], x['metadata']['importance']), reverse=True)
            return relevant_memories[0] 
        return None
    