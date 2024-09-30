from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import google.generativeai as genai
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import textwrap

# Set up the API key
genai.configure(api_key='AIzaSyDXx5mLODzmOqmE3ihDULRcy4QhNsGLIjY')

app_name = 'chatapp'
# Define the function to interact with the Google Generative AI API
def ask_gemini(userMessage):
    try:
        # Use the Gemini 1.5 Flash model to generate a response
        # response = genai.generate_text(
        #     model='models/text-bison-001',  # Updated to Gemini 1.5 Flash model
        #     prompt=userMessage,
        #     max_output_tokens=150,
        #     temperature=0.7,
        # )
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
            }
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config=generation_config,
            system_instruction="You are an AI chatbot assistant on a studies website for university student to do quiz and get study material, you will try to assist them on the work they are working on, try to supporting them as best as you can do. You can call your self AI assistant.\nThe website include many subject like math, coding from beginner to intermediate.",
        )
        chat_session = model.start_chat(
            history=[
            ]
        )
        response = chat_session.send_message(userMessage)
        # Extracted the generated text from the response
        if hasattr(response, 'text'):
            answer = response.text.strip()
            # Replace double quotes with single quotes
            answer = answer.replace('"',"'")
            answer = answer.replace('*', '')
            # Endure proper spacing with line breaks
            answer = textwrap.fill(answer, width= 70)
        else:
            answer = "no response generated."

        
        # Extract the generated text from the response
        answer = response.text.strip() if hasattr(response, 'text') else "No response generated."
        print(response)
    except Exception as e:
        print(e)
        answer = f"An error occurred: {e}"
    return answer

# Define the view to handle user messages and API responses
def getUserResponse(request):
    if request.method == 'POST':
        userMessage = request.POST.get('message')

        # Generate a response using the ask_gemini function
        response = ask_gemini(userMessage)
        # Return the user message and AI response as JSON
        return JsonResponse({'message': userMessage, 'response': response})
    
    # Render the HTML template if the request method is GET
    return render(request, 'chat.html')

# if not config.API_KEY:
#     raise ValueError("API key not found. Make sure to set the 'API_KEY' in config.py.")


def index(request):
    return render(request, 'chat.html')

def specific(request):
    return HttpResponse("list1")


# def getResponse(request):
#     userMessage = request.GET.get('userMessage')

#     return HttpResponse(userMessage)

# def chatbot(request):
#     if request.method == 'POST':
#         message = request.POST.get('message')
#         response = 'Hi there'
#         return JsonResponse({'message': message, 'response': response})
#     return render(request, 'index.html',)

# openai_api_key = 'API-KEY'
# openai.api_key = openai_api_key

# def ask_openai(userMessage):
#     response = openai.ChatCompletion.create(
#         model = "gpt-3.5-turbo",
#         prompt = userMessage,
#         max_tokens = 50,
#         n=1,
#         stop=None,
#         temperture=0.7,
#     )
    
#     answer = response.choices[0].text.strip()
#     return answer



# def ask_gemini(userMessage):
#     response = genai.GenerativeModel(
#         model="gemini-1.5-flash",  # Replace with the actual model identifier
#         prompt=userMessage,
#         max_tokens=150,
#         temperature=0.7,
#     )
    
#     answer = response['text'].strip()
#     return answer
    
# def getUserResponse(request):
#     if request.method == 'POST':
#         userMessage = request.POST.get('message')
#         response = 'Hi, How is your day '
#         return JsonResponse({'message': userMessage, 'response': response})
#     return render(request, 'index.html',)



# Define the generation configuration
# generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 64,
#     "max_output_tokens": 8192,
#     "response_mime_type": "text/plain",
# }

# # Initialize the model
# model = genai.GenerativeModel(
#     model_name="gemini-1.5-flash",
#     generation_config=generation_config,
# )

# # Define a function to ask the model a question and get the response
# def ask_gemini(userMessage):
#     response = model
#     return response.text

# def getUserResponse(request):
#     if request.method == 'POST':
#         userMessage = request.POST.get('message')
#         response = ask_gemini(userMessage)
#         return JsonResponse({'message': userMessage, 'response': response})
#     return render(request, 'index.html')
