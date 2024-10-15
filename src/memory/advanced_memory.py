import json
import os
from datetime import datetime

class AdvancedMemorySystem:
    def __init__(self, memory_file="long_term_memory.json", short_term_limit=10):
        self.memory_file = memory_file
        self.memory_storage = self.load_memory()
        self.short_term_memory = []
        self.short_term_limit = short_term_limit

    def load_memory(self):
        if os.path.exists(self.memory_file):
            with open(self.memory_file, 'r') as f:
                return json.load(f)
        else:
            return []

    def save_memory(self):
        with open(self.memory_file, 'w') as f:
            json.dump(self.memory_storage, f, indent=4)

    def store_interaction(self, user_input, ai_reflection, ai_response, metadata, memory_type="short_term"):
        """
        Store an interaction in either short-term or long-term memory.
        Short-term memory has a limited size and decays over time.
        """
        timestamp = str(datetime.now())
        memory_entry = {
            'user_input': user_input,
            'ai_reflection': ai_reflection,
            'ai_response': ai_response,
            'timestamp': timestamp,
            'metadata': metadata
        }

        if memory_type == "short_term":
            self.short_term_memory.append(memory_entry)
            if len(self.short_term_memory) > self.short_term_limit:
                self.short_term_memory.pop(0) 
        elif memory_type == "long_term":
            self.memory_storage.append(memory_entry)
            self.save_memory()

    def retrieve_relevant_memory(self, sentiment=None, category=None, memory_type="short_term"):
        """
        Retrieve relevant memories from either short-term or long-term storage.
        """
        memory_pool = self.short_term_memory if memory_type == "short_term" else self.memory_storage
        for memory in reversed(memory_pool):
            if (sentiment and memory['metadata'].get('sentiment') == sentiment) or \
               (category and memory['metadata'].get('category') == category):
                return memory
        return None
        