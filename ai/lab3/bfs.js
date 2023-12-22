class Graph {
  constructor() {
    this.adjList = new Map();
  }

  addVertex(vertex) {
    this.adjList.set(vertex, []);
  }

  addEdge(vertex, neighbor) {
    this.adjList.get(vertex).push(neighbor);
    this.adjList.get(neighbor).push(vertex); // Assuming an undirected graph
  }

  bfs(start, destination) {
    // Create a queue for BFS and a visited array to keep track of visited vertices
    const queue = [];
    const visited = new Set();

    // Enqueue the starting vertex
    queue.push([start]);

    // Mark the starting vertex as visited
    visited.add(start);

    // BFS algorithm
    while (queue.length > 0) {
      const path = queue.shift();
      const currentVertex = path[path.length - 1];

      // Check if we reached the destination
      if (currentVertex === destination) {
        return path;
      }

      // Enqueue neighboring vertices
      const neighbors = this.adjList.get(currentVertex);
      for (const neighbor of neighbors) {
        if (!visited.has(neighbor)) {
          const newPath = [...path, neighbor];
          queue.push(newPath);
          visited.add(neighbor);
        }
      }
    }

    // If no path is found
    return null;
  }
}

// Example usage
const graph = new Graph();
graph.addVertex('A');
graph.addVertex('B');
graph.addVertex('C');
graph.addVertex('D');
graph.addEdge('A', 'B');
graph.addEdge('B', 'C');
graph.addEdge('C', 'D');

const path = graph.bfs('A', 'D');
console.log(path);