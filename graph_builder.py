import pandas as pd
import networkx as nx

def build_game_graph(recommendation_file, min_shared_users=2):
    print("Building game similarity graph...")
    G = nx.Graph()

    chunksize = 100000   # Reduce chunk size
    processed_users = 0
    max_users = 1000000    # Limit for testing

    for chunk in pd.read_csv(recommendation_file, usecols=['user_id', 'app_id', 'is_recommended'], chunksize=chunksize):
        chunk = chunk[chunk['is_recommended'] == True]
        
        for user_id, group in chunk.groupby('user_id'):
            games = list(group['app_id'])
            for i in range(len(games)):
                for j in range(i + 1, len(games)):
                    game1, game2 = games[i], games[j]
                    if G.has_edge(game1, game2):
                        G[game1][game2]['weight'] += 1
                    else:
                        G.add_edge(game1, game2, weight=1)
            processed_users += 1
            if processed_users >= max_users:
                break
        if processed_users >= max_users:
            break

    print(f"Graph built with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")
    return G

