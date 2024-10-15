def main():
    memory_system = MemorySystem()
    reflective_learning = ReflectiveLearning(memory_system)

    while True:
        # Simulate user input
        user_input = input("Enter your input: ")
        if user_input.lower() == "exit":
            break

        metadata = {
            'sentiment': 'neutral',
            'category': 'general',
            'strategy': 'informative'
        }

        ai_reflection = f"Reflecting on input: {user_input}"
        ai_response = f"Responding to: {user_input}"

        memory_system.store_interaction(user_input, ai_reflection, ai_response, metadata)

        interaction_data = {
            'user_input': user_input,
            'emotion': metadata['sentiment'],
            'category': metadata['category']
        }
        reflective_learning.feedback_loop(interaction_data)

        print(f"AI Response: {ai_response}")

if __name__ == "__main__":
    main()