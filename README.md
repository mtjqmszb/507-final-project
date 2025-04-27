# 🎮 Steam Game Recommendation & Network Explorer

## Overview

This project builds a **graph-based recommendation system** using real Steam user recommendation data. By analyzing how players co-recommend games, we create a network where:

- **Nodes** = Games
- **Edges** = Games recommended by the same users
- **Edge Weights** = Number of shared recommending users

The program allows users to explore relationships between games through a command-line interface (CLI), offering features like game recommendations, shortest paths between games, and identifying the most influential games.

---

## Features

- 🔗 **Recommend Similar Games**  
  Get top related games based on shared player recommendations.

- 🧭 **Find Shortest Path Between Two Games**  
  Discover how two games are connected through player behavior.

- ⭐ **Identify Most Influential Games**  
  Uses PageRank to find central "hub" games in the network.

- 🔍 **Search for Game IDs by Name**  
  Easily look up a game's ID using partial name search.

---

## Project Structure

```bash
steam_game_network_project/
├── data/
│ ├── recommendations.csv
│ ├── games.csv
│ └── games_metadata.json
├── main.py
├── graph_builder.py
├── README.md
└── requirements.txt
```

> ⚠️ **Note:** The program processes a limited number of users (`max_users = 100,000`) for efficiency. Only games present in the recommendation data will appear in the network.

---

## How to Run

1. **Install Dependencies**  
   Ensure you have Python 3.x installed. Then install required packages:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Program**

   ```bash
   python main.py
   ```

3. **Follow the CLI Prompts**  
   You'll see a menu like this:

   ```
   --- Steam Game Network ---

   1. Recommend similar games
   2. Find shortest path between two games
   3. Find most influential games
   4. Search for Game ID by Name
   5. Exit
   ```
