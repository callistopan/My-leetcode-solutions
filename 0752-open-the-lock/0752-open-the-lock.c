typedef struct Node {
    char *data;
    struct Node *prev;
    struct Node *next;
} Node;

typedef struct {
    Node *front;
    Node *rear;
} Queue;

Queue *createQueue() {
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->front = NULL;
    q->rear = NULL;
    return q;
}

void enqueue(Queue *q, char *s) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = strdup(s);
    newNode->next = NULL;
    if (q->rear == NULL) {
        q->front = newNode;
        q->rear = newNode;
    } else {
        q->rear->next = newNode;
        newNode->prev = q->rear;
        q->rear = newNode;
    }
}

char *dequeue(Queue *q) {
    if (q->front == NULL) {
        return NULL; // Queue is empty
    }
    Node *temp = q->front;
    char *result = temp->data;
    if (q->front == q->rear) {
        q->front = NULL;
        q->rear = NULL;
    } else {
        q->front = q->front->next;
        q->front->prev = NULL;
    }
    free(temp);
    return result;
}

int isEmpty(Queue *q) {
    return q->front == NULL;
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
        int size = 0;
        for (Node *temp = queue->front; temp != NULL; temp = temp->next) {
            size++;
        }
        for (int i = 0; i < size; i++) {
            char *current = dequeue(queue);
            if (strcmp(current, target) == 0) {
                while (!isEmpty(queue)) {
                    dequeue(queue); // Clear the remaining queue
                }
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
