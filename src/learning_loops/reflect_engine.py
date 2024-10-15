from config import client

class ReflectionEngine:
    def generate_reflection(self, user_input, ai_response):
        """
        Generates a reflection on the AI's response to the user's input, using OpenAI's GPT model.
        """
        reflection_prompt = (
            f"User input: {user_input}\n"
            f"AI response: {ai_response}\n"
            "What did the AI learn from this interaction? Reflect and suggest improvements."
        )

        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an AI that generates reflections based on previous interactions."},
                    {"role": "user", "content": reflection_prompt}
                ],
                max_tokens=200
            )
            reflection = response.choices[0].message.content.strip()
            return reflection
        except Exception as e:
            print(f"Error during reflection generation: {e}")
            return "Reflection could not be generated."