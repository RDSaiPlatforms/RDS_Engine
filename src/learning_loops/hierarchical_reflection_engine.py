from config import client

class HierarchicalReflectionEngine:
    def generate_reflection(self, user_input, ai_response, level="shallow"):
        """
        Generate reflection at different levels of depth.
        Levels:
        - shallow: Reflect on the immediate response.
        - medium: Reflect across the session, incorporating user goals and changes in mood.
        - deep: Reflect across multiple sessions, identifying key patterns and long-term behavior.
        """
        if level == "shallow":
            reflection_prompt = (
                f"User input: {user_input}\n"
                f"AI response: {ai_response}\n"
                "Reflect on this interaction and suggest any immediate improvements."
            )
        elif level == "medium":
            reflection_prompt = (
                f"Session Reflection:\n"
                f"User input: {user_input}\n"
                f"AI response: {ai_response}\n"
                "Reflect on the entire session, including changes in user mood and goals."
            )
        elif level == "deep":
            reflection_prompt = (
                f"Long-term Reflection:\n"
                f"Over multiple sessions, the user has interacted as follows: '{user_input}'. "
                f"AI responses were: '{ai_response}'. "
                "What long-term patterns can be identified in user behavior and AI responses?"
            )
        else:
            raise ValueError("Invalid reflection level. Use 'shallow', 'medium', or 'deep'.")

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI that reflects on its own actions and decisions."},
                    {"role": "user", "content": reflection_prompt}
                ],
                max_tokens=200
            )
            reflection = response.choices[0].message.content.strip()
            return reflection
        except Exception as e:
            print(f"Error during reflection generation: {e}")
            return "Reflection could not be generated."
        