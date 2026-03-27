int cmp(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    int i, moves;
    moves = 0;

    qsort(seats, seatsSize, sizeof(int), cmp);
    qsort(students, studentsSize, sizeof(int), cmp);

    for (i = 0; i < studentsSize; i++)
    {
        moves += (seats[i] > students[i]) ? seats[i] - students[i] : students[i] - seats[i];
    }

    return moves;
}