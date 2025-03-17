# 👻 Find the Phantom - A Bayesian Inference Game

**Find the Phantom** is a Python-based interactive game where players must locate the phantom on an **8x13 grid**. The game provides feedback using a **distance sensor** that changes colors based on proximity to the phantom.

---

## 🎯 Game Mechanics
- **Click a cell** to receive feedback on how close you are to the phantom.
- The game uses **Bayesian Inference** to update probabilities after each move.
- Players start with **10 points and 2 attempts**.
- The game ends when you **find the phantom or run out of points/attempts**.

---

## 🌈 Color-Based Feedback
| Color         | Meaning  |
|--------------|----------------------------------|
| 🟣 **Purple** | Phantom is at the clicked position. |
| 💗 **Pink**   | 1-2 cells away. |
| 💛 **Yellow** | 3-4 cells away. |
| 💚 **Light Green** | 5+ cells away. |

---

## 🛠 Technologies Used
- **Python 3.x**
- **NumPy** (for probability matrix operations)
- **Tkinter** (for graphical user interface)

---

## 🚀 Installation & Setup
### **1️⃣ Install Python & Dependencies**
Ensure you have Python installed, then run:
```sh
pip install numpy
```

### **2️⃣ Run the Game**
```sh
python main.py
```

---

## 📂 Project Structure
```
📂 FindThePhantom/
  📂 src/
    📜 gui.py              # Handles the graphical user interface
    📜 inference.py        # Implements Bayesian inference for probability updates
    📜 main.py             # Main game logic and execution
    📜 sensors.py          # Simulates sensor feedback for distance detection
    📂 __pycache__/        # Compiled Python files
```

---

## 🕹️ How to Play
1. Start with **10 points** and **2 attempts**.
2. Click a cell on the grid to receive feedback.
3. Use the color feedback to refine your guesses.
4. Find the phantom before your **points/attempts run out**.

---

## 👥 Contributors
- **Maria Chmite** - [@MariaChmite](https://github.com/MariaChmite)
- **Salim El Ghersse** - [@SalimElGhersse](https://github.com/SalimElGhersse)
- **Mohamed Ouballouk** - [@MohamedOuballouk](https://github.com/MohamedOuballouk)

🔹 Special thanks to **Dr. Tajeddine Rachidi** for guidance and support!

---

## 📜 License
This project is **open-source** and free to use. Contributions are welcome! 🚀

---

## 📫 Connect With Us
💡 **Maria Chmite** – [GitHub](https://github.com/MariaChmite) | [LinkedIn](https://linkedin.com/in/maria-chmite)
💡 **Salim El Ghersse** – [GitHub](https://github.com/SalimElGhersse)
💡 **Mohamed Ouballouk** 

---

🎉 **Enjoy the game & keep innovating!** 🚀
