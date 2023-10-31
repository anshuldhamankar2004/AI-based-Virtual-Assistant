import speech_recognition as sr
import win32com.client
import os
import webbrowser
import openai
import datetime
import random
import ctypes
import wikipedia as wiki
import time
import pyautogui
import pywhatkit
import requests
import wolframalpha
import pyfiglet
import array
from colorama import init, Fore
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart



import turtle

# colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
# import turtle
# t = turtle.Pen()
# turtle.bgcolor('black')
# for x in range(360):
#     t.pencolor(colors[x%6])
#     t.width(x/100 + 1)
#     t.forward(x)
#     t.left(59)
# turtle.exitonclick()


speaker = win32com.client.Dispatch("SAPI.SpVoice")


def askname():
    init(autoreset=True)
    figlet_text = pyfiglet.figlet_format("E  C  H  O", font="slant")
    colored_text = Fore.BLUE + figlet_text
    print(colored_text,"version:1.0")
    s = "Hi, im Echo, your personal A I"
    print(s)

    speaker.Speak(s)
    # r = sr.Recognizer()
    # print("listening....")
    #
    # with sr.Microphone() as source:
    #     r.pause_threshold = 0.7
    #     audio1 = r.listen(source)
    #
    #     try:
    #         # name=r.recognize_google(audio1, language="en-in")
    #         name = input()
    #         name = str(name)
    #
    #         return str(name)
    #     except Exception as ne:
    #         print("Can you please repeat that?")
    #         speaker.speak("Can you please repeat that?")
    #         name = ""
    #         return name


name = askname()
#named = (f"hi,{name} how can i help you?")
named = (f" how can i help you?")
print(f"how can i help you?")
#print(f"hi,{name} how can i help you?")
speaker.speak(named)

def pass_generator():
    MAX_LEN = 12
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                         'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                         'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                         'z']

    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                         'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q',
                         'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                         'Z']

    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
               '*', '(', ')', '<']

    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    for x in range(MAX_LEN - 4):
        temp_pass = temp_pass + random.choice(COMBINED_LIST)

        temp_pass_list = array.array('u', temp_pass)
        random.shuffle(temp_pass_list)

    password = ""
    for x in temp_pass_list:
        password = password + x

    print(password)

def ai(prompt):
    openai.api_key = "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"
    text = f"Open AI response from{prompt}\nn ***********************\\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=4000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("OpenAI"):
        os.mkdir("OpenAI")

    with open(f"OpenAI/prompt- {random.randint(1, 50)}", "w") as f:
        f.write(text)

#random.randint(1, 2363333333)}
def imagen(prompt):
    openai.api_key = "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"
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    return image_url
app_id="LUY8P4-LPGQRX5GVK"
def computational_intelligence(question):
    try:
        client = wolframalpha.Client(app_id)
        answer = client.query(question)

        answer = next(answer.results).text
        print(answer)
        return answer
    except:
        speaker.speak("Sorry sir I couldn't fetch your question's answer. Please try again ")
        functioning()

def fetch_news(api_key="40b18b18746d4cce8688abe08f9ec91c", country_code='in'):
    NEWS_API_URL = 'https://newsapi.org/v2/top-headlines'

    params = {
        'apiKey': api_key,
        'country': country_code,
    }

    response = requests.get(NEWS_API_URL, params=params)

    if response.status_code == 200:
        news_data = response.json()
        articles = news_data['articles']
        for index, article in enumerate(articles, start=1):
            print(f"{index}. {article['title']}")
            print(f"   {article['description']}")
            print(f"   Read more: {article['url']}")
            print()
    else:
        print('Error fetching news:', response.status_code)

def takeuserinput():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.7
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            #query=input()
            query = str(query)
            print("User said:" + query)
            return str(query)
        except Exception as e:
            speaker.speak("Could not hear you. Please speak again.")
            print("Could not hear you. Please speak again.")
            functioning()


def functioning():
    while True:
        print("Listening.....")
        query = takeuserinput()
        query = str(query)
        if not query:
            speaker.speak("Could not hear you. Please speak again.")
            continue

        greetings = [
            "hi",
            "hello",
            "hi there",
            "hey",
            "greetings",
            "salutations",
            "howdy",
            "welcome",
            "hi how are you",
            "hey what's up",
            "hola",
            "bonjour",
            "ciao",
            "namaste",
            "konnichiwa",
            "guten tag",
            "sawasdee"
        ]

        humorous_responses = [
            "Hmm, that's an interesting one! Unfortunately, it's beyond my capabilities right now.",
            "I'm like a magician, but even I can't decode that command. Maybe try something else?",
            "You've stumped me with this one! Can you ask another question?",
            "Oops! Looks like I missed that lesson in virtual assistant school. What else can I do for you?",
            "Well, this is awkward. My virtual brain seems to be on vacation. Please try another command!",
            "Oh dear, that went over my head. Let's try a different approach, shall we?",
            "I'm afraid this is where my knowledge hits a roadblock. How about something else?",
            "Hmmm, I'm trying to be smart, but this one has me stumped. Any other requests?",
            "I'm a fast learner, but this command is next-level. Give me a simpler task, please!",
            "You found a hidden easter egg! But I'm not sure what it does. Can you try a valid command?",
        ]

        sites = [
            ["google", "https://www.google.co.in"],
            ["youtube", "https://www.youtube.com"],
            ["facebook", "https://www.facebook.com"],
            ["amazon", "https://www.amazon.in"],
            ["flipkart", "https://www.flipkart.com"],
            ["indiatimes", "https://www.indiatimes.com"],
            ["paytm", "https://www.paytm.com"],
            ["snapdeal", "https://www.snapdeal.com"],
            ["bookmyshow", "https://www.bookmyshow.com"],
            ["irctc", "https://www.irctc.co.in"],
            ["licindia", "https://www.licindia.in"],
            ["hdfcbank", "https://www.hdfcbank.com"],
            ["statebankofindia", "https://www.sbi.co.in"],
            ["ndtv", "https://www.ndtv.com"],
            ["aajtak", "https://www.aajtak.intoday.in"],
            ["moneycontrol", "https://www.moneycontrol.com"],
            ["icicibank", "https://www.icicibank.com"],
            ["cricbuzz", "https://www.cricbuzz.com"],
            ["incometaxindiaefiling", "https://www.incometaxindiaefiling.gov.in"],
            ["indianexpress", "https://www.indianexpress.com"],
            ["linkedin", "https://www.linkedin.com"],
            ["oyo", "https://www.oyorooms.com"],
            ["zomato", "https://www.zomato.com"],
            ["olx", "https://www.olx.in"],
            ["makemytrip", "https://www.makemytrip.com"],
            ["magicbricks", "https://www.magicbricks.com"],
            ["justdial", "https://www.justdial.com"],
            ["jio", "https://www.jio.com"],
            ["cricinfo", "https://www.espncricinfo.com"],
            ["rediff", "https://www.rediff.com"],
            ["timesofindia", "https://www.timesofindia.indiatimes.com"],
            ["yahoo", "https://www.yahoo.co.in"],
            ["bhaskar", "https://www.bhaskar.com"],
            ["indiamart", "https://www.indiamart.com"],
            ["shopclues", "https://www.shopclues.com"],
            ["bigbasket", "https://www.bigbasket.com"],
            ["quikr", "https://www.quikr.com"],
            ["hindustantimes", "https://www.hindustantimes.com"],
            ["jabong", "https://www.jabong.com"],
            ["myntra", "https://www.myntra.com"],
            ["ebay", "https://www.ebay.in"],
            ["indianrail", "https://www.indianrail.gov.in"],
            ["zee5", "https://www.zee5.com"],
            ["olacabs", "https://www.olacabs.com"],
            ["indianexpress", "https://www.indianexpress.com"],
            ["swiggy", "https://www.swiggy.com"],
            ["netflix", "https://www.netflix.com"],
            ["hotstar", "https://www.hotstar.com"],
            ["abplive", "https://www.abplive.com"],
            ["airtel", "https://www.airtel.in"],
            ["spotify", "https://open. .com"]
        ]

        functionality_titles = [
            "Operating System and Web-related Tasks",
            "Opening Websites",
            "Opening the Photo Gallery",
            "Opening the Games Folder",
            "AI-based Responses",
            "Generating Images",
            "Computational Intelligence",
            "Time",
            "Mathematical Calculations",
            "Web Search and Information Retrieval",
            "Searching on Google",
            "Searching on Wikipedia",
            "Searching on Spotify",
            "Sending WhatsApp Messages",
            "System Shutdown",
            "Aborting System Shutdown",
            "Weather Information",
            "Password Generation",
        ]

        compliments = [
            "great job",
            "well done",
            "you nailed it",
            "impressive",
            "fantastic",
            "nice work",
            "bravo",
            "excellent",
            "you're awesome",
            "outstanding",
            "you rock",
            "good going",
            "keep it up",
            "you're the best",
            "kudos",
            "thumbs up",
            "superb",
            "you're amazing",
            "terrific",
            "spot on"
        ]

        responses = [
            "Thank you!",
            "I appreciate that!",
            "Glad to hear that!",
            "I'm here to help!",
            "You're too kind!",
            "I'm always at your service!",
            "Thanks a bunch!",
            "It's a pleasure assisting you!",
            "You make my day!",
            "I'm delighted to be of assistance!",
            "You're making me blush (if I could)!",
            "Your feedback is motivating!",
            "I'm just doing my job!",
            "You're awesome too!",
            "I'm here to make things easier for you!",
            "Thanks for the encouragement!",
            "I'll keep up the good work!",
            "I aim to please!",
            "Your words mean a lot!",
            "I'm here to make your life better!"
        ]

        abusive_words=["fuck","shit","bitch","motherfucker","ass"]



        for site in sites:
            if f"open {site[0]} website".lower() in query.lower():
                query = query.lower().replace("Echo ", "").replace("echo ", "")
                speaker.Speak(f"opening{site[0]} for you!")
                webbrowser.open(site[1])



        if "the time" in query:
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            strfTime = datetime.datetime.now().strftime("%H hours ,%M minutes ,%S seconds")
            print(strfTime)
            speaker.Speak(f"The time is{strfTime}")

        query_words = query.lower().split()
        abusive_used = any(word in abusive_words for word in query_words)

        if abusive_used:
            speaker.speak("Please use appropriate language.")
            continue


        elif any(query.lower().startswith(greeting) for greeting in greetings):

            speaker.speak(random.choice(greetings))

            continue

        elif "what can you do for me".lower() in query.lower():
            speaker.speak("I can do many tasks for you quiet efficiently, here's a list ")
            for _ in functionality_titles:
                print(_)

        elif "open photo gallery" in query:
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.Speak("opening gallery")
            os.system(r"start C:\Users\ASUS\Pictures")

        elif "open games" in query:
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.Speak("opening games folder")
            os.system(r"start D:\GAMES")

        elif "exit" in query:
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("thank you.Bye")
            exit()

        elif "Using artificial intelligence".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            print("Hold on a sec, Im on it")
            speaker.speak("Hold on a sec, Im on it")
            ai(prompt=query)

        elif f"search on google".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            query = query.lower()
            query = query.replace("search on google", "")
            speaker.speak(f"Searching {query}on google")
            pywhatkit.search(query)

        elif f"search on wiki".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            query = query.lower()
            query = query.replace("search ", "")
            query = query.replace(" on wiki ", "")
            speaker.speak(f"Enlightening you,,,,,hold on")
            try:
                info = wiki.summary(query)
                print(info)
                ctypes.windll.user32.MessageBoxW(
                    0, info[:4000000], query, 0
                )
                speaker.speak(info)
            except Exception as a:
                speaker.speak("please specify")
                print("please specify")


        elif "on spotify".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            query = query.lower()
            query = query.replace("play ", "")
            query = query.replace(" on spotify", "")
            webbrowser.open(f"https://open.spotify.com/search/{query}")
            time.sleep(13)
            pyautogui.click(x=1055, y=417)
            speaker.speak(f"Playing {query}")
            exit()

        elif "using image generator".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            query = query.lower()
            query = query.replace(" using image generator generate", "")
            speaker.speak("sure,I can do that")
            speaker.speak("please follow the link below to see the generated image")

            image_url = imagen(prompt=query)
            print(image_url)

        elif "on youtube".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            query = query.lower()
            query = query.replace("play ", "")
            query = query.replace(" on youtube", "")
            speaker.speak(f"playing{query} on youtube")
            pywhatkit.playonyt(query)

        elif "get me info about".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            query = query.replace("get me info about ", "")
            inf = ""
            pywhatkit.info(query, 20, inf)
            print(inf)

        elif "send a whatsapp message".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("enter receivers number")
            ph_number = (input())
            speaker.speak("enter the message you want to send")
            message = input()
            speaker.speak("Sending Your message, please hold on")
            pywhatkit.sendwhatmsg_instantly(ph_number, message, 10, False)
            time.sleep(10)
            speaker.speak("message sent successfully")


        elif "shutdown the system".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Shutting down the system")
            pywhatkit.shutdown(20)
            speaker.speak("Shutting down the system in 20 seconds, command me if u want to abort")

        elif "abort".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Aborting")
            pywhatkit.cancel_shutdown()
            speaker.speak("Abort successful")


        elif "calculate".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            answer=computational_intelligence(query)
            speaker.speak("Hold on a sec")
            speaker.speak(answer)


        elif "when".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Hold on a sec")
            print("when")
            answer=computational_intelligence(query)
            speaker.speak(answer)


        elif "why".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Hold on a sec")
            print("why")
            answer=computational_intelligence(query)
            speaker.speak(answer)

        elif "which".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Hold on a sec")
            answer=computational_intelligence(query)
            speaker.speak(answer)

        elif "how".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Hold on a sec")
            answer=computational_intelligence(query)
            speaker.speak(answer)

        elif "what".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Hold on a sec")
            answer=computational_intelligence(query)
            speaker.speak(answer)

        elif "who".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")

            speaker.speak("Hold on a sec")
            answer=computational_intelligence(query)
            speaker.speak(answer)

        elif "where".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            speaker.speak("Hold on a sec")
            answer=computational_intelligence(query)
            speaker.speak(answer)

        elif "weather in".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")

            api_key = '30d4741c779ba94c470ca1f63045390a'

            user_input = query.replace("weather in ","")

            weather_data = requests.get(
                f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

            if weather_data.json()['cod'] == '404':
                print("No City Found")
            else:
                weather = weather_data.json()['weather'][0]['main']
                temp = round(weather_data.json()['main']['temp'])
                tempc = (temp - 32) * 5 / 9
                print(f"The weather in {user_input} is: {weather}")
                print(f"The temperature in {user_input} is: {round(tempc,2)}ºC")


                speaker.speak(f"The weather in {user_input} is: {weather}")
                speaker.speak(f"The temperature in {user_input} is: {round(tempc,2)}ºCelcius")

        elif "generate a password".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            PASSWORD=pass_generator()
            speaker.speak("Here's the password , I'll keep it a secret, I promise!!!")
            print(PASSWORD)

        elif "tell me a joke" in query:
            query = query.lower().replace("echo ", "")
            speaker.Speak("Sure! Which language do you prefer? English or Hindi?")
            language = takeuserinput()

            if language.lower() == "english":
                jokes = [
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
                    "Why don't scientists trust atoms? Because they make up everything!",
                    "Why don't skeletons fight each other? They don't have the guts!",
                    "Why don't oysters donate to charity? Because they are shellfish!",
                    "What did one wall say to the other wall? I'll meet you at the corner!",
                    "Why don't eggs tell jokes? Because they might crack up!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                    "What do you call fake spaghetti? An impasta!",
                    "Why did the tomato turn red? Because it saw the salad dressing!",
                    "How do you organize a space party? You planet!",
                    "What did one traffic light say to the other? Stop looking! I'm changing!",
                    "What do you call a bear with no teeth? A gummy bear!",
                    "Why did the bicycle fall over? It was two-tired!",
                    "How do you make a tissue dance? You put a little boogie in it!",
                    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
                    "Why don't melons get married? Because they cantaloupe!",
                    "Why did the stadium get hot after the game? All of the fans left!",
                    "Why did the math book look sad? Because it had too many problems!",
                    "What did one hat say to the other hat? You stay here, I'll go on ahead!",
                    "Why did the chicken go to the seance? To talk to the other side!",
                    "Why don't you ever see elephants hiding in trees? Because they're so good at it!",
                    "Why don't skeletons fight each other? They don't have the guts!",
                    "Why did the bicycle fall over? It was two-tired!",
                    "How do you make a tissue dance? You put a little boogie in it!",
                    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
                    "Why don't melons get married? Because they cantaloupe!",
                    "Why did the stadium get hot after the game? All of the fans left!",
                    "Why did the math book look sad? Because it had too many problems!",
                    "What did one hat say to the other hat? You stay here, I'll go on ahead!",
                    "Why did the chicken go to the seance? To talk to the other side!",
                    "Why don't you ever see elephants hiding in trees? Because they're so good at it!",
                    "Why did the scarecrow win an award? Because he was outstanding in his field!",
                    "What did one wall say to the other wall? I'll meet you at the corner!",
                    "What do you call fake spaghetti? An impasta!",
                ]
                joke = random.choice(jokes)
                print(joke)
                speaker.Speak(joke)
            elif language.lower() == "hindi":
                jokes = [
                    "एक आदमी दूसरे आदमी से: तेरी बीवी मेरे लिए बहुत खतरनाक साबित हुई है, पिछले साल तो इंसानों की संख्या 2 से घट गई।",
                    "एक बच्चा: तू कहां रहता है? दूसरा बच्चा: पीछे मोदी जी के बगीचे में. बच्चा: वाह! वहां पर कैसी सुरक्षा होती है? दूसरा बच्चा: अरे नहीं यार, वहीं तो बगीचे की खुरपीयां और पौधे होते हैं।",
                ]
                joke = random.choice(jokes)
                print(joke)
                speaker.Speak(joke)
            else:
                speaker.Speak("I'm sorry, I don't have jokes in that language.")

        elif "tell me about yourself".lower() in query.lower():
            query = query.lower().replace("Echo ", "").replace("echo ", "")
            print and speaker.speak(
                "My Name Is Echo.  "
                "Version-0.1.   "
                "Created by Mr. ANSHUL"
            )
            print(
                "I am your virtual assistant created using Python. I am designed to perform various tasks such as speech recognition, web browsing, opening applications, answering questions, and more.")
            print(
                "My purpose is to assist you and make your tasks easier. I can provide information from Wikipedia, search the web, play music, set reminders, and even solve math problems using Wolfram Alpha.")
            print("Feel free to ask me anything or give me commands, and I'll do my best to help you!")


        elif query.lower() in compliments:
            response = random.choice(responses)
            print(response)
            speaker.Speak(response)


        elif "tell news".lower() in query.lower():

            country_code = "in"
            speaker.speak("Fetching news")
            fetch_news(api_key="YOUR_API_KEY", country_code=country_code)



        else:
            rand_reply=random.choice(humorous_responses)
            print(rand_reply)
            speaker.speak(
            rand_reply
            )

functioning()