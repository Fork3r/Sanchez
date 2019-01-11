#include <QCoreApplication>
#include <QTextStream>
#include <QFile>

int main(int argc, char *argv[])
{
    while (1) {
     QTextStream qtin(stdin);
     QString test;
        test = qtin.readLine();
    }
}
