import json
import os
from datetime import datetime

class MemorySystem:
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
        Store a new interaction in memory with an initial weight and timestamp.
        Each memory will have a weight that reflects its relevance and priority.
        """
        timestamp = str(datetime.now())
        memory_entry = {
            'user_input': user_input,
            'ai_reflection': ai_reflection,
            'ai_response': ai_response,
            'weight': 1,  # Initial weight
            'timestamp': timestamp,
            'metadata': {
                'sentiment': metadata.get('sentiment'),
                'category': metadata.get('category'),
                'strategy': metadata.get('strategy')
            }
        }

        if not self.memory_storage or self.memory_storage[-1] != memory_entry:
            self.memory_storage.append(memory_entry)
            self.save_memory()

    def prioritize_memory(self):
        """
        Update memory weights based on relevance and usage.
        Memories that are accessed more frequently or recalled during reflection
        get a higher weight.
        """
        for memory in self.memory_storage:
            memory['weight'] += 1  
            self.save_memory()

    def retrieve_relevant_memory(self, emotion=None, category=None):
        """
        Retrieve the most relevant memory based on emotion, category, and weight.
        Memories with higher weights are prioritized, and we search in reverse order.
        """
        relevant_memories = [
            memory for memory in reversed(self.memory_storage)
            if (emotion and memory['metadata'].get('sentiment') == emotion) or
               (category and memory['metadata'].get('category') == category)
        ]

        if relevant_memories:
            relevant_memories.sort(key=lambda x: x['weight'], reverse=True)
            return relevant_memories[0] 
        return None

    def decay_memory_weights(self):
        """
        Decay the weights of memories over time so older, less relevant memories
        naturally become less important unless recalled.
        """
        for memory in self.memory_storage:
            memory['weight'] *= 0.95 
            self.save_memory()
