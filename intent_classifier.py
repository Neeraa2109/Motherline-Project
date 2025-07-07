
def classify_intent(user_input):
    user_input = user_input.lower()

    # Keywords per intent (English + Tamil)
    intent_keywords = {
        "nutrition": [
            "eat", "food", "diet", "hemoglobin", "immunity", "diabetic",
            "iron", "sugar", "blood pressure", "boost",
            "உணவு", "கீரை", "இம்யூனிட்டி", "இரும்பு", "சர்க்கரை", "ஹீமோகுளோபின்"
        ],
        "medicine": [
            "paracetamol", "ibuprofen", "antibiotic", "medicine", "safe",
            "pregnancy", "pain", "fever",
            "பராசிட்டமால்", "மருந்து", "பாதுகாப்பா", "கர்ப்பம்", "காய்ச்சல்"
        ],
        "emergency": [
            "heart attack", "snake bite", "dengue", "emergency", "hospital",
            "symptoms", "bleeding", "immediate", "chest pain",
            "அவசரம்", "மருத்துவமனை", "பாம்பு", "மார்புவலி", "டெங்கு", "இரத்தம்"
        ]
    }

    # Check for keywords in input
    for intent, keywords in intent_keywords.items():
        if any(keyword in user_input for keyword in keywords):
            return intent

    return "unknown"

# Example usage
if __name__ == "__main__":
    test_questions = [
        "What to eat when hemoglobin is low?",
        "Is paracetamol safe during pregnancy?",
        "What are the symptoms of a heart attack?",
        "Can I take antibiotics for viral fever?",
        "What foods should diabetic patients eat?",
        "What should I do in case of a snake bite?",
        "What are symptoms of dengue?",
        "Can I take ibuprofen during pregnancy?",
        "How can I reduce high blood pressure naturally?",
        "What foods boost immunity?",
        "கர்ப்ப காலத்தில் பராசிட்டமால் சாப்பிடலாமா?",
        "நீரிழிவுக்கு என்ன உணவு நல்லது?",
        "பாம்பு கடித்தால் என்ன செய்ய வேண்டும்?",
        "ஹீமோகுளோபின் குறைவு என்றால் என்ன சாப்பிடலாம்?"
    ]

    for q in test_questions:
        print(f"Q: {q}")
        print(f"=> Intent: {classify_intent(q)}\n")
