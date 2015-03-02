#ifndef LEVEL_H_INCLUDED
#define LEVEL_H_INCLUDED
#include <SDL.h>
#include <list>
#include <string>
#include "BST.h"

//Forward declarations
class data_base;
class Trigger;
class ProgressBar;
class draw_base;
class textbox;
class sound_base;
class Timer;
class Pywrap;
class Game;

class Level
{
private:
    sound_base *lvlBackgroundMusic;
    size_t heroID;
    std::list<size_t> unitList;
    std::list<size_t> layerList;
    std::list<size_t> uiList;
    std::list<size_t> triggerList;
    std::list<size_t> moduleList;
    Game* sys;
    bool backgroundFixed;
    std::string mapName;
public:
    //Constructors and Destructors
    Level();
    ~Level();

    //Getters
    std::string& GetMapName() const;
    size_t GetHeroID() const;
    std::list<size_t>* GetLayerIDs() const;
    std::list<size_t>* GetUnitIDs() const;
    std::list<size_t>* GetUIIDs() const;
    std::list<size_t>* GetModuleIDs() const;
    std::list<size_t>* GetTriggerIDs() const;
};


#endif // LEVEL_H_INCLUDED
