import streamlit as st
import google.generativeai as genai
import textwrap
import os

def to_markdown(text):
    text = text.replace('•', '  *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

def get_user_input():
    # Predefined dictionary keys with default values
    inputs = {
        "recipe": st.text_input("Recipe"),
        "for": st.text_input("For (number of persons)"),
        "spicy": st.text_input("Spicy (mild/medium/spicy)"),
        "prep_time": st.number_input("Preparation Time"),
        "cook_time": st.number_input("Cooking Time")
    }
    return inputs 

def generate_prompt(inputs):
    # Function to generate the prompt based on user inputs
    prompt = f"Give me the recipe to cook {inputs['recipe']} for {inputs['for']} with {inputs['spicy']} spiciness, {inputs['prep_time']} preparation time, and {inputs['cook_time']} cooking time."
    return prompt

def main():
    st.title("Recipe Wizard")
    
    # Collecting user inputs
    user_inputs = get_user_input()

    if st.button("Generate Recipe"):
        # Configure API key for Google Generative AI
        #api_key = st.secrets["AIzaSyCT2qloRABQ1s-du8UnBZZo0uFbjfn9Kek"]
        api_key = "AIzaSyCT2qloRABQ1s-du8UnBZZo0uFbjfn9Kek"
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-pro')

        prompt = generate_prompt(user_inputs)
        response = model.generate_content(prompt)
        
        # Displaying the response
        if hasattr(response, 'text'):
            st.markdown(to_markdown(response.text))
        elif 'text' in response:
            st.markdown(to_markdown(response['text']))
        else:
            st.write("No text content found in the response.")

if __name__ == "__main__":
    main()

# import streamlit as st

def main():
    api_key = st.secrets["general"]["AIzaSyCT2qloRABQ1s-du8UnBZZo0uFbjfn9Kek"]
    st.write(f"API Key: {api_key}")


