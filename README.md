# Amazon-Lex-Chatbot-
Step 1: Create a custom lex bot
We’ll start off by creating a custom bot. The bot will be created in LEX bot by Amazon. In the options select custom bot, Choose the name of the bot “university chat bot”. Choose the output voice as you would preffer followed by a timeout of 3 minutes

Step 2: Building the language model
Here’s where we give our bot the ability to understand conversations. Some terms used here:
1.	Intent: Intent is a skill the bot has. Our bot has one skill for now : students querries
2.	Utterances: Sentences to invoke an intent. To find the correct answer for  intent. Utterances for the bot are 
Hello
                  What courses do you offer?
                  What is the academic fee?
               When is the intake?
3.	Slots: Values user must supply to an intent.
Slots are the inputs which the user needs to provide for fulfilling the intent. 
Here the slots are the answer  to hello which is hello
Another slot will have the courses offered
A slot for fee table per department
A slot for next intake

Prompts are the questions which are asked to get input from the user. They are used to request values for slots from the user
The prompts will be:
 would you like to know the courses offered
Would you like to check the fees structure
Check next intake

Test the bot
Input lambda fie attached and select run with python 3.6

