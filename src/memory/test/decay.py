class MemorySystem:
    def forget_memory(self, condition):
        """
        Forget memories based on a given condition (e.g., category, context, or user input).
        """
        self.memory_storage = [
            memory for memory in self.memory_storage
            if not condition(memory)
        ]
        self.save_memory()

def forget_category(memory_system, category):
    memory_system.forget_memory(lambda memory: memory['metadata'].get('category') == category)