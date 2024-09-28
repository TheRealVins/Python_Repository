#include <iostream>
using namespace std;


void quizGame () {
    string questions[] = {{"At what TH Level does Barbarian King appear?"},
                          {"Does the Queen unlocks in TH9?"},
                          {"At TH10, what defensive structure do you unlock?"},
                          {"At TH15, what is the maximum level of the King and Queen?"},
                          {"At what TH Level can you unlock Air Defense?"}};

    string choices [][4] = {{"A. TH9", "B. TH7", "C. TH11", "D. TH4"},
                            {"A. True", "B. False", "C. I don't know"},
                            {"A. Air Defense", "B. Cannon", "C. Archer Tower", "D. Inferno Tower"},
                            {"A. 85", "B. 95", "C. 90", "D. 100"},
                            {"A. TH9", "B. TH7", "C. TH11", "D. TH4"}};

    char answerKey [] = {'B', 'A', 'D', 'C', 'D'};

    int size = sizeof(questions)/sizeof(string);
    char answer;
    int score;

    for(int i = 0; i < size; i++) {
        cout << "__\n";
        cout << questions[i] << endl;
        cout << "__\n";

        for(int j = 0; j < sizeof(choices[i])/sizeof(choices[i][0]); j++) {
            cout << choices [i][j] << endl;
        }

        cout << "Answer: ";
        cin >> answer;
        answer = toupper(answer);

        if(answer == answerKey[i]) {
            cout <<"Correct!\n";
            score++;
        } else {
            cout <<"Wrong!\n";
            cout <<"Answer: " << answerKey[i] << endl;
        }
        system("cls");
    }

        cout <<"You scored: " << score << "/" << size << "!\n";
}



int main () {

    cout <<"**\n";
    cout <<"CLASH OF CLANS KNOWLEDGE CHECK!\n";
    cout <<"**\n";

    quizGame();

    return 0;
}