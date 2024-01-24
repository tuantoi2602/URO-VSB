#include "QtGuiApplication02.h"
#include <QtWidgets/QApplication>

int main(int argc, char* argv[])
{
	QApplication a(argc, argv);
	QtGuiApplication02 w;
	w.show();
	return a.exec();
}
