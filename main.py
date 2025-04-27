import networkx as nx
from graph_builder import build_game_graph
import pandas as pd


def recommend_similar_games(G, game_id, game_lookup, min_weight=2, top_n=5):
    if game_id not in G:
        print("⚠️  Game not found in network.")
        return

    game_name = game_lookup.get(game_id, f"Unknown Game ({game_id})")
    print("\n" + "="*50)
    print(f"🎮 Top {top_n} Similar Games to: '{game_name}'")
    print("="*50)

    neighbors = sorted(G[game_id].items(), key=lambda x: x[1]['weight'], reverse=True)
    strong_recommendations = [(n, attr) for n, attr in neighbors if attr['weight'] >= min_weight]

    if not strong_recommendations:
        print(f"No strong recommendations found (shared users < {min_weight}).")
        print(f"But it has {len(neighbors)} weak connections.")
        return

    for idx, (neighbor, attr) in enumerate(strong_recommendations[:top_n], 1):
        neighbor_name = game_lookup.get(neighbor, f"Unknown Game ({neighbor})")
        print(f"{idx}. {neighbor_name:<30} | Shared Users: {attr['weight']}")

    print("="*50)


def display_shortest_path(G, source_id, target_id, game_lookup):
    if source_id not in G or target_id not in G:
        print("⚠️  One or both games not found in the network.")
        return

    try:
        path = nx.shortest_path(G, source=source_id, target=target_id)
        print("\n🔗 Shortest Path Between Games:")
        print("="*40)
        for idx, game_id in enumerate(path):
            game_name = game_lookup.get(game_id, f"Unknown Game ({game_id})")
            print(f"{idx+1}. {game_name} (ID: {game_id})")
        print("="*40)
    except nx.NetworkXNoPath:
        print("❌ No path found between these games.")


def display_influential_games(G, game_lookup, top_n=5):
    print("\n⭐ Top Influential Games (by PageRank):")
    print("="*50)

    pr = nx.pagerank(G)
    top_games = sorted(pr.items(), key=lambda x: x[1], reverse=True)[:top_n]

    for idx, (game_id, score) in enumerate(top_games, 1):
        game_name = game_lookup.get(game_id, f"Unknown Game ({game_id})")
        print(f"{idx}. {game_name:<30} | Score: {score:.4f}")

    print("="*50)


def search_game_id(game_lookup):
    query = input("Enter part of the game name to search: ").lower()

    print("\n🔍 Search Results:")
    print("="*40)

    matches = [(app_id, name) for app_id, name in game_lookup.items() if query in name.lower()]

    if not matches:
        print("No games found matching your query.")
        return

    for app_id, name in matches:
        print(f"- {name} (ID: {app_id})")

    print("="*40)



def main():
    G = build_game_graph('data/recommendations.csv')

    # Load Game ID to Name mapping
    game_lookup = pd.read_csv('data/games.csv', usecols=['app_id', 'title']).set_index('app_id')['title'].to_dict()

    while True:
        print("\n--- Steam Game Network ---")
        print("1. Recommend similar games")
        print("2. Find shortest path between two games")
        print("3. Find most influential games")
        print("4. Search for Game ID by Name") 
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            print("Sample Game IDs in network:", list(G.nodes)[:10])
            game_id = int(input("Enter Game ID: "))
            recommend_similar_games(G, game_id, game_lookup)
        elif choice == '2':
            source = int(input("Source Game ID: "))
            target = int(input("Target Game ID: "))
            display_shortest_path(G, source, target, game_lookup)
        elif choice == '3':
            display_influential_games(G, game_lookup)
        elif choice == '4':
            search_game_id(game_lookup)
        elif choice == '5':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
