from core.sentiment_analyzer import SentimentAnalyzer
from core.reflection_engine import ReflectionEngine
from core.strategy_generator import StrategyGenerator
from memory_system.memory_storage import MemoryStorage
from config import client
from colorama import init, Fore


init(autoreset=True)

class ReflectiveDialogueSystem:
    def __init__(self):
        self.memory_system = MemoryStorage()
        self.sentiment_analyzer = SentimentAnalyzer()
        self.reflection_engine = ReflectionEngine()
        self.strategy_generator = StrategyGenerator()

    def process_user_input(self, user_input):
        print("\n" + "=" * 50)
        print(f"User Input: {user_input}")

        
        question_type = self.detect_question_type(user_input)

        
        sentiment = self.sentiment_analyzer.analyze_sentiment(user_input)

        
        category = self.detect_category(user_input)
        relevant_memory = self.memory_system.retrieve_relevant_memory(sentiment=sentiment, category=category)

        
        if relevant_memory:
            internal_prompt = self.generate_internal_prompt(relevant_memory, user_input)
        else:
            internal_prompt = f"I'm thinking about the user's current input: '{user_input}', and it's a new topic."

        
        response_strategy = self.strategy_generator.generate_response_strategy(user_input, sentiment, internal_prompt, question_type)

        
        final_response = self.generate_final_response(user_input, response_strategy, internal_prompt, question_type)

        
        self.memory_system.store_interaction(
            user_input=user_input,
            ai_reflection=internal_prompt,
            ai_response=final_response,
            metadata={"sentiment": sentiment, "category": category, "strategy": response_strategy}
        )

        print("=" * 50 + "\n")
        return final_response

    def detect_question_type(self, user_input):
        return 'general' if '?' in user_input else 'technical'

    def detect_category(self, user_input):
        return 'general'

    def generate_internal_prompt(self, relevant_memory, user_input):
        past_user_input = relevant_memory['user_input']
        past_response = relevant_memory['ai_response']
        return (
            f"I'm considering the user's current input: '{user_input}', "
            f"and reflecting on a past interaction where the user said: '{past_user_input}', "
            f"and my response was: '{past_response}'. "
        )

    def generate_final_response(self, user_input, response_strategy, internal_prompt, question_type):
        return f"Based on {internal_prompt}, my response is: {response_strategy}"
    