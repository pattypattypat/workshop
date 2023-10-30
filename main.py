import streamlit as st
import os
import main_code as mc
from streamlit_antd_components import menu, MenuItem, divider


def workshop_sidebar():  
	with st.sidebar: #options for sidebar
		opt = menu([
				MenuItem('Workshop Prep', icon='file-slides', href='https://docs.google.com/document/d/1MHjWBYAahb7KyKO-dXEDnaBF3og7ZA5V/edit?usp=sharing&ouid=104232750497195021523&rtpof=true&sd=true'),
				MenuItem('Workshop Deck', icon='file-slides', href='https://docs.google.com/presentation/d/1yByNzFHWxxmSaudttcrf2Mo0ATx5UpCr/edit?usp=sharing&ouid=104232750497195021523&rtpof=true&sd=true'),
				MenuItem('Code Template', icon=''),
				MenuItem('Intro to Streamlit', icon='', children=[
					MenuItem("Exercise 1", icon='journal-code'),
					MenuItem("Exercise 2", icon='journal-code'),
					MenuItem("Exercise 3", icon='journal-code'),
					MenuItem("Exercise 4", icon='journal-code'),
					MenuItem("Exercise 5", icon='journal-code'),
				]),
				MenuItem('Rule-based chatbot', icon='', children=[
					MenuItem("Exercise 6", icon='journal-code'),
				]), 
				MenuItem('Prompt Template', icon='', children=[
					MenuItem("Exercise 7", icon='journal-code'),
				]), 
				MenuItem('Integrate OpenAI API', icon='', children=[
					MenuItem("Secrets", icon='journal-code'),        
					MenuItem("Exercise 8", icon='journal-code'),
					MenuItem("Exercise 9", icon='journal-code'),
				]),
			MenuItem('Chat with Memory', icon='', children=[
					MenuItem("Exercise 10", icon='journal-code'),
				]), 
			MenuItem('Vector Store and RAG', icon='', children=[
					MenuItem('Sample Files', icon='cloud-download', href='https://github.com/peachredfu/workshop/tree/main/UPLOADED'),
					MenuItem("Exercise 11&12", icon='journal-code'),
				]), 
			MenuItem('Integrate Google LLM API', icon='', children=[
					MenuItem("Exercise 13", icon='journal-code'),
					MenuItem("Exercise 14", icon='journal-code'),
					MenuItem("Exercise 15", icon='journal-code'),
				]), 
			# MenuItem('Smart Agent', icon='', children=[
			# 		MenuItem("Exercise 16", icon='journal-code'),
			# 	]),
			# MenuItem('Document Search', icon='', children=[
			# 		MenuItem("Exercise 17", icon='journal-code'),
			# 	]),
			MenuItem(type='divider',dashed=True),],open_all=True, index=2)

		clear_session = st.button("**Clear Chat Memory**")
		if clear_session: 
			st.session_state.memory.clear()
			st.session_state.msg.clear()
			st.success("you chat memory is cleared")

	if opt == 'Code Template': workshop_code_template()
	elif opt == 'Exercise 1': ex1()
	elif opt == 'Exercise 2': ex2()
	elif opt == 'Exercise 3': ex3()
	elif opt == 'Exercise 4': ex4()
	elif opt == 'Exercise 5': ex5()
	elif opt == 'Exercise 6': ex6()
	elif opt == 'Exercise 7': ex7()
		# with st.expander("Reveal Code"): st.code(mc.code_ex7, language='python')
		# prompt_inputs_form()
	elif opt == 'Secrets': secrets()  
	elif opt == 'Exercise 8': ex8()
	elif opt == 'Exercise 9': ex9()
	elif opt == 'Exercise 10': ex10()
	elif opt == 'Exercise 11&12': ex11_and_ex12()
	elif opt == 'Exercise 13': ex13()
	elif opt == 'Exercise 14': ex14()
	elif opt == 'Exercise 15': ex15()
	# elif opt == 'Exercise 16': ex16()
	else: workshop_code_template()

#to display after reveal code for each exercise
def after_reveal_code(codeoutput):
	st.write("Remember to save your file (press ctrl+s) and refresh your browser after pasting the code.")
	st.write(" ") 
	if codeoutput: st.markdown(":orange[Code Output]") 
 

# workshop template for main.py
def workshop_code_template():
	st.subheader("Workshop Template")

	with st.expander("", expanded=True): 
		st.code(mc.code_template, language='python')

# Exercise 1 : Hello World and Input
def ex1():
	st.subheader("Exercise 1: Functions")
	st.write("The code for Hello World is inside what you call a Python function.") #new
	st.write("The **def main()** function and **if__name__=='__main__'** statement are coding conventions for any Python programme. \n") #new  
	with st.expander("Reveal Code"):	
		st.code(mc.code_ex1, language='python')
	st.write("After pasting the code above, did you correctly include your **ex1()** inside **main()**?") #new  
	st.write("As this is your first exericse, don't forget to **run** the app by typing the following into the **terminal**") #new
	st.code('''streamlit run main.py''', language='python') #new
 
	st.write(" ") 
	st.write("You should see the following behaviour in your browser window:")
	st.markdown(":orange[Code Output]") #new
 
	st.subheader("**Hello World**", divider='rainbow')
	name = st.text_input("Enter your name")
	# only prints the Hello {name} if input box is not empty
	if name:
		st.write("Hello " + name)


# Exercise 2: radio button
def ex2():
	st.subheader("Exercise 2: Radio Button") #new
	st.write("You can add radio button by using **st.radio()**. It returns a :green[**string value**] of the selected option or :green[**None**] if no option is selected.") #new 
	st.write("For this exercise, we will do a simple *horizontal (default is vertical)* radio button widget that has :rainbow[rainbow coloured] and **bolded** options with :grey[caption] under each options.")
	st.write("**st.radio**( <*explanatory short label*>, <*options*>, caption=<*caption to show under each option*>, horizontal=<*true/false*> )")

	with st.expander("Reveal Code"): st.code(mc.code_ex2, language='python')
 
	after_reveal_code(True)
	st.subheader("Streamlit Radio Button", divider='rainbow')
	llm = st.radio(
		"Your preferred LLM",
		[":rainbow[GPT3.5]", "**PALM**"],
		captions = ["OpenAI", "Google"], horizontal=True)

	if llm == ':rainbow[GPT3.5]':
		st.write('You selected GPT3.5')
	elif llm == '**PALM**':
		st.write('You selected PALM')
	else:
		st.write("You didn\'t select LLM.")


# Exercise 3: sidebar
def ex3():
	st.subheader("Exercise 3: Navigational Sidebar")
	st.write("Let's add interativity to the app by organizing the different exercises into a sidebar using **st.sidebar()**. It returns a :green[**string value**] of the selected option or :green[**None**] if no option is selected.")
	st.write("For this exercise, we will do a radio button sidebar and also a button to clear the session chat history which will be used in upcoming exercises.")
	st.write("**st.sidebar.radio**( <*explanatory short label*>, <*elements or options*>, caption=<*caption to show under each option*>)")

	with st.expander("Reveal Code"): 
		st.code(mc.code_ex3, language='python')
	after_reveal_code(False)
	st.write(
    """
    **[Things to note]** 
    - The exercises data list (e.g. :green[**Exercise 1**], :green[**Exercise 11&12**]) names must match with the if-else conditional statement (e.g. :green[if opt=='**Exercise 1**'])")
    - Please using :green[**Ctrl**] + :green[**/**] to comment off the unavailable exercises' functions in :green[**elif**] statements to avoid error
	"""
	)
 

# Exercise 4: chat elements
def ex4():
	st.subheader("Exercise 4: Chat Elements")  
	st.markdown(
	"""
	Let's try out the available chat elements and build a conversation window using:
	- **st.chat_message()**: a container that lets you insert any Streamlit elements including charts, tables, text and more from the user or assitant. 
	- **st.chat_input()**: lets you display a chat input that the user has entered. It returns a :green[**string value**] of the user's input or :green[**None**] if the user hasn't sent a message yet.
	""" 
	)
	st.write("For this exercise, we will be displaying chat messages by different authors with customized avatar shown next to the message.")
	st.write("**st.chat_message**( < *'user'/'assistant'/'custom author name'*>, avatar=<*emoji or image only for user/assistant*>)")
	st.write("**st.chat_input**( < *placeholder text shown when chat input textbox is empty*>)")
  
	with st.expander("Reveal Code"): st.code(mc.code_ex4, language='python')
	after_reveal_code(True)
 
	st.subheader("Streamlit Chat Elements", divider='rainbow')
	msg_container = st.container()
	with msg_container:
		user_message = st.chat_message("user")
		user_message.write("I'm user")

		asst_message = st.chat_message("assistant")
		asst_message.write("I'm your assistant")

		other_message = st.chat_message("whoami")
		other_message.write("I'm nobody")

		st.chat_message("user", avatar="👩‍🎤").write("I'm user")

		st.chat_message('PA assistant', avatar='./avatar.png').write("Hi, I'm PA assistant")
  
		st.chat_message('assistant', avatar='https://raw.githubusercontent.com/dataprofessor/streamlit-chat-avatar/master/bot-icon.png').write('Hello world!')
  
		prompt = st.chat_input("Say something")
		if prompt:
			st.chat_message("user").write(f"**You entered**:  {prompt}")


# Exercise 5: upload files to working directory
# Create a folder for uploaded files, create only when it doesn't exist
UPLOAD_DIRECTORY = os.path.join(os.getcwd(), "UPLOADED")
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)
# Define allowed file extensions and maximum file size
allowed_extensions = [".docx", ".txt", ".pdf"]
max_file_size = 10 * 1024 * 1024  # 10MB

def display_uploaded_files():
	filelist=[]
	for root, dirs, files in os.walk(UPLOAD_DIRECTORY):
		for file in files:
			#filename=os.path.join(root, file)
			filelist.append(file)
	st.write(f"#### You have the following files uploaded")
	st.write({UPLOAD_DIRECTORY})
	st.write(filelist)

# Function to check if the file is valid
def is_valid_file(file):
	if file is None:
		return False
	file_extension = os.path.splitext(file.name)[-1]
	file_size = len(file.getvalue())
	return file_extension in allowed_extensions and file_size <= max_file_size

# uploading component
def ex5():
	st.subheader("Exercise 5: Upload File")    
	st.markdown(
	"""
	Let's try uploading file to your working directory using **st.file_uploader()**. For this exercise, we will create a file uploader that will:
	- accept only **.docx**, **.txt** and **.pdf** extension 
	- accept only **1 file** at a time (default)
	- check max file size limit of **10MB** (default is 200MB)
	- upload file to working directory folder, **UPLOADED**
	""" 
	)
 
	st.write("**st.file_uploader**( <*explantory label*>, type=<*array of allowed extensions*>)")
  
	with st.expander("Reveal Code"): st.code(mc.code_ex5, language='python')
	after_reveal_code(True)
 
	# File upload section
	uploaded_file = st.file_uploader("Upload a file", type=allowed_extensions)

	if uploaded_file is not None:
		if is_valid_file(uploaded_file):
			# Save the uploaded file to the upload folder
			file_path = os.path.join(f"{UPLOAD_DIRECTORY}", uploaded_file.name)
			with open(file_path, "wb") as f:
				f.write(uploaded_file.getvalue())
			st.success(f"File '{uploaded_file.name}' uploaded successfully.")
		else:
			st.error("Invalid file. Please upload a .docx, .txt, or .pdf file with a size of up to 10MB.")
	display_uploaded_files()


#Exercise 6 : Session State, Rule-based Echo Chatbot 
def ex6():
	st.subheader("Exercise 6: Rule-based Echo Chatbot, Session State")
	st.write("You can finally start building a simple rule-based echo chatbot using chat elements mastered from Exercise 4 and store the messages using **st.session_state**!")
	st.write("**st.session_state** holds information of the defined variables for a specific user during their entire session (re-runs and across multipage app) on a website or application. E.g. online purchase shopping cart")

	st.markdown(
	"""
	For this exercise, we will:
	- display chat input that user has entered and based on the input, reply with a pre-set message or echo the input using **if-else conditional statement**.
	- store and display chat messages from history (on app rerun) using **st.session_state** 
	""" 
	)
 
	with st.expander("Reveal Code"): st.code(mc.code_ex6, language='python')
	after_reveal_code(True)

	st.subheader("Rule-based Echo Bot", divider='rainbow')	
	st.caption("Try entering the rule-based response keyword: '*Hello*' and '*What is up?*'. (Enter the keyword in UPPERCASE and see what happens) ")
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Display chat messages from history on app rerun
	for message in st.session_state.msg:
		st.chat_message(message["role"]).markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.msg.append({"role": "user", "content": prompt})

		# define rule-based response
		response = ""
		if prompt.lower() == "hello":
			response = "Hi there what can I do for you"
		else:
			response = f"Echo: {prompt}"

		# Display assistant response in chat message container
		st.chat_message("assistant").markdown(response)
		# Add assistant response to chat history
		st.session_state.msg.append({"role": "assistant", "content": response})


def ex7():
	st.subheader("Exercise 7: Session State with User Input")
	st.write("Now, lets create **prompt_inputs_form()** function that will get the user's input from the textbox and store it in the session state. ")

	st.markdown(
	"""
	For this exercise, we will:
	- Create a form using **st.form()**. Each form must contain a **st.form_submit_button**. A form is a container that organize different elements together (e.g. textbox, radio button). Upon sumission, all element values inside the form will be sent together for further processing. 
	- Store user input into **st.session_state**. 
	""" 
	)	
 
	st.write("The created session state variable (:green[**prompt_template**]) contains input that you have entered. It will be used in **Exercise 10**.")
	with st.expander("Reveal Code"): st.code(mc.code_ex7, language='python')
	after_reveal_code(True)
	prompt_inputs_form()

# Exercise 7 : prompt input form
def prompt_inputs_form():  
    
	# with st.expander("Reveal Code"): st.code(mc.code_ex7, language='python')
	with st.form("Prompt Template"):
		my_prompt_template = st.text_input("Enter a system prompt template. E.g. Reply in Singlish.")

		submitted = st.form_submit_button("Submit")
		if submitted:
			st.session_state.prompt_template = my_prompt_template
			st.success(f"""your session_state.prompt_template is set to: 
				**'{my_prompt_template}'**""")
			return st.session_state.prompt_template

		# display session_state.prompt_template if any
		if st.session_state.prompt_template:
			st.write("**your session_state.prompt_template is set to:**")
			st.write(st.session_state.prompt_template)


def secrets():
	st.subheader("Secrets Managment with Streamlit🤫")
	st.write("Before doing the next few exercises, you will need to hide your API keys (e.g. OpenAI, PALM, Pinecone) or any other credentials/secrets.")
	st.write("In your **CHATBOT** working directory, create a new folder :red[**.**]**streamlit**.")
	st.write("Do take note of the **dot** infront of the folder.")
	st.write("Under the new folder, create a new file **secrets.toml**. The file content will be provided during the workshop.")
	st.write(":blue[**Code**]")
	st.code(
     """
     openai_key="xxxxxx"
     palm_api_key="xxxxxx"
     pinecone_key="xxxxxx"
     """, language="python")
	st.caption("Replace '**xxxxxxx**' with the API keys accordingly in your **secrets.toml**:")
	st.write(" ")
	st.write("Lastly, if you are commiting the code to github, in your **CHATBOT** directory, create a file **.gitignore** and add :green[**.streamlit/**] into it. A .gitignore file specifies intentionally directories/files that Git should ignore.")


# Exercise 8 : Using the OpenAI API
import openai
os.environ["OPENAI_API_KEY"] = st.secrets["openai_key"]
openai.api_key = st.secrets["openai_key"]

def openai_completion(prompt):
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": st.session_state.prompt_template},
			{"role": "user", "content": prompt},
		],
		temperature=0.5,  # temperature between 0 and 1. The higher the temperature, the more random the results
	)
	return response

# integration API call into chat components
def ex8():
	st.subheader("Exercise 8: Incorporating LLM API (OpenAI) into your chatbot")
	st.write("Recall in Exercise 6, the rule-based chatbot shows the chat history, get the user chat input and echoes the user chat input back to the user?")
	st.write("Also recall in Exercise 7, you created a session state variable (**prompt_template**) and stored the input that you have entered inside this session variable?")	
	st.write("Now, instead of echoing the user input, you will be passing the user **chat input** and **prompt_template** set in Exercise 7 to OpenAI API to generate a response.")
	st.markdown(
	"""
	For this exercise, we will:
	- Create a new function :blue[**openai_completion()**] to generate a response from OpenAI based on user chat input. Note that there is a new import statement :blue[**import openai**].
	- Call OpenAI LLM API using **openai.ChatCompletion.create()** inside :blue[**openai_completion()**].
	- Set the following prarameter for **openai.ChatCompletion.create()**:
		- :green[**model**]: The OpenAI GPT model to use (e.g. gpt-3.5-turbo, gpt-4). 
		- :green[**messages**]: Often adopt specific roles to guide the model's responses (the three roles: :green[user], :green[system], :green[assistant]).   
		- :green[**temperature**]: The higher the temperature, the more random the results. (Temperature is between 0 and 1)  
	""" 
	)
	with st.expander("When to use the different messages role?"): 	
		st.markdown(
		"""
		- :green[user]: The user messages help instruct the assistant. Generated by end user like you and me   
		- :green[system]: The system messages set the behavior of the assistant. This is the model identity. For this exercise, the assistant will be instructed with the **prompt_template** set in Exercise 7 (e.g. You are a philosophy teacher). 
		- :green[assistant]: The assistant messages stores prior responses. This is to remind the model of its previous responses.   
		""" 
		)
		st.write(" ")
		st.write("**Code Example of the different messages role**")
		st.code('''
        response = openai.ChatCompletion.create(
		model="gpt-3.5.turbo",
		messages=[
			{"role": "system", "content": st.session_state.prompt_template},
			{"role": "user", "content": query},
			{"role": "assistant", "content": "model previous responses"},   
		],
		temperature=0
	)
          ''', language='python')
	with st.expander("Temperature Tips"): 	st.markdown(
	"""
	- For transformation tasks (extraction, standardization, format conversion, grammar fixes), consider a temperature of 0 or up to 0.3.   
	- For writing tasks, you should adjust the temperature higher, closer to 0.5. If you want GPT to be highly creative (for marketing or advertising copy for instance), consider values between 0.7 and 1  
	- If you want to experiment and create many variations quickly, a high temperature is better. But do note that a very high temperature increases the risk of 'hallucination', meaning that the AI starts selecting words that will make no sense or be offtopic.     
	""" 
	)
	with st.expander("Reveal Code"): st.code(mc.code_ex8, language='python')
	after_reveal_code(True)
	st.subheader("Chatbot using OpenAI API", divider='rainbow') 

	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "You are a helpful assistant"

	# display session_state.prompt_template if any
	if st.session_state.prompt_template:
		st.write("**Your :green[session_state.prompt_template] is set to:**", st.session_state.prompt_template)
		st.caption("Recall in **Exercise 7**, you stored the input you have entered in **session_state.prompt_template**?")
 	
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Display chat messages from history on app rerun
	for message in st.session_state.msg:
		if message["role"]=='assistant':
			st.chat_message(message["role"], avatar='./avatar.png').markdown(message["content"])
		else:
			st.chat_message(message["role"]).markdown(message["content"])

	# React to user input
	if prompt := st.chat_input("What is up?"):
		# Display user message in chat message container
		st.chat_message("user").markdown(prompt)
		# Add user message to chat history
		st.session_state.msg.append({"role": "user", "content": prompt})

		# call OpenAI API to get response
		response_raw = openai_completion(prompt)
		response = response_raw["choices"][0]["message"]["content"].strip()
		total_tokens = str(response_raw["usage"]["total_tokens"])
  
		# Display assistant response in chat message
		st.chat_message("assistant", avatar='./avatar.png').markdown(response)
		c = st.empty()
		c.markdown(f"**Total tokens used in last converstation:** {total_tokens}")
  
		# Add assistant response to chat history
		st.session_state.msg.append({"role": "assistant", "content": response})


# Exercise 9 : Using the OpenAI API with streaming option
# if "prompt_template" not in st.session_state:
# 	st.session_state.prompt_template = "You are a helpful assistant" 
# def openai_completion_stream(query, prompt_template = st.session_state.prompt_template):
def openai_completion_stream(query, prompt_template_passin):
	MODEL = "gpt-3.5-turbo"
	response = openai.ChatCompletion.create(
		model=MODEL,
		messages=[
			{"role": "system", "content": prompt_template_passin},
			{"role": "user", "content": query},
		],
		temperature=0,
		stream=True, 
		# stream the results from the ChatGPT API as they were generated, 
  		# rather than waiting for the entire thing to complete before displaying anything.
	)
	return response

# integration API call into streamlit chat components
def ex9():
	st.subheader("Exercise 9: Building a ChatGPT-like clone with streaming responses")
	st.write("Now, we will incorporate a streaming response (real-time text generation) from the LLM API into our chatbot to mimic the behaviour of ChatGPT. This will enhance the level of engagement and interaction between the chatbot and the user.")
	st.markdown(
	"""
	For this exercise, we will:
	- Create a new function **openai_completion_stream(*query*, *prompt_template_passin*)** that takes in two arguments to generate streaming response from OpenAI based on user input. 
	- Set the prarameter :green[**stream=True**] for :green[**openai.ChatCompletion.create()**] inside **openai_completion_stream()**.
	- Handle real-time text generation response in ex9() using **for-loop**. For-loop is a conditonal iterative statement that is used to repeat a specific block of code until a condition is met.
	""" 
	)
	with st.expander("Reveal Code"): st.code(mc.code_ex9, language='python')
	after_reveal_code(True) 
	st.subheader("Chatbot using OpenAI Stream API", divider='rainbow')
 
	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "You are a helpful assistant"
  
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# display session_state.prompt_template if any
	if st.session_state.prompt_template:
		st.write("**Your :green[session_state.prompt_template] is set to:**", st.session_state.prompt_template)
		st.caption("Recall in **Exercise 7**, you stored the input you have entered in **session_state.prompt_template**?")

	# Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])

	if query := st.chat_input("say something"):
		# set user prompt in chat history
		st.session_state.msg.append({"role": "user", "content": query})
		with st.chat_message("user"):
			st.markdown(query)

		with st.chat_message("assistant"):
			message_placeholder = st.empty()
			full_response = ""
			# streaming function
			for response in openai_completion_stream(query,st.session_state.prompt_template):
				full_response += response.choices[0].delta.get("content", "")
				message_placeholder.markdown(full_response + "▌")
			message_placeholder.markdown(full_response)
		st.session_state.msg.append({"role": "assistant", "content": full_response})
		


# Exercise 10: Chatbot with memory
from langchain.memory import ConversationBufferWindowMemory
def ex10():
	st.subheader("Exercise 10: Chatbot with memory")
	st.write("Now, we will create a chatbot similar to Exercise 9 but with memory. The memory that will be used is ***langchain* ConversationBufferwindowMemory**.")
	st.write(":green[**ConversationBufferwindowMemory(K=n)**] keeps a list of the interactions of the coversation over time. You can determine the number of previous messages to remember by setting the ***K*** parameter.")
 
	st.markdown(
	"""
	For this exercise, we will:
	- Call the function **prompt_inputs_forms()** created in Exercise 7 to display the form in case user want to set a new prompt template
	- Set the number of previous messages to remember in :green[**ConversationBufferwindowMemory(K=n)**] and store the memory in :green[**st.session_state.memory**]. Note that there is a new import statement :blue[**from *langchain.memory* import ConversationBufferWindowMemory**].
	- Integrate the memory with the session state prompt template :green[**st.session_state.prompt_template**]
	- Save the conversation in the memory using :green[**save_context({"input": "user input msg"}, {"output": "model respond message"})**]
	""" 
	) 
 
	with st.expander("Reveal Code"): st.code(mc.code_ex10, language='python')
	after_reveal_code(True) 
	st.subheader("Chatbot with Memory", divider='rainbow')
	
	# display prompt_inputs_form in case user want to set a new prompt template
	prompt_inputs_form()

	if "memory" not in st.session_state: # k=3 means that the bot remember the last 3-rounds of converstaions
		st.session_state.memory = ConversationBufferWindowMemory(k=3) 

	# step 1 save the memory from your chatbot
	memory_data = st.session_state.memory.load_memory_variables({})
 
	# step 2 combine the memory with the prompt_template
	st.session_state.prompt_template_with_memory = f"""
{st.session_state.prompt_template}										

Below is the conversation history between the AI and Users so far

{memory_data}

"""
	# call the function in your base bot
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Showing Chat history
	for message in st.session_state.msg:
		st.chat_message(message["role"]).markdown(message["content"])
  
	try:
		if query := st.chat_input("say something?"):
			# set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": query})
			with st.chat_message("user"):
				st.markdown(query)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				# streaming function
				for response in openai_completion_stream(query, st.session_state.prompt_template_with_memory):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})
			st.session_state.memory.save_context({"input": query}, {"output": full_response})
		st.write("**Memory Data**: ", st.session_state.memory.load_memory_variables({}))
	except Exception as e:
		st.error(e)

	

# Exercise 11: RAG chatbot supported by LanceDB and OpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.embeddings import GooglePalmEmbeddings
from langchain.vectorstores import LanceDB
import lancedb
from langchain.text_splitter import RecursiveCharacterTextSplitter
# from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.document_loaders import DirectoryLoader
from langchain.document_loaders import TextLoader
from langchain.document_loaders import PyPDFLoader
from langchain.prompts import PromptTemplate

openaiembedding = OpenAIEmbeddings(openai_api_key=st.secrets["openai_key"])
palmembeddings = GooglePalmEmbeddings(google_api_key=st.secrets["palm_api_key"])

UPLOAD_DIRECTORY = os.path.join(os.getcwd(), "UPLOADED")
DB_DIRECTORY = os.path.join(os.getcwd(), "LanceDB") # define LanceDB directory 
TABLE_NAME = "my_table" # LanceDB table name
TBL_DIRECTORY = os.path.join(DB_DIRECTORY, TABLE_NAME+'.lance')
TARGET_DOC_TYPE = "PDF"
openaiembedding = OpenAIEmbeddings(openai_api_key=st.secrets["openai_key"])
palmembeddings = GooglePalmEmbeddings(google_api_key=st.secrets["palm_api_key"])

def document_loader():
	text_loader_kwargs={'autodetect_encoding': True}
	if TARGET_DOC_TYPE=="TXT":
		loader = DirectoryLoader(f"{UPLOAD_DIRECTORY}", glob="**/*.txt", loader_cls=TextLoader, loader_kwargs=text_loader_kwargs)
	elif TARGET_DOC_TYPE=='PDF':
		loader = DirectoryLoader(f"{UPLOAD_DIRECTORY}", glob="**/*.pdf", loader_cls=PyPDFLoader)
		#loader = PyPDFLoader(f"{UPLOAD_DIRECTORY}"/*.pdf")
		#documents = loader.load_and_split()
	else:
		return None


	documents = loader.load()
	# recursively tries to split by different characters to find one that works
	text_splitter = RecursiveCharacterTextSplitter(
		separators=['\n\n'],
		chunk_size=300, 
		chunk_overlap=0
	)
	documents = text_splitter.split_documents(documents)
	return documents

def lance_vectorstore_creator():
	documents = document_loader()
	#documents = document_loader(type='PDF')
	if documents:
		# Create a folder for VectorDB, and create only when it doesn't exist
		os.makedirs(DB_DIRECTORY, exist_ok=True)
		db = lancedb.connect(DB_DIRECTORY)
		table = db.create_table(
			TABLE_NAME,
			data=[
				{
					"vector": openaiembedding.embed_query("Hello World"),
					"text": "Hello World",
					"id": "1",
				}
			],
			mode="overwrite",
		)
		db = LanceDB.from_documents(documents, embedding=openaiembedding, connection=table)
		st.session_state.lance_vs = db
		return db
	else:
		# when document (e.g. othe than TXT and PDF) is not supported
		st.session_state.lance_vs = False
		return None


from datetime import datetime
def LanceDB_TableUpdateDate(TBL_DIRECTORY):		
	if os.path.exists(TBL_DIRECTORY):
		last_update_timestamp = os.path.getmtime(TBL_DIRECTORY)
		last_update_date = datetime.fromtimestamp(last_update_timestamp).strftime('%Y-%m-%d %H:%M:%S')
		st.info(f"""Last update date of Your LanceDB  
{TBL_DIRECTORY}

{last_update_date}
""")
		st.session_state.TBLdate = last_update_date
	else:
		st.error(f"Your LanceDB '{TBL_DIRECTORY}' does NOT exist.")


def RAG_LanceDB_OpenAI():
	with st.expander("Reveal Code"): st.code(mc.code_ex11, language='python')
	st.subheader('RAG Chatbot supported by LanceDB and OpenAI', divider='rainbow')
	# Add a button to create vectorstore
	lance_vs_btn = st.button('Create/Update LanceDB VectorStore')
	if lance_vs_btn:
		lance_vectorstore_creator()
	# display update date of LanceDB Table
	LanceDB_TableUpdateDate(TBL_DIRECTORY)
 
	# set prompt template for RAG to include {context} retreived from VectorDB
	st.session_state.prompt_template_RAG = """
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. 

<Context>: {context}

<Question>: {question}

<Answer>:
"""	
	st.markdown(f"#### Your RAG Prompt Template")
	st.write({st.session_state.prompt_template_RAG})

	input_prompt = PromptTemplate(
		input_variables=["context", "question"],
		template=st.session_state.prompt_template_RAG,
	)

	# if "memory" not in st.session_state: # k=3 means that the bot remember the last 3-rounds of converstaions
	# 	st.session_state.memory = ConversationBufferWindowMemory(k=3) 
	##step 1 save the memory from your chatbot
	# memory_data = st.session_state.memory.load_memory_variables({})
 	# st.write("**Memory Data**: ", memory_data)
	# Showing Chat history
	# for message in st.session_state.msg:
	# 	st.chat_message(message["role"]).markdown(message["content"])

	if st.session_state.lance_vs:
		vectorstore = st.session_state.lance_vs
		if query := st.text_input("**RAG1**"):
			# set user prompt in chat history
			# st.session_state.msg.append({"role": "user", "content": query})
			with st.chat_message("user"):
				st.markdown(query)

			docs = vectorstore.similarity_search(query=query, k=2)
			context = " \n".join([doc.page_content for doc in docs])

			input_prompt_formated = input_prompt.format(context=context, question=query)
			# st.session_state.msg.append({"role": "system", "content": input_prompt_formated})
			with st.chat_message("system", avatar = "🦜"):
				st.markdown(input_prompt_formated)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				# streaming function
				for response in openai_completion_stream(query, input_prompt_formated):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			# st.session_state.msg.append({"role": "assistant", "content": full_response})
			# st.session_state.memory.save_context({"input": query}, {"output": full_response})

def ex11_and_ex12():
	st.subheader("Exercise 11 & 12: Create RAG Chatbot and Vector Stores")
	st.write("Now, using what you have learn from previous exercises, you will now create a RAG Chatbot that stores data in a vector store.")
	st.write("This process uses OpenAI to generate embeddings and vector store (**LanceDB**/**Pinecone**) for storing text embeddings.")
	st.write("For experimentation, we will focus on TXT and/or PDF file(s) ONLY.")
	st.write("Soon you will notice the :red[**drawback of LanceDB**] is that it doesn't integrate with LangChain well and users have to recreate vector store everytime after application is restarted or session is refreshed. Whereas :green[**Pinecone**] is able to load existing indexes from vector store without a need to recreate.")
	st.markdown("""

	""" 
	)
	
	# with open("./UPLOADED/CDCMerchantsFAQ.pdf", "rb") as f:
	# 	st.download_button("CDCMerchantsFAQ PDF", f, "CDCMerchantsFAQ.pdf")
	st.divider()
	tab1, tab2, tab3 = st.tabs(["Spliting Chunks", "RAG Chatbot 1", "RAG Chatbot 2"])
	with tab1:
		# duplicate Excercise 5 - File Uploading
		uploaded_file = st.file_uploader("Upload a file", type=allowed_extensions)
		if uploaded_file is not None:
			if is_valid_file(uploaded_file):
				# Save the uploaded file to the upload folder
				file_path = os.path.join(f"{UPLOAD_DIRECTORY}", uploaded_file.name)
				with open(file_path, "wb") as f:
					f.write(uploaded_file.getvalue())
				st.success(f"File '{uploaded_file.name}' uploaded successfully.")
			else:
				st.error("Invalid file. Please upload a .docx, .txt, or .pdf file with a size of up to 10MB.")
		display_uploaded_files()
	
		st.divider()
		st.write(f"#### Your targeted document is **{TARGET_DOC_TYPE}**")
		documents=document_loader()
		st.write("**No. of Chunks:**", len(documents))
		st.write("**Chunk(s):**", documents)
	with tab2:		
		RAG_LanceDB_OpenAI()
	# comment off / uncomment the code when RAG_Pinecone_OpenAI is added from Exercise 12
	with tab3:		
		RAG_Pinecone_OpenAI()


# Exercise 12: RAG chatbot supported by Pinecone and OpenAI
from langchain.vectorstores import Pinecone
import pinecone

pinecone.init(api_key=st.secrets["pinecone_key"], environment="asia-northeast1-gcp")
vs_index_name = "workshop-vs"

def pinecone_vectorstore_creator(vs_index_name):
	documents = document_loader()
	dimensions = len(openaiembedding.embed_query("put anything"))
	# First, check if our index already exists. If it doesn't, we create it
	if vs_index_name not in pinecone.list_indexes():
		# we create a new index
		pinecone.create_index(
				name=vs_index_name,
				metric='cosine',
				dimension=dimensions)
	else:
		pinecone.delete_index(vs_index_name) # delete existing before create new
		pinecone.create_index(
				name=vs_index_name,
				metric='cosine',
				dimension=dimensions)

	if documents:
		# The OpenAI embedding model uses 1536 dimensions; Create Vector DB
		# The PALM embedding model uses 768 dimensions; Create Vector DB
		Pinecone.from_documents(documents, openaiembedding, index_name=vs_index_name)
		# connect to index
		index = pinecone.Index(vs_index_name)
		text_field = "text"
		db = Pinecone(index, openaiembedding, text_field)
		st.session_state.pinecone_vs = db
		return db
	else:
		# when document (e.g. othe than TXT and PDF) is not supported
		st.session_state.pinecone_vs = False
		return None

def RAG_Pinecone_OpenAI():
	with st.expander("Reveal Code"): st.code(mc.code_ex12, language='python')
	st.subheader("RAG supported by Pinecone and OpenAI", divider='rainbow')
	if "pinecone_vs" not in st.session_state:
		st.session_state.pinecone_vs = False 
  
	# Add a button to create vectorstore
	pinecone_vs_btn = st.button('Create/Update Pinecone VectorStore')

	if vs_index_name not in pinecone.list_indexes():
		st.error("pinecone index not exist")
	else:
		index = pinecone.Index(vs_index_name)
		text_field = "text"
		db = Pinecone(index, openaiembedding, text_field)
		st.session_state.pinecone_vs = db
		st.success("pinecone vectorstore successfully loaded")

	if pinecone_vs_btn:
		db = pinecone_vectorstore_creator(vs_index_name)
		st.session_state.pinecone_vs = db
		st.info("pinecone vectorstore successfully created/updated")

	# set prompt template for RAG to include {context} retreived from VectorDB
	st.session_state.prompt_template_RAG = """
Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. 

<Context>: {context}

<Question>: {question}

<Answer>:
"""	
	st.markdown(f"#### Your RAG Prompt Template")
	st.write({st.session_state.prompt_template_RAG})

	input_prompt = PromptTemplate(
		input_variables=["context", "question"],
		template=st.session_state.prompt_template_RAG,
	)
	if st.session_state.pinecone_vs:
		vectorstore = st.session_state.pinecone_vs
		if query := st.text_input("**RAG2**"):
			# set user prompt in chat history
			# st.session_state.msg.append({"role": "user", "content": query})
			with st.chat_message("user"):
				st.markdown(query)
			docs = vectorstore.similarity_search(query=query, k=2)
			context = " \n".join([doc.page_content for doc in docs])

			input_prompt_formated = input_prompt.format(context=context, question=query)
			# st.session_state.msg.append({"role": "system", "content": input_prompt_formated})
			with st.chat_message("system", avatar = "🦜"):
				st.markdown(input_prompt_formated)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = ""
				# streaming function
				for response in openai_completion_stream(query,input_prompt_formated):
					full_response += response.choices[0].delta.get("content", "")
					message_placeholder.markdown(full_response + "▌")
				message_placeholder.markdown(full_response)
			# st.session_state.msg.append({"role": "assistant", "content": full_response})


# Exercise 13: Using PALM API
import google.generativeai as palm
# set the PALM API key.
os.environ["PALM_API_KEY"] = st.secrets["palm_api_key"]
palm.configure(api_key=st.secrets["palm_api_key"])

# Call the PALM API and print the response.
def palm_chat(prompt):
	response = palm.chat(messages=prompt)
	print(response.last)
	return response.last

def ex13():
	with st.expander("Reveal Code"): st.code(mc.code_ex13, language='python')
	st.subheader("Chatbot using PALM API", divider='rainbow')
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Showing Chat history
	for message in st.session_state.msg:
		with st.chat_message(message["role"]):
			st.markdown(message["content"])
	try:
		if prompt := st.chat_input("say something"):
			# set user prompt in chat history
			st.session_state.msg.append({"role": "user", "content": prompt})
			with st.chat_message("user"):
				st.markdown(prompt)

			with st.chat_message("assistant"):
				message_placeholder = st.empty()
				full_response = palm_chat(prompt)
				message_placeholder.markdown(full_response)
			st.session_state.msg.append({"role": "assistant", "content": full_response})

	except Exception as e:
		st.error(e)



# Exercise 14: Using Vertex AI API (without stream)
from google.oauth2 import service_account
from langchain.chat_models import ChatVertexAI
from langchain.schema import HumanMessage, SystemMessage

google_api_cred = service_account.Credentials.from_service_account_info(
	info={
		"type": st.secrets['type'] ,
		"project_id": st.secrets['project_id'] ,
		"private_key_id": st.secrets['private_key_id'] ,
		"private_key": st.secrets['private_key'] ,
		"client_email": st.secrets['client_email'] ,
		"client_id": st.secrets['client_id'] ,
		"auth_uri": st.secrets['auth_uri'] ,
		"token_uri": st.secrets['token_uri'] ,
		"auth_provider_x509_cert_url": st.secrets['auth_provider_x509_cert_url'] ,
		"client_x509_cert_url": st.secrets['client_x509_cert_url'] ,
		"universe_domain": st.secrets['universe_domain'] 
	},
)

vertex_chat = ChatVertexAI(
		model_name="chat-bison",
		max_output_tokens=500,
		temperature=0,
		top_p=0.8,
		top_k=40,
		verbose=True,
		credentials = google_api_cred,
		project=google_api_cred.project_id,
	)

# integration API call into chat components
def ex14():
	with st.expander("Reveal Code"): st.code(mc.code_ex14, language='python')
	st.subheader("Chatbot using Vertex AI", divider="rainbow")
	# display prompt_inputs_form for user to set new prompt template
	prompt_inputs_form()

	if "memory" not in st.session_state: # k=3 means that the bot remember the last 3-rounds of converstaions
		st.session_state.memory = ConversationBufferWindowMemory(k=3) 

	# step 1 save the memory from your chatbot
	memory_data = st.session_state.memory.load_memory_variables({})
 
	# step 2 combine the memory with the prompt_template 
	st.session_state.prompt_template_with_memory = f"""
{st.session_state.prompt_template}										

Below is the conversation history between the AI and Users so far

{memory_data}

"""
	# call the function in your base bot
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Showing Chat history
	for message in st.session_state.msg:
		st.chat_message(message["role"]).markdown(message["content"])

	if query := st.chat_input("What is up?"):
		# set user prompt in chat history
		st.session_state.msg.append({"role": "user", "content": query})
		st.chat_message("user").markdown(query)

		with st.chat_message("assistant"):
			message_placeholder = st.empty()
			full_response = vertex_chat([SystemMessage(content=st.session_state.prompt_template_with_memory), HumanMessage(content=query)])
			message_placeholder.markdown(full_response.content)
		
		st.session_state.msg.append({"role": "assistant", "content": full_response.content})
		st.session_state.memory.save_context({"input": query}, {"output": full_response.content})
	st.write("**Memory Data**: ", st.session_state.memory.load_memory_variables({}))


# Exercise 15: Using VertexAI stream
# integration strem API call into chat components
def ex15():
	with st.expander("Reveal Code"): st.code(mc.code_ex15, language='python')
	st.subheader("Chatbot using Vertex AI Stream API", divider='rainbow')
	# display prompt_inputs_form for the user to set new prompt template
	prompt_inputs_form()

	if "memory" not in st.session_state: # k=3 means that the bot remember the last 3-rounds of converstaions
		st.session_state.memory = ConversationBufferWindowMemory(k=3) 

	# step 1 save the memory from your chatbot
	memory_data = st.session_state.memory.load_memory_variables({})
 
	# step 2 combine the memory with the prompt_template
	st.session_state.prompt_template_with_memory = f"""
{st.session_state.prompt_template}										

Below is the conversation history between the AI and Users so far

{memory_data}

"""
	# Initialize chat history
	if "msg" not in st.session_state:
		st.session_state.msg = []

	# Showing chat history
	for message in st.session_state.msg:
		st.chat_message(message["role"]).markdown(message["content"])

	if query := st.chat_input("say something"):
		# set user prompt in chat history
		st.session_state.msg.append({"role": "user", "content": query})
		with st.chat_message("user"):
			st.markdown(query)
   
		with st.chat_message("assistant"):
			message_placeholder = st.empty()
			full_response = ""
			for response in vertex_chat.stream([SystemMessage(content=st.session_state.prompt_template_with_memory) ,HumanMessage(content=query)]):
				full_response += response.content
				message_placeholder.markdown(full_response + "▌")
			message_placeholder.markdown(full_response)

		st.session_state.msg.append({"role": "assistant", "content": full_response})
		st.session_state.memory.save_context({"input": query}, {"output": full_response})
	st.write("**Memory Data**: ", st.session_state.memory.load_memory_variables({}))


# Exercise 16: Smart Agent
from langchain.agents import ConversationalChatAgent, AgentExecutor
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.memory.chat_message_histories import StreamlitChatMessageHistory
from langchain.tools import DuckDuckGoSearchRun

# https://github.com/langchain-ai/streamlit-agent/blob/main/streamlit_agent/search_and_chat.py
def ex16():
	st.subheader("🦜 LangChain: Chat with Internet Search")

	msgs = StreamlitChatMessageHistory()
	memory = ConversationBufferMemory(
     chat_memory=msgs, return_messages=True, memory_key="chat_history", output_key="output"
	)
	reset_btn = st.button("Reset chat history")
	if len(msgs.messages) == 0 or reset_btn:
		msgs.clear()
		msgs.add_ai_message("How can I help you?")
		st.session_state.steps = {}

	avatars = {"human": "user", "ai": "assistant"}
	for idx, msg in enumerate(msgs.messages):
		with st.chat_message(avatars[msg.type]):
			# Render intermediate steps if any were saved
			for step in st.session_state.steps.get(str(idx), []):
				if step[0].tool == "_Exception":
					continue
				with st.status(f"**{step[0].tool}**: {step[0].tool_input}", state="complete"):
					st.write(step[0].log)
					st.write(step[1])
			st.write(msg.content)

	if prompt := st.chat_input(placeholder="say something"):
		st.chat_message("user").write(prompt)

		# llm = ChatVertexAI(model_name="chat-bison",temperature=0, credentials = google_api_cred, project=google_api_cred.project_id)
		llm = ChatOpenAI(model_name="gpt-3.5-turbo-16k", temperature=0, openai_api_key=st.secrets["openai_key"], streaming=True)
		tools = [DuckDuckGoSearchRun(name="Search")]
		chat_agent = ConversationalChatAgent.from_llm_and_tools(llm=llm, tools=tools)
		executor = AgentExecutor.from_agent_and_tools(
			agent=chat_agent,
			tools=tools,
			memory=memory,
			return_intermediate_steps=True,
			handle_parsing_errors=True,
		)
		with st.chat_message("assistant"):
			st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
			response = executor(prompt, callbacks=[st_cb])
			st.write(response["output"])
			st.session_state.steps[str(len(msgs.messages) - 1)] = response["intermediate_steps"]






from streamlit_antd_components import divider 
def main():	
	st.set_page_config(
		page_icon="🧊",
		layout="wide",
	) 

	st.title("Hands-on Workshops 2023")	
	divider(label='Exploring Generative AI: Codecraft Workshop', icon='journal-code', align='left')

	if "prompt_template" not in st.session_state:
		st.session_state.prompt_template = "You are a helpful assistant"
	if "memory" not in st.session_state:
		st.session_state.memory = ConversationBufferWindowMemory(k=3)
	if "msg" not in st.session_state:
		st.session_state.msg = []
	# initialize vectorstore in session_state
	if "TBLdate" not in st.session_state:
		st.session_state.TBLdate = False
	if "lance_vs" not in st.session_state:
		st.session_state.lance_vs = False
	if "pinecone_vs" not in st.session_state:
		st.session_state.pinecone_vs = False
 
	password_container = st.empty()
	password_container.text_input("Enter the password", key="pwd_input", type="password")

	if st.session_state.pwd_input == st.secrets['workshop_pwd']:
		password_container.empty()
		workshop_sidebar()
	elif st.session_state.pwd_input!='' and st.session_state.pwd_input != st.secrets['workshop_pwd']:
		st.error("Incorrect password. Please enter the correct password to proceed.")


if __name__ == "__main__":
	main()
