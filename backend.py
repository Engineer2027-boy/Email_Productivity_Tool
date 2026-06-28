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

    user_email = """Greetings from TCS!!

We are pleased to share TCS Campus Commune Portal - a unified platform designed to bridge academia and industry, strengthen talent readiness, and support a skills-based hiring approach for the 2027 cohort and beyond. Through curated learning channels in emerging technologies and key business domains, the platform enables students to build relevant capabilities, gain industry insights, and confidently transition from campus to corporate environments.

This portal aims to provide students with timely updates and information related to campus hiring, understand expectations, and prepare effectively for interviews through guided resources.

We request you to socialize below message with students across batches and specializations to get them onboarded on the portal.

*****************************************************************************************

Dear Student, 

 

We are pleased to invite you to be part of the TCS Campus Commune. 

Campus Commune is a digital engagement platform from TCS designed to help you explore career guidance, hiring process, emerging technologies, learning opportunities, and unparallel industry insights. It will help you stay connected with larger TCS ecosystem and get a glimpse of ever evolving enterprise.

Through Campus Commune, you can: 

Join channels based on your interests and specializations.
Stay informed about expert talks, hiring updates.
Explore implementation of technologies across business domains.
Showcase academic accomplishments, explore internships
Stay connected with peers across top institutes
 

To get started, please complete your registration and the pilot activities listed below.

Step 1: Register on Campus Commune

Please visit the link below to register:
https://campuscommune.tcsapps.com/en-in/intro

Once you are on the page, follow these steps:

Click Register
Use your personal email ID
Verify your email ID
Complete the registration by following the on-screen instructions
Install Microsoft Authenticator or Google Authenticator
Link the authenticator app with your registered email ID
Log in using your registered credentials
 

Note: TCS Next Step credentials are not required for this registration.

 

Step 2: Further Activities

After logging in, you may explore the following:

Visit the Home Page
Complete your Campus Commune profile
Go to Explore Channels → India Channel
Explore other channels and subscribe to the ones that interest you
Subscribe to your regional channel"""
    print(email_content(user_email))



