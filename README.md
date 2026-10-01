# 🧱 Ricochet

**A colorful brick-breaker arcade game, built entirely with Python's Turtle module.**

Ricochet is a classic Breakout-style game: control a paddle to keep a bouncing ball alive, smash through five rainbow rows of bricks, and clear the board before you run out of lives.

---

## 🎮 Gameplay

- Move the paddle left and right to keep the ball in play
- The ball bounces off walls, the ceiling, the paddle, and every brick it hits
- Each destroyed brick adds to your score
- You start with **3 lives** — missing the ball costs a life and resets the ball to center
- Clear all 55 bricks to **win**; lose all your lives and it's **game over**

---

## 🛠️ Tech Stack

- **Python 3**
- **`turtle`** — rendering, movement, and keyboard input
- **`time`** — game loop timing

No external dependencies — everything used is part of Python's standard library.

---

## 📁 Project Structure

```
ricochet/
├── code.py          # Full game logic
└── README.md
```

---

## ⌨️ Controls

| Key           | Action           |
|----------------|------------------|
| `→` Right Arrow | Move paddle right |
| `←` Left Arrow  | Move paddle left  |

---

## ▶️ Getting Started

### Prerequisites
- Python 3 (Turtle is included in the standard library, so no extra installs are needed)

### Running the Game

```
git clone https://github.com/rhitamcoder/ricochet.git
```
```
cd ricochet
```
```
python code.py
```

A game window will open — use the arrow keys to move the paddle and keep the ball alive. Close the window at any time to end the game.

---

## 🧠 How It Works

- **Brick grid:** 5 rows × 11 columns of bricks are generated at the start, each row colored differently (red, orange, yellow, green, blue), and stored in a list for collision checking
- **Ball physics:** the ball moves by a fixed `dx`/`dy` each frame, bouncing (reversing direction) off walls, the ceiling, the paddle, and bricks using simple coordinate boundary checks
- **Collision detection:** uses distance-based checks (comparing x/y coordinates within a threshold) for ball-paddle and ball-brick hits — no physics engine, just Turtle coordinates
- **Score & lives tracking:** displayed via dedicated Turtle text objects, updated and re-rendered on every hit or life lost
- **Game loop:** a `while True` loop paced with `time.sleep()` and `screen.update()` drives all movement, bouncing, and collision logic each frame

---

## 📝 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.
