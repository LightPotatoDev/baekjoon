#include <string>
#include <iostream>
using namespace std;

class Person{
    string name;
    int day;
    int month;
    int year;
public:
    Person(string s, int d, int m, int y);
    Person(Person& p);
    Person();
    void print_name();
    void swap(Person& p);
    Person& operator = (const Person& p);
    int operator > (const Person& p);
    friend ostream& operator << (ostream& stream, const Person& p);
};
Person::Person(){
    name = "";
    day = 0;
    month = 0;
    year = 0;
}
Person::Person(Person& p){
    name = p.name;
    day = p.day;
    month = p.month;
    year = p.year;
}
Person::Person(string s, int d, int m, int y){
    name = s;
    day = d;
    month = m;
    year = y;
}
Person& Person::operator=(const Person& p){
    if (this == &p)
        return *this;
    name = p.name;
    day = p.day;
    month = p.month;
    year = p.year;

    return *this;
}
void Person::swap(Person& p){
    Person *temp = new Person;
    *temp = *this;
    *this = p;
    p = *temp;
}
int Person::operator>(const Person& d){
    if (year > d.year){
        return 1;
    }
    if (year < d.year){
        return 0;
    }
    if (month > d.month){
        return 1;
    }
    if (month < d.month){
        return 0;
    }
    if (day > d.day){
        return 1;
    }
    if (day < d.day){
        return 0;
    }
    return -1;
}
void Person::print_name(){
    cout << name;
}
ostream& operator << (ostream& s, const Person& p){
    s << p.name << " " << p.day << "/" << p.month << "/" << p.year;
    return s;
}

int main(){
    int n;
    cin >> n;
    cin.ignore();
    Person *p_array = new Person[n];

    for (int i=0; i<n; i++){
        string name;
        int d,m,y;
        cin >> name >> d >> m >> y;
        cin.ignore();
        p_array[i] = Person(name,d,m,y);
    }

    for (int i=0; i<n; i++){
        for (int j=i+1; j<n; j++){
            if (p_array[i] > p_array[j]){
                p_array[i].swap(p_array[j]);
            }
        }
    }

    p_array[n-1].print_name();
    cout << endl;
    p_array[0].print_name();

    return 0;
}