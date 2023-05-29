from nltk.chat.util import Chat, reflections
  
pairs =[
    ['my name is (.*)', ['Hello ! % 1']],
    ['(hi|hello|hey|holla|hola)', ['Hey there !', 'Hi there !', 'Hey !']],
    ['(.*) your name ?', ['My name is Geeky']],
    ['(.*) do you do ?', ['We provide a platform for tech enthusiasts, a wide range of options !']],
    ['(.*) created you ?', ['Geeksforgeeks created me using python and NLTK']]
]
  
chat = Chat(pairs, reflections)
chat.converse()