import matplotlib.pyplot as plt
import networkx as nx
import pandas as pd
from vkapi.friends import get_friends, get_mutual
from vkapi.friends import MutualFriends, get_friends, get_mutual


def ego_network(
@@ -17,46 +17,46 @@ def ego_network(
    :param user_id: Идентификатор пользователя, для которого строится граф друзей.
    :param friends: Идентификаторы друзей, между которыми устанавливаются связи.
    """
    graf = []
    script = []
    if friends is None:
        friends_fields = get_friends(user_id, fields=["nickname", "is_closed, deactivate"]).items  # type: ignore
        fields: tp.List[tp.Dict[str, tp.Any]] = get_friends(user_id, fields=["nickname", "is_closed, deactivate"]).items  # type: ignore
        friends = [
            friend["id"]  # type: ignore
            for friend in friends_fields
            if not friend.get("deactivate") and not friend.get("is_closed")  # type: ignore
            friend["id"]
            for friend in fields
            if not (friend.get("deactivate") or friend.get("is_closed"))
        ]
    mutuals = get_mutual(user_id, target_uids=friends)
    for mutual in mutuals:
        if isinstance(mutual, dict):
            for common in mutual["common_friends"]:
                graf.append((mutual["id"], common))
    return graf
        mut = tp.cast(MutualFriends, mutual)
        for common in mut["common_friends"]:
            script.append((mut["id"], common))
    return script


def plot_ego_network(net: tp.List[tp.Tuple[int, int]]) -> None:
    graph = nx.Graph()
    graph.add_edges_from(net)
    layout = nx.spring_layout(graph)
    nx.draw(graph, layout, node_size=10, node_color="black", alpha=0.5)
    script = nx.Graph()
    script.add_edges_from(net)
    layout = nx.spring_layout(script)
    nx.draw(script, layout, node_size=10, node_color="black", alpha=0.5)
    plt.title("Ego Network", size=15)
    plt.show()


def plot_communities(net: tp.List[tp.Tuple[int, int]]) -> None:
    graph = nx.Graph()
    graph.add_edges_from(net)
    layout = nx.spring_layout(graph)
    partition = community_louvain.best_partition(graph)
    nx.draw(graph, layout, node_size=25, node_color=list(partition.values()), alpha=0.8)
    script = nx.Graph()
    script.add_edges_from(net)
    layout = nx.spring_layout(script)
    partition = community_louvain.best_partition(script)
    nx.draw(script, layout, node_size=25, node_color=list(partition.values()), alpha=0.8)
    plt.title("Ego Network", size=15)
    plt.show()


def get_communities(net: tp.List[tp.Tuple[int, int]]) -> tp.Dict[int, tp.List[int]]:
    communities = defaultdict(list)
    graph = nx.Graph()
    graph.add_edges_from(net)
    partition = community_louvain.best_partition(graph)
    script = nx.Graph()
    script.add_edges_from(net)
    partition = community_louvain.best_partition(script)
    for uid, cluster in partition.items():
        communities[cluster].append(uid)
    return communities
    
