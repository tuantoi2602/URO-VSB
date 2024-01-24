#pragma once

#include <QtWidgets/QMainWindow>
#include "ui_QtGuiApplication02.h"

class QtGuiApplication02 : public QMainWindow
{
	Q_OBJECT

public:
	QtGuiApplication02(QWidget* parent = Q_NULLPTR);
	void CreateWidgets();

private:
	Ui::QtGuiApplication02Class ui;
};
