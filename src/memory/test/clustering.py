from collections import defaultdict
class Clustering:
    def cluster_memories(self):
        """
        Group memories into clusters based on their metadata tags (e.g., category, context).
        Returns a dictionary of clusters where keys are tags and values are lists of memories.
        """
        clusters = defaultdict(list)
        
        for memory in self.memory_storage:
            category = memory['metadata'].get('category', 'general')
            context = memory['metadata'].get('context', 'default')
            intent = memory['metadata'].get('intent', 'ask')

            clusters[(category, context, intent)].append(memory)

        return clusters