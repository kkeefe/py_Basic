#include <iostream>
#include "test.h"

// root
#include "TCanvas.h"
#include "TROOT.h"
#include "TStyle.h"
#include "TGraph.h"

using namespace std;

int main(int argc, char *argv[]) {

    double x[] = {1,2,3};
    double y[] = {1,4,9};
    foo a = foo();

    gROOT->SetBatch(true);
    TCanvas tc("", "", 500, 500);
    TGraph tg(3, x, y);
    tg.Draw();
    tc.Draw();
    tc.Print("main.png");

    y[2] = 8;

    std::cout << "ni hao fren!" << x[0] << std::endl;

    return 0;
}
