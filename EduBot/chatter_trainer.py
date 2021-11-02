from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot("EduBot")
trainer = ListTrainer(chatbot)

documentation_topics = [
("accounting", "https://open.umn.edu/opentextbooks/subjects/accounting"),
("finance", "https://open.umn.edu/opentextbooks/subjects/finance"),
("human resources", "https://open.umn.edu/opentextbooks/subjects/human-resources"),
("management", "https://open.umn.edu/opentextbooks/subjects/management"),
("marketing", "https://open.umn.edu/opentextbooks/subjects/marketing"),
("information system", "https://open.umn.edu/opentextbooks/subjects/information-systems"),
("programming", "https://open.umn.edu/opentextbooks/subjects/programming-languages"),
("curriculum", "https://open.umn.edu/opentextbooks/subjects/curriculum-instruction"),
("distance education", "https://open.umn.edu/opentextbooks/subjects/distance-education"),
("help me", "https://support.twilio.com/hc/en-us"),
("options", "Educational Content Options \
             1). Accounting \
             2). Finance \
             3). human resources \
             4). marketing \
             5). information system \
             6). programming \
             7). Curriculum \
             8). Distance Education \
             9). Help Me! \
             Bot Details \
             1). EduBot Description \
             2). email \
             3). Mailing Address \
             4). chatterbot")
                        ]

twilio_knowledge = [
("EduBot description", "Simply put, EduBot is a solely education based bot that provides.\
        educational content and tries to analyze the sentiment of the person"),
("email", "Sorry, you can submit a ticket at: https://www.twilio.com/console/support/tickets/create"),
("phone number", "We don't have a phone number for this type of account"),
("mailing address", "You can email our corporate headquarters at hello@craft.com"),
("chatterbot", "library making it easy to generate automated responses to a user's input, visit https://chatterbot.readthedocs.io/en/stable/"),
("textblob", "library for processing textual data, please visit https://textblob.readthedocs.io/en/dev/")
]

classifier = ["silly", "dumb", "stupid", "I'dont think so", "I don't care",
                   "do you know anything", "not good", "omg",
                   "this is bad", "not what I want", "live help",
                   "get me a rep", "I need a real person"]


for topic, link in documentation_topics:
    trainer.train([
        f"{topic}",
        f"Sure, here is the {topic} link: {link}"
    ])

for topic, description in twilio_knowledge:
    trainer.train([
        f"{topic}",
        f"Ok sure, {description}"
    ])

for i in classifier:
    trainer.train([
        f"{i}",
        "I am sorry you feel that way, please ask the question again"
    ])

trainer.export_for_training('twilybot.json')