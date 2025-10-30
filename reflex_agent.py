import random
import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# --- Environment setup ---
rooms = ["A", "B", "C", "D"]
room_states = {room: random.choice(["Clean", "Dirty"]) for room in rooms}
agent_position = 0  # Start from Room A

# --- Visualization setup ---
fig, ax = plt.subplots(figsize=(8, 3))
plt.ion()

def draw_environment():
    ax.clear()
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 3)
    ax.axis('off')

    for i, room in enumerate(rooms):
        color = "lightgreen" if room_states[room] == "Clean" else "salmon"
        ax.add_patch(Rectangle((i*2, 1), 1.5, 1, facecolor=color, edgecolor="black", linewidth=2))
        ax.text(i*2 + 0.75, 1.5, f"{room}\n{room_states[room]}", ha="center", va="center", fontsize=10, weight="bold")
    
    # Draw Agent
    ax.text(agent_position*2 + 0.75, 0.5, "🤖", ha="center", va="center", fontsize=16)
    plt.draw()
    plt.pause(0.8)

# --- Reflex Agent Function ---
def reflex_agent():
    global agent_position
    for i in range(len(rooms)):
        current_room = rooms[agent_position]
        draw_environment()
        print(f"Agent in Room {current_room} → {room_states[current_room]}")

        if room_states[current_room] == "Dirty":
            print("Cleaning...")
            room_states[current_room] = "Clean"
        else:
            print("Already clean, moving on...")

        draw_environment()
        time.sleep(0.5)
        agent_position = (agent_position + 1) % len(rooms)

    print("\nAll rooms cleaned!")

# --- Run Simulation ---
reflex_agent()
plt.ioff()
plt.show()
