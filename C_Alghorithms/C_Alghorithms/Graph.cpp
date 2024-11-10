#include <iostream>
#include <vector>
#include <queue>
#include <utility>
#include <limits>
#include <cstdlib>
#include <ctime>
#include <cmath>

class Graph {
    private:
        int numNodes;
        std::vector<std::vector<std::pair<int, double>>> adjList;

    public:
        Graph(int nodes) : numNodes(nodes) {
            adjList.resize(numNodes);
        }

        void addEdge(int u, int v, double weight) {
            adjList[u].push_back({ v, weight });
            adjList[v].push_back({ u, weight });
        }

        // Random graph generation based on density and distance range
        void generateRandomGraph(double density, double minDistance, double maxDistance) {
            std::srand(std::time(0)); // Seed for random number generator
            for (int i = 0; i < numNodes; ++i) {
                for (int j = i + 1; j < numNodes; ++j) {
                    if (static_cast<double>(std::rand()) / RAND_MAX < density) {
                        double weight = minDistance + static_cast<double>(std::rand()) / RAND_MAX * (maxDistance - minDistance);
                        addEdge(i, j, weight);
                    }
                }
            }
        }

        // Dijkstra shortest paths from a source node
        std::vector<double> dijkstra(int source) {
            std::vector<double> distances(numNodes, std::numeric_limits<double>::infinity());
            distances[source] = 0.0;
            std::priority_queue<std::pair<double, int>, std::vector<std::pair<double, int>>, std::greater<>> pq;
            pq.push({ 0.0, source });

            while (!pq.empty()) {
                double dist = pq.top().first;
                int node = pq.top().second;
                pq.pop();

                if (dist > distances[node]) continue;

                for (const auto& neighbor : adjList[node]) {
                    int neighborNode = neighbor.first;
                    double weight = neighbor.second;
                    if (distances[node] + weight < distances[neighborNode]) {
                        distances[neighborNode] = distances[node] + weight;
                        pq.push({ distances[neighborNode], neighborNode });
                    }
                }
            }
            return distances;
        }

        // Calculate the average shortest path from node 1 to all other nodes
        double averageShortestPath(int source) {
            std::vector<double> distances = dijkstra(source);
            double sum = 0.0;
            int count = 0;

            for (int i = 0; i < numNodes; ++i) {
                if (i != source && distances[i] < std::numeric_limits<double>::infinity()) {
                    sum += distances[i];
                    ++count;
                }
            }

            return (count > 0) ? (sum / count) : 0.0;
        }

        ~Graph() { std::cout << "\n Destructor"; };
};

int main() {
    const int numNodes = 50;
    Graph graph(numNodes);

    double density1 = 0.2;
    double density2 = 0.4;
    double minDistance = 1.0;
    double maxDistance = 10.0;

    graph.generateRandomGraph(density1, minDistance, maxDistance);
    double avgPathDensity20 = graph.averageShortestPath(0);
    std::cout << "Average shortest path length for 20% density: " << avgPathDensity20 << std::endl;

    graph = Graph(numNodes); 
    graph.generateRandomGraph(density2, minDistance, maxDistance);
    double avgPathDensity40 = graph.averageShortestPath(0);
    std::cout << "Average shortest path length for 40% density: " << avgPathDensity40 << std::endl;

    return 0;
}
