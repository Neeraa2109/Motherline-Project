
# -*- coding: utf-8 -*-
import sys
import io

# Ensure UTF-8 encoding for Unicode (Tamil) output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def classify_intent(user_input):
    user_input = user_input.lower()

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

    for intent, keywords in intent_keywords.items():
        if any(keyword in user_input for keyword in keywords):
            return intent
    return "unknown"

# Predefined responses per intent
intent_responses = {
    "nutrition": """
✅ Nutrition Advice:
- Eat iron-rich foods like spinach, beetroot, pomegranate, lentils, and dates.
- Diabetics should eat whole grains, green vegetables, and low-sugar fruits like guava.
- Foods that boost immunity include citrus fruits, ginger, garlic, turmeric, and green tea.
""",
    "medicine": """
💊 Medicine Guidance:
- Paracetamol is generally safe during pregnancy (consult doctor first).
- Avoid ibuprofen during pregnancy.
- Antibiotics don’t work on viral infections — consult your physician.
""",
    "emergency": """
🚨 Emergency Symptoms:
- Heart attack: Chest pain, left arm pain, breathlessness.
- Snake bite: Stay calm, tie above bite, go to hospital immediately.
- Dengue: Fever, rash, joint pain — get tested and see a doctor.
""",
    "unknown": """
❓ Sorry, I didn't understand that clearly.
Please rephrase or consult a doctor directly for better help.
"""
}

# --- Chatbot loop ---
def chatbot():
    print("🩺 Welcome to the Health Assistant Chatbot!")
    print("You can ask me health-related questions in English or Tamil.")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("🧑 You: ").strip()
        if user_input.lower() == "exit":
            print("🤖 Chatbot: Take care! Stay healthy. Goodbye!")
            break

        intent = classify_intent(user_input)
        response = intent_responses[intent]
        print(f"🤖 Chatbot ({intent}):\n{response}")

if __name__ == "__main__":
    chatbot()
