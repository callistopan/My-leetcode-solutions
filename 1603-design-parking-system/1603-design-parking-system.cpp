class ParkingSystem {
public:

    // Parking limit of each type of car
    vector<int> limit;

    // Count of cars of each type
    vector<int> count;

    ParkingSystem(int big, int medium, int small) {

        // Parking limit of each type of car
        this->limit = {big, medium, small};

        // Count of cars of each type
        this->count = {0, 0, 0};
    }

    bool addCar(int carType) {

        // If space is available, allocate and return True
        if (this->count[carType - 1] < this->limit[carType - 1]) {
            this->count[carType - 1]++;
            return true;
        }

        // Else, return False
        return false;
    }
};