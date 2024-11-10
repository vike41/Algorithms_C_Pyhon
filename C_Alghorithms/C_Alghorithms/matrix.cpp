// learing about matrix and function override
#include <iostream>
#include <vector>

using namespace std;


class Matrix {

    private:
        int rows;
        int collums;
        std::vector<std::vector<int>> data;

    public:
        Matrix(int r, int c) : rows(r), collums(c), data(r, std::vector<int>(c, 0)) {}
        
        void setElement(int r, int c, int value) {
            if (r >= 0 && r < rows && c >= 0 && c < collums)
            {
                data[r][c] = value;
            }
            else
            {
                std::cerr << "Index out of bounds\n";
            }
        }


        int getElement(int r, int c) const {
            if (r >= 0 && r < rows && c >= 0 && c < collums)
            {
                return data[r][c];
            }
            else
            {
                std::cerr << "Index out of bounds\n";
                return -1;
            }
        }

        friend std::ostream& operator <<(std::ostream& os, const Matrix& obj) {
            for (const auto& row : obj.data) { // Access private member `data`
                for (int elem : row) {
                    os << elem << " ";
                }
                os << "\n";
            }
            return os;
        }

        ~Matrix() { cout << "\n Destructor"; };
};



int main() {
    Matrix matrix(3, 3);
    matrix.setElement(0, 0, 1);
    matrix.setElement(1, 1, 2);
    matrix.setElement(2, 2, 3);
    cout << matrix << endl;
    
    return 0;
}