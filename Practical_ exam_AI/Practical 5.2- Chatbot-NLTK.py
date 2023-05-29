#Bakery Chatbot
from nltk.chat.util import Chat, reflections

pairs =[
	['my name is (.*)', ['Hello ']],
	['(hi|hello|hey|hola|ni hao|konichiwa)', ['Hey there! Welcome to Foodies Bakery! How can I help you?']],
	['(.*) your name', ['My name is Washington!']],
	['(.*)do you do', ['I help to clear doubts with respect to the restaurant & your service.']],
	['(.*)dishes(.*)|(.*)menu(.*)', ['We offer sandwiches, cupcakes, rolls, tea, hot cocoa, noodles.']],
	['(.*)types of noodles', ['We have vegetarian and chicken noodles.']],
	['(.*)types of sandwiches', ['We have chutney and mayo sandwiches.']],
	['(.*)types of rolls', ['We have vegetarian and tandoori rolls.']],
	['(.*)types of tea', ['We have black, green, white and brick tea.']],
	['(.*)types of cupcakes', ['We have chocolate chip, strawberry and caramel cupcakes.']],
	['(.*)timings(.*)|(.*)time for ordering', ['We deliver from 8AM to 10PM on all days!']],
	['(.*)discount(.*)', ['You can use this code for a 10 percent off!: GGHD']],
	['(.*)bye|exit', ['Bye!']]
]


print("Hello. Welcome to Foodies Bakery! How can I help you? [Note: Please use lowercase letters to converse.]")
chat = Chat(pairs, reflections)
chat.converse()

