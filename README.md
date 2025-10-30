# 🧹 Simple Reflex Agent – Room Cleaning AI

## 📘 Overview
This project demonstrates a **Simple Reflex Agent** using **Artificial Intelligence concepts**.  
The agent's goal is to clean four rooms (A, B, C, D).  
If a room is dirty, the agent cleans it; otherwise, it moves to the next room.  
This simulation also includes a **visual animation** using `matplotlib`.

---

## 🧠 Logic Description
- There are **4 rooms**: A, B, C, D  
- Each room can be either **Clean** or **Dirty**  
- The agent:
  1. Starts from Room A  
  2. Checks the current room’s status  
  3. If **Dirty → cleans the room**  
  4. If **Clean → moves to next room**  
  5. Repeats until all rooms are clean  

---

## 🧩 Technologies Used
- **Python 3**
- **Matplotlib** (for visualization)
- **Random** module (for generating random room states)
- **Time** module (for animation delays)

---

## 💻 How to Run
1. Make sure you have Python installed (Python 3.8+ recommended).  
2. Install the required library:
   ```bash
   pip install matplotlib
   ```
3. Save the code in a file named `reflex_agent.py`
4. Run the program:
   ```bash
   python reflex_agent.py
   ```
5. Watch the agent clean the rooms step by step! 🤖

---

## 🎨 Visualization
- 🟥 **Red Room** → Dirty  
- 🟩 **Green Room** → Clean  
- 🤖 **Robot Emoji** shows the agent’s current position  

Each step updates the visualization to show the agent’s movement and cleaning actions.

---

## 📸 Example Output
```
Agent in Room A → Dirty
Cleaning...
Agent in Room B → Clean
Already clean, moving on...
Agent in Room C → Dirty
Cleaning...
All rooms cleaned!
```

---

## 🚀 Future Improvements
- Add user input to make rooms dirty manually  
- Create a GUI using `tkinter` or `pygame`  
- Add random movement or multiple agents  

---

## 👨‍💻 Author
**Your Name**  
AI Student | Python Enthusiast  
📧 your.email@example.com  
