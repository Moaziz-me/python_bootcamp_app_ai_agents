import json

with open("questions.json", "r") as file:
    data = file.read()

data = json.loads(data)



for q in data:
    print(q["question_text"])
    for i, a in enumerate(q["alternatives"]):
        print(i+1, "-", a)
    user_choice = int(input("Enter your choice: "))
    q["user_choice"] = user_choice


score = 0
for q in data:
    if q["user_choice"] == q["correct_answer"]:
        score = score + 1
        result = "Correct Answer"
    else:
        result = "Incorrect Answer"

    message = f"Your answer: {q['user_choice']},"\
            f"Correct Answer: {q['correct_answer']}"
    print(message)
print(score, "/", len(data))