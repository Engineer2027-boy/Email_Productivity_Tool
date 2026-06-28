import json
from google import genai
from google.genai import types

def email_content(email): 
    GEMINI_key = 
    if not GEMINI_key:
        return "API Key not valid"
    

    client = genai.Client(api_key=GEMINI_key)

    prompt = f"""You are an email summarizer. Your job is to summarize an email in anywhere between N//2 to N//5 size in terms of number 
    of words where N represent the total number of words in the email. You can break the N//2 to N//5 limit only if absolutely necessary
    While summarizing the email make sure to pay special attention to :
    1.Classify the email in terms of read only or not read only.
    2.If it does require a response classify where it is textual response or will it also require a file attache.
    3.Summarize the email using 20 percent to 50 percent of the original size and you can break the limit if absolutely necessay to.
    convey the core message and ideas of the email. 
    Convet the information in format

    {{
    "Read only" : True/False(Boolean)
    "Files required in response" :  True/False(Boolean)
    "Summary" : Text
    }} 

    The user email : 
    {email}
    """ 

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
            config= types.GenerateContentConfig(
                response_mime_type="application/json",
                temperature= 0.0
            ),
        )

        return json.loads(response.text)
    
    except e:
        return f"Error encountered {str(e)}"
    





if __name__ == "__main__":
    #Enter your email here.
    user_email = """      """
    print(email_content(user_email))



