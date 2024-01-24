#include "qtguiapplication02.h"
#include <QGridLayout>
#include <QGroupBox>
#include <QLabel>
#include <QListWidget>
#include <QComboBox>
#include <QPushButton>
#include <QCheckBox>

QtGuiApplication02::QtGuiApplication02(QWidget* parent)
	: QMainWindow(parent)
{
	ui.setupUi(this);

	setWindowTitle("Configuration");

	CreateWidgets();
}

void QtGuiApplication02::CreateWidgets()
{

	QGridLayout* main = new QGridLayout();
	ui.centralWidget->setLayout(main);

	{
		QListWidget* menu = new QListWidget(this);
		menu->addItems({ "Layout", "Display", "  Icons", "  Font", " Color", " Tabstops", " Folder Tabs", " Custom columns", " View mode", "   Auto Switch Mode", " Language", "Operation", " Edit/View", " Copy/Delete", " Refresh", " Quick Search", " FTP", " Plugins", " Thumbnails", " Log file", " Ignore list", "Packer", " Zip packer", "Misc." });

		main->addWidget(menu, 0, 0, 12, 3, Qt::AlignLeft);
		QLabel* main2 = new QLabel("                                       ", this);
		main->addWidget(main2, 13, 0);
	}


	{
		QLabel* lblTitle = new QLabel("Color", this);
		main->addWidget(lblTitle, 0, 3);

		lblTitle->setFrameStyle(QFrame::Panel | QFrame::Sunken);
		lblTitle->setAlignment(Qt::AlignCenter);
		lblTitle->setMinimumHeight(25);

		QPalette palette = lblTitle->palette();
		palette.setColor(lblTitle->backgroundRole(), QColor("#99B4D1"));
		lblTitle->setPalette(palette);
		lblTitle->setAutoFillBackground(true);

	}

	{
		QGroupBox* color = new QGroupBox(this);
		color->setTitle("Color");
		main->addWidget(color, 1, 3, Qt::AlignTop);

		QLabel* lbl1 = new QLabel(this);
		lbl1->setText("Dark mode:");

		QComboBox* cmbModes = new QComboBox(this);
		cmbModes->addItems(QStringList({ "Always disabled", "Always enabled" }));

		QGridLayout* layout = new QGridLayout(this);
		color->setLayout(layout);

		layout->addWidget(lbl1, 0, 0, Qt::AlignLeft);
		layout->addWidget(cmbModes, 0, 1,1,14);

		QLabel* lbl2 = new QLabel(this);
		lbl2->setText("Font Color:");

		QComboBox* cmbModess = new QComboBox(this);
		cmbModess->addItems(QStringList({ "default" }));
		cmbModess->setEditable("True");
		QPushButton* btn01 = new QPushButton(">>", this);
		btn01->setFixedWidth(25);

		layout->addWidget(lbl2, 1, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess, 1, 1);
		layout->addWidget(btn01, 1, 2);

		QLabel* lbl3 = new QLabel(this);
		lbl3->setText("Background:");

		QComboBox* cmbModess3 = new QComboBox(this);
		cmbModess3->addItems(QStringList({ "default" }));
		cmbModess3->setEditable("True");
		QPushButton* btn02 = new QPushButton(">>", this);
		btn02->setFixedWidth(25);

		layout->addWidget(lbl3, 2, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess3, 2, 1);
		layout->addWidget(btn02, 2, 2);

		QLabel* lbl4 = new QLabel(this);
		lbl4->setText("Background 2:");

		QComboBox* cmbModess4 = new QComboBox(this);
		cmbModess4->addItems(QStringList({ "default" }));
		cmbModess4->setEditable("True");
		QPushButton* btn03 = new QPushButton(">>", this);
		btn03->setFixedWidth(25);

		layout->addWidget(lbl4, 3, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess4, 3, 1);
		layout->addWidget(btn03, 3, 2);

		QLabel* lbl5 = new QLabel(this);
		lbl5->setText("Mark color:");

		QComboBox* cmbModess5 = new QComboBox(this);
		cmbModess5->addItems(QStringList({ "default" }));
		cmbModess5->setEditable("True");
		QPushButton* btn04 = new QPushButton(">>", this);
		btn04->setFixedWidth(25);


		layout->addWidget(lbl5, 4, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess5, 4, 1);
		layout->addWidget(btn04, 4, 2);

		QLabel* lbl6 = new QLabel(this);
		lbl6->setText("Cursor color:");

		QComboBox* cmbModess6 = new QComboBox(this);
		cmbModess6->addItems(QStringList({ "default" }));
		cmbModess6->setEditable("True");
		QPushButton* btn05 = new QPushButton(">>", this);
		btn05->setFixedWidth(25);

		layout->addWidget(lbl6, 5, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess6, 5, 1);
		layout->addWidget(btn05, 5, 2);

		QLabel* lbl7 = new QLabel(this);
		lbl7->setText("Cursor font:");
		lbl7->setDisabled("True");
		QComboBox* cmbModess7 = new QComboBox(this);
		cmbModess7->addItems(QStringList({ "default" }));
		cmbModess7->setEditable("True");
		cmbModess7->setDisabled("True");
		QPushButton* btn06 = new QPushButton(">>", this);
		btn06->setDisabled("True");
		btn06->setFixedWidth(25);

		layout->addWidget(lbl7, 6, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess7, 6, 1);
		layout->addWidget(btn06, 6, 2);

		QLabel* lbl8 = new QLabel(this);
		lbl8->setText("Other:");

		QComboBox* cmbModess8 = new QComboBox(this);
		cmbModess8->addItems(QStringList({ "Lister" }));

		QComboBox* cmbModess81 = new QComboBox(this);
		cmbModess81->addItems(QStringList({ " " }));
		cmbModess81->setEditable("True");
		cmbModess81->setDisabled("True");
		QPushButton* btn062 = new QPushButton(">>", this);
		btn062->setFixedWidth(25);
		btn062->setDisabled("True");
		layout->addWidget(lbl8, 7, 0, Qt::AlignLeft);
		layout->addWidget(cmbModess8, 8, 0,1,2);
		layout->addWidget(cmbModess81, 8, 2,1,2);
		layout->addWidget(btn062, 8, 4);

		QCheckBox* chb1 = new QCheckBox(this);
		chb1->setChecked("True");
		chb1->setText("Use Windows theme for cursor");

		QCheckBox* chb2 = new QCheckBox(this);
		chb2->setText("Use inverted cursor");

		QCheckBox* chb3 = new QCheckBox(this);
		chb3->setText("Use inverted selection");

		QCheckBox* chb4 = new QCheckBox(this);
		chb4->setChecked("True");
		chb4->setText(" ");


		QPushButton* btn25 = new QPushButton("Define colors by file type...", this);
		btn25->setFixedWidth(290);
		
		layout->addWidget(chb1, 9, 0, Qt::AlignLeft);
		layout->addWidget(chb2, 10, 0, Qt::AlignLeft);
		layout->addWidget(chb3, 11, 0, Qt::AlignLeft);
		layout->addWidget(chb4, 12, 0,1,1,Qt::AlignLeft);
		layout->addWidget(btn25, 12, 0,1,3, Qt::AlignRight);
		
		QLabel* lbl21 = new QLabel(this);
		lbl21->setText("Example:");

		layout->addWidget(lbl21, 1, 3, Qt::AlignLeft);

		QLabel* lblEx = new QLabel("", this);


		lblEx->setFrameStyle(QFrame::Panel | QFrame::Sunken);
		lblEx->setAlignment(Qt::AlignCenter);
		lblEx->setFixedHeight(180);
		layout->addWidget(lblEx, 2,3,5,12);

		QListWidget* list1 = new QListWidget(this);
		list1->addItems({ "         Selected", "         Selected","            Text","            Text","          Cursor"," Selected + Cursor" });
		layout->addWidget(list1, 2, 3, 4, 9, Qt::AlignLeft);
	}

	{
		QFrame* buttons = new QFrame(this);
		main->addWidget(buttons, 14, 3, Qt::AlignBottom | Qt::AlignRight);

		QPushButton* btn1 = new QPushButton("OK", this);
		btn1->setFixedWidth(80);

		QPushButton* btn2 = new QPushButton("Cancel", this);
		btn2->setFixedWidth(80);

		QPushButton* btn3 = new QPushButton("Help", this);
		btn3->setFixedWidth(80);

		QPushButton* btn4 = new QPushButton("Apply", this);
		btn4->setFixedWidth(80);
		btn4->setDisabled("True");

		QHBoxLayout* layout = new QHBoxLayout(this);
		buttons->setLayout(layout);

		layout->addWidget(btn1);
		layout->addWidget(btn2);
		layout->addWidget(btn3);
		layout->addWidget(btn4);
	}

	
}
