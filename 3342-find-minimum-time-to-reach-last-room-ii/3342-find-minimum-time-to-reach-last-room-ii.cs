using System;
using System.Collections.Generic;

public class Solution {
    public int MinTimeToReach(int[][] moveTime) {
        int numRows = moveTime.Length;
        int numCols = moveTime[0].Length;

        // Priority queue to store (current_time, x, y, z)
        var minHeap = new SortedSet<(int time, int x, int y, int z)>(Comparer<(int time, int x, int y, int z)>.Create((a, b) => 
            a.time == b.time ? (a.x == b.x ? (a.y == b.y ? a.z.CompareTo(b.z) : a.y.CompareTo(b.y)) : a.x.CompareTo(b.x)) : a.time.CompareTo(b.time)
        ));
        minHeap.Add((0, 0, 0, 0));

        // 3D array to store the minimum arrival time for each cell and state
        var arrivalTime = new int[2, numRows, numCols];
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < numRows; j++) {
                for (int k = 0; k < numCols; k++) {
                    arrivalTime[i, j, k] = int.MaxValue;
                }
            }
        }
        arrivalTime[0, 0, 0] = 0;

        // Directions for adjacent rooms (down, up, right, left)
        int[][] directions = new int[][] {
            new int[] {1, 0},  // Down
            new int[] {-1, 0}, // Up
            new int[] {0, 1},  // Right
            new int[] {0, -1}  // Left
        };

        while (minHeap.Count > 0) {
            var (currentTime, x, y, k) = minHeap.Min;
            minHeap.Remove(minHeap.Min);

            // If we reached the target room (numRows - 1, numCols - 1)
            if (x == numRows - 1 && y == numCols - 1) {
                return currentTime;
            }

            // Explore adjacent rooms
            foreach (var direction in directions) {
                int newX = x + direction[0];
                int newY = y + direction[1];
                int newZ = k ^ 1;  // Toggle the z state (k)

                if (newX >= 0 && newX < numRows && newY >= 0 && newY < numCols) {
                    int waitTime = Math.Max(moveTime[newX][newY] - currentTime, 0);
                    int newArrivalTime = currentTime + 1 + waitTime + k;

                    // Only add to the queue if we found a better arrival time
                    if (newArrivalTime < arrivalTime[newZ, newX, newY]) {
                        arrivalTime[newZ, newX, newY] = newArrivalTime;
                        minHeap.Add((newArrivalTime, newX, newY, newZ));
                    }
                }
            }
        }

        return -1; // Return -1 if the target room is unreachable
    }
}
