#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "mod_picker.h"


class Game;
class data_base;
class QFileDialog;
class QGraphicsScene;

namespace Ui {
  class MainWindow;
}

class MainWindow : public QMainWindow
{
  Q_OBJECT

public:
  explicit MainWindow(QWidget *parent = 0);
  ~MainWindow();

private slots:
  void on_action_Exit_triggered();

  void on_pbModBrowse_clicked();

  void on_pBInstallBrowse_clicked();

  void on_pbModSave_clicked();

  void on_MainWindow_destroyed();

  void on_pbTextureBrowse_clicked();

  void on_pbRegTexture_clicked();

private:
  Ui::MainWindow *ui;
  data_base* DOM, *DOMWriter;
  QFileDialog *open;
  QGraphicsScene* textPrev, *worldPrev;
  std::string modName, modDescription, modPath, modRootPath;
  Game* engine;

  //Methods
  bool modExists(size_t& index);
};

void build_new_directory_tree(const std::string source, const std::string &target);

#endif // MAINWINDOW_H
