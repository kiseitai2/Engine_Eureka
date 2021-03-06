#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "startup.h"
#include "data_base.h"
#include "globals.h"
#include <string>
#include <QFileDialog>
#include <QMessageBox>
#include <QThread>

MainWindow::MainWindow(QWidget *parent) :
  QMainWindow(parent),
  ui(new Ui::MainWindow)
{
  ui->setupUi(this);
  DOM = NULL;
  DOMWriter = NULL;
  //Once the file path was written to our global variables, open the file in read mode.
  std::string tmpPath = getProjectDirectory();
  tmpPath += getProjectName();
  DOM = new data_base(tmpPath.c_str());
  //Let's check if the file is empty! If it's empty, the file is a new project and the program has to be set up accordingly.
  if(DOM->SearchTermExists("this_is_a_project_file"))
    {
      //Let's parse the file and set the settings in the main window!
      setBasicSettings(getProjectDirectory(), getProjectName(), DOM->GetStrFromData("mod_loc").c_str());
      ui->leMod->setText(DOM->GetStrFromData("mod_loc").c_str());
      ui->leModInstall->setText(DOM->GetStrFromData("mod_install_loc").c_str());
      ui->leModName->setText(DOM->GetStrFromData("mod_name").c_str());
      ui->teModDescription->setPlainText(DOM->GetStrFromData("mod_description").c_str());
    }
  else
    {
      //File is empty or potentially corrupted, so we have to regenerate its contents with default settings.
      DOM->CreateNewFile(tmpPath.c_str());
      DOM->OpenFileForQuickWrite(tmpPath.c_str());
      /*Let's generate the data fields. I can generate the fields and give them values, but the code will be harder
      to read, so I will separate both processes! Also, some fields require further input from the user.
      */
      DOM->WriteValueAndFlush("proj_name = ;\n");
      DOM->WriteValueAndFlush("mod_loc = ;\n");
      DOM->WriteValueAndFlush("texture_count = ;\n");
      DOM->WriteValueAndFlush("sound_count = ;\n");
      DOM->WriteValueAndFlush("script_count = ;\n");
      DOM->WriteValueAndFlush("mod_install_loc = ;\n");
      DOM->WriteValueAndFlush("mod_description = ;\n");
      DOM->WriteValueAndFlush("mod_name = ;\n");
      //Let's validate the file by tagging it with the check field.
      DOM->WriteValueAndFlush("this_is_a_project_file = ;:EOF:");
      //Let's set the values!
      DOM->CloseFile();
      DOM->OpenFile(tmpPath.c_str(), false);
      DOM->WriteValue(removeCharFromStr('/', getProjectName().c_str()), "proj_name");
      DOM->WriteValue("", "mod_loc");
      std::string test = intToStr(0);
      DOM->WriteValue(test, "texture_count");
      DOM->WriteValue(intToStr(0), "sound_count");
      DOM->WriteValue(intToStr(0), "script_count");
      DOM->CloseFile();
      DOM->OpenFile(tmpPath.c_str());
    }
  open = new QFileDialog(this);
  DOMWriter = new data_base(tmpPath.c_str(), false);
  //QMessageBox::information(NULL,"test", DOMWriter->GetStrBuffer().c_str());
  DOMWriter->RestoreFileContents();
  changeProgramWorkingDirectory(getMODPath().c_str());
}

MainWindow::~MainWindow()
{
  delete ui;
}

void MainWindow::on_action_Exit_triggered()
{
    QApplication::quit();
}

void MainWindow::on_pbModBrowse_clicked()
{
    open->setFileMode(QFileDialog::Directory);
    ui->leMod->setText(open->getExistingDirectory(this, "Open Folder Dialog", "."));
}

void MainWindow::on_pBInstallBrowse_clicked()
{
  open->setFileMode(QFileDialog::Directory);
  ui->leModInstall->setText(open->getExistingDirectory(this, "Open Folder Dialog", "."));
}

void MainWindow::on_pbModSave_clicked()
{
  /*This method will save all settings for the mod into the project file (.pr).
   **/
  //Let's capture the string in the Mod's description.
    std::string tmp = ui->teModDescription->toPlainText().toStdString();
    std::string replacement = "";
    size_t index = 0;
    //Let's clean the string of new line and ; characters since they interfere with the file parser.
    while(searchChar('\n', tmp) && tmp != "")
      {
        //Let's swap new line characters for spaces!
        index = searchCharIndex('\n', tmp.c_str());
        tmp = removeCharFromStr('\n', tmp.c_str());
        tmp.insert(index, " ");
      }
    while(searchChar(';', tmp) && tmp != "")
      {
        //Let's swap ; characters for .!
        index = searchCharIndex(';', tmp.c_str());
        tmp = removeCharFromStr(';', tmp.c_str());
        replacement = tmp[index];
        replacement = ". ";
        replacement += capitalizeChar(tmp[index]);
        tmp.replace(index, 1, "");
        tmp.insert(index, replacement);
      }

    //We are ready to write settings to project file
    DOMWriter->WriteValue(tmp, "mod_description");
    DOMWriter->WriteValue(ui->leModName->text().toStdString(), "mod_name");
    DOMWriter->WriteValue(ui->leModInstall->text().toStdString(), "mod_install_loc");
    DOMWriter->WriteValue(ui->leMod->text().toStdString(), "mod_loc");
    DOM->RefreshFile();
}

void MainWindow::on_MainWindow_destroyed()
{
    DOM->CloseFile();
}



void MainWindow::on_pbTextureBrowse_clicked()
{
    open->setFileMode(QFileDialog::AnyFile);
    std::string tmp = open->getOpenFileName(NULL, "Select Texture","" ,"Textures (*.png *.tiff *.tex *.bmp *.jpg *.jpeg)").toStdString();
    tmp = tmp.replace(0, getMODPath().size(),"");
    ui->leTexturePath->setText(tmp.c_str());
}

void MainWindow::on_pbRegTexture_clicked()
{
  if(ui->leTexName->text() == "" || ui->leTexturePath->text() == "")
    {
      QMessageBox::critical(this, "Error!", "Error: Either the filename or the object name was not specified. Fill the missing fields and try again!");
    }
  else
    {
      data_base tmp;
      //First, we need to build the file path we need for this io operation!
      std::string path = "Textures/";
      path += ui->leTexName->text().toStdString();
      path += ".txt";
      //Now, we create a new and empty file!
      tmp.CreateNewFile(path.c_str());
      //Now, let's generate the data fields in the file!
      tmp.OpenFileForQuickWrite(path.c_str());
      tmp.WriteValueAndFlush("tex_texture = ;\n");
      tmp.WriteValueAndFlush("tex_frames = 1;\n");
      tmp.WriteValueAndFlush("tex_height = 0;\n");
      tmp.WriteValueAndFlush("tex_width = 0;\n");
      tmp.WriteValueAndFlush("tex_anim_counter = 0;\n");
      tmp.WriteValueAndFlush("tex_anim_num = 0;\n");
      tmp.WriteValueAndFlush("tex_time_on_frames = 0;\n");
      tmp.WriteValueAndFlush("tex_noloop = 0;\n");
      //Now, let's initialize the fields!
      tmp.CloseFile();
      tmp.OpenFile(path.c_str());
      tmp.WriteValue(ui->leTexturePath->text().toStdString(), "tex_texture");
      tmp.WriteValue(intToStr(ui->sbFrames->value()), "tex_frames");
      tmp.WriteValue(intToStr(ui->sbHeight->value()), "tex_height");
      tmp.WriteValue(intToStr(ui->sbWidth->value()), "tex_width");
      tmp.WriteValue(intToStr(ui->sbAnimCounter->value()), "tex_anim_counter");
      tmp.WriteValue(intToStr(ui->sbAnimNum->value()), "tex_anim_num");
      tmp.WriteValue(intToStr(ui->sbTimePerFrame->value()), "tex_time_on_frames");
      tmp.WriteValue(!ui->sbLoop->value(), "tex_noloop");
      tmp.CloseFile();
    }
}
