from google import genai

#Place API key here
GEMINI_API_KEY = ''
client = genai.Client(api_key=GEMINI_API_KEY)

'''
response = client.models.generate_content(
    model="gemini-3-flash-preview",
    contents="How does AI work?"
)
print(response.text)
'''

def grade_article_individual(title):
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents= f"""
                    Based on the following news article title, generate me a grade ranging from 1 through 5 based on the relevance of this topic to the greater financial market
                    
                    Important parameters: 
                    -DO NOT include any notes about the topic in your response, only the grade in a single digit number  
                    -Base your grades SOLELY on how this news would effect stocks, bonds, and other assets, not based on political climates 
                    -Make sure to utilize the fact there are 5 possible grades(1, 2, 3, 4, or 5)

                    "{title}"
                   """
        )

    return(response.text)

