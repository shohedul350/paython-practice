class Graph {
  constructor() {
    this.nodes = [];
    this.edges = {};
  }

  addNode(node) {
    this.nodes.push(node);
    this.edges[node] = [];
  }

  addEdge(node1, node2) {
    this.edges[node1].push(node2);
    this.edges[node2].push(node1); // Assuming undirected graph
  }

  isConnected(startNode, endNode) {
    const visited = new Set();
    
    this._dfs(startNode, visited);

    return visited.has(endNode);
  }

  _dfs(node, visited) {
    visited.add(node);

    const neighbors = this.edges[node];

    for (const neighbor of neighbors) {
      if (!visited.has(neighbor)) {
        this._dfs(neighbor, visited);
      }
    }
  }
}

// Example usage
const graph = new Graph();

graph.addNode(1);
graph.addNode(2);
graph.addNode(3);
graph.addNode(4);

graph.addEdge(1, 2);
graph.addEdge(2, 3);
graph.addEdge(3, 4);

const startNode = 1;
const endNode = 4;

const isConnect = graph.isConnected(startNode, endNode);

console.log(`Nodes ${startNode} and ${endNode} are connected: ${isConnect}`);
