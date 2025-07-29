Customizing Your Quiz Questions
You can customize the questions in this quiz by using the public question database from OpenTDB. This platform allows you to:

Search for trivia questions on your favorite topics.

Add your own custom questions.

Use it as a source for your quiz application.

🔧 How to Add Your Own Questions
Visit OpenTDB:

Go to OpenTDB

Find or create questions you like.

Add to Your Database:

Open data.py in your project directory.

Add your new questions to the question_data list in the following format:

question_data = [
    {"text": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"text": "What is the main programming language used in Android development?", "answer": "Java"},
    # Add more questions here...
]
Format the Code (Optional but Recommended):

In your IDE, click the Code menu and choose Reformat to make the question list more readable.

Check Key Names in main.py:

Open main.py.

Make sure the keys used in the question_data list match the ones used in the following lines:

q_text = list["text"]
q_answer = list["answer"]
If your custom data uses different keys (e.g., "question" and "correct_answer"), update the lines accordingly:

q_text = list["question"]
q_answer = list["correct_answer"]
This customization lets you tailor the quiz to any topic you're interested in — whether it's software development, movies, science, or pop culture.

📧 Need Help?
If you encounter any issues or have questions, feel free to reach out to:

berivanalpagu@gmail.com

Happy coding and enjoy building your personalized quiz app!
