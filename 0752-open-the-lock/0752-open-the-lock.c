#define MAX_QUEUE_SIZE 10000
typedef struct {
    char *data[MAX_QUEUE_SIZE];
    int front, rear;
} Queue;

Queue *createQueue() {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = -1;
    q->rear = -1;
    return q;
}

void enqueue(Queue *q, char *s) {
    if ((q->rear + 1) % MAX_QUEUE_SIZE == q->front) {
        return; // Queue is full
    }
    if (q->front == -1) {
        q->front = 0;
    }
    q->rear = (q->rear + 1) % MAX_QUEUE_SIZE;
    q->data[q->rear] = strdup(s);
}

char *dequeue(Queue *q) {
    if (q->front == -1) {
        return NULL; // Queue is empty
    }
    char *result = q->data[q->front];
    if (q->front == q->rear) {
        q->front = -1;
        q->rear = -1;
    } else {
        q->front = (q->front + 1) % MAX_QUEUE_SIZE;
    }
    return result;
}

int isEmpty(Queue *q) {
    return q->front == -1;
}

int openLock(char **deadends, int deadendsSize, char *target) {
    if (target == NULL || deadends == NULL || deadendsSize == 0) {
        return -1;
    }

    char *start = "0000";
    if (strcmp(start, target) == 0) {
        return 0;
    }

    int *visited = (int *)calloc(10000, sizeof(int));
    for (int i = 0; i < deadendsSize; i++) {
        visited[atoi(deadends[i])] = 1;
    }
    if (visited[atoi(start)] == 1){
        return -1;
    }
    Queue *queue = createQueue();
    enqueue(queue, start);
    visited[atoi(start)] = 1;

    int level = 0;
    while (!isEmpty(queue)) {
        int size = (queue->rear - queue->front + MAX_QUEUE_SIZE + 1) % MAX_QUEUE_SIZE;
        for (int i = 0; i < size; i++) {
            char *current = dequeue(queue);
            if (strcmp(current, target) == 0) {
                free(queue);
                free(visited);
                return level;
            }
            for (int j = 0; j < 4; j++) {
                for (int k = -1; k <= 1; k += 2) {
                    char *next = strdup(current);
                    next[j] = (next[j] - '0' + k + 10) % 10 + '0';
                    if (!visited[atoi(next)]) {
                        enqueue(queue, next);
                        visited[atoi(next)] = 1;
                    }
                    free(next);
                }
            }
            free(current);
        }
        level++;
    }

    free(queue);
    free(visited);
    return -1;
}