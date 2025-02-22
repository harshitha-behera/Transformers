# Transformers

## Enhanced Chatbot with DialoGPT

An AI-powered chatbot built using **Hugging Face's DialoGPT** and **Streamlit** for an interactive UI. This chatbot allows users to engage in real-time conversations and generates intelligent responses.

---

### 🚀 Features

- Real-time AI chatbot powered by **DialoGPT**
- Interactive web interface using **Streamlit**
- Maintains chat history in session
- Customizable UI with background and heading styling

---

### 📋 Requirements

Before running the project, ensure you have the following installed:

- Python 3.8+
- pip (Python package manager)

Install the required libraries:

```bash
pip install streamlit transformers torch
```

---

### 💻 Usage

1. **Clone the repository:**

```bash
git clone https://github.com/harshitha-behera/Transformers/tree/b32eee5cbf81158bd52e449eb8a23139e350d825/chatbot_DialoGPT
cd Transformers
cd chatbot_DialoGPT
```

2. **Run the Streamlit application:**

```bash
streamlit run main.py
```

3. **Access the chatbot:**

The app will automatically open in your browser at:

```
http://localhost:8501
```


### 🖼️ Sample Output

Here’s how the chatbot looks in action:

#### Initial Screen

![image](https://github.com/user-attachments/assets/ae8df5e5-fac5-46e7-a87d-c97e0e1205f2)


#### Chat in Progress

![image](https://github.com/user-attachments/assets/fe000bda-b74f-438a-a461-56bf83a1f14f)


---

### ❓ Troubleshooting

- **ModuleNotFoundError:** Ensure all packages are installed using:

  ```bash
  pip install streamlit transformers torch
  ```

- **Streamlit Command Error:**
  Make sure to run the app with:

  ```bash
  streamlit run main.py
  ```

---

### 📄 License

This project is licensed under the MIT License.

---

### 🙌 Acknowledgements

- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
- [PyTorch](https://pytorch.org/)

---

Happy chatting! 🤖


Harshitha Behera
Video Link:
https://umsystem.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f9e95329-af20-4d06-b59f-b28c00566b13&start=0

Code File:
https://github.com/harshitha-behera/Transformers/tree/0566c54c05c0eead05eda63b7634b9acf5db795a/chatbot_DialoGPT




Harshitha Behera: Enhanced Chatbot with DialoGPT
Summary of Enhanced Chatbot with DialoGPT
Overview
The provided Python code implements an interactive chatbot using the DialoGPT-medium model from Microsoft's Transformers library. This chatbot uses the Streamlit framework for building an intuitive web interface and PyTorch for handling machine learning model computations.
How the Code Works
1.	Library Imports:
o	streamlit: Used to create a simple and interactive web application.
o	transformers: Provides access to pre-trained language models.
o	torch: Handles tensor operations and model execution.
2.	Model Initialization:
o	Loads the DialoGPT-medium model and its tokenizer from Hugging Face’s model hub.
3.	Web Interface with Streamlit:
o	A title and description are displayed on the web app.
o	Light blue background and dark purple header styling are applied for better UI aesthetics.
4.	Chat Functionality:
o	Uses Streamlit's session state to maintain chat history.
o	Captures user input through a text box.
o	Encodes the user's message, generates a response using DialoGPT, and decodes it.
o	Displays both user and bot messages sequentially on the app.
5.	Error Handling:
o	Catches and notifies the user if required libraries are missing.
Real-World Use Cases
1.	Customer Support Chatbots:
o	Businesses can use similar bots to handle frequently asked questions, helping to reduce customer service costs.
2.	Virtual Assistants:
o	Can be embedded in personal apps or devices to assist users with reminders, scheduling, or providing information.
3.	Educational Platforms:
o	An AI tutor that helps students with queries, explains concepts, or assists with practice questions.
4.	Entertainment:
o	Used in gaming for creating interactive NPC dialogues or as a conversational companion.
5.	Healthcare Support:
o	Helps patients schedule appointments, answer common questions, and provide health-related information (non-diagnostic).
Usage Example
Imagine integrating this chatbot on an e-commerce website:
•	User: "What are your store hours?"
•	Bot: "Our store is open from 9 AM to 9 PM every day."
Or in an educational platform:
•	User: "Can you explain Newton's first law?"
•	Bot: "Newton's first law states that an object will remain at rest or move in a straight line unless acted upon by an external force."
This demonstrates how AI chatbots enhance user engagement, streamline customer service, and provide valuable assistance across various domains.

Code File:
https://github.com/harshitha-behera/Transformers/tree/0566c54c05c0eead05eda63b7634b9acf5db795a/chatbot_DialoGPT
Output:
 

 




