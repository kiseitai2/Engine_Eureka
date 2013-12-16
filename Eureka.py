# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_Eureka', [dirname(__file__)])
        except ImportError:
            import _Eureka
            return _Eureka
        if fp is not None:
            try:
                _mod = imp.load_module('_Eureka', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _Eureka = swig_import_helper()
    del swig_import_helper
else:
    import _Eureka
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


class math_VECTOR(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, math_VECTOR, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, math_VECTOR, name)
    __repr__ = _swig_repr
    __swig_setmethods__["endX"] = _Eureka.math_VECTOR_endX_set
    __swig_getmethods__["endX"] = _Eureka.math_VECTOR_endX_get
    if _newclass:endX = _swig_property(_Eureka.math_VECTOR_endX_get, _Eureka.math_VECTOR_endX_set)
    __swig_setmethods__["endY"] = _Eureka.math_VECTOR_endY_set
    __swig_getmethods__["endY"] = _Eureka.math_VECTOR_endY_get
    if _newclass:endY = _swig_property(_Eureka.math_VECTOR_endY_get, _Eureka.math_VECTOR_endY_set)
    __swig_setmethods__["direction"] = _Eureka.math_VECTOR_direction_set
    __swig_getmethods__["direction"] = _Eureka.math_VECTOR_direction_get
    if _newclass:direction = _swig_property(_Eureka.math_VECTOR_direction_get, _Eureka.math_VECTOR_direction_set)
    __swig_setmethods__["magnitude"] = _Eureka.math_VECTOR_magnitude_set
    __swig_getmethods__["magnitude"] = _Eureka.math_VECTOR_magnitude_get
    if _newclass:magnitude = _swig_property(_Eureka.math_VECTOR_magnitude_get, _Eureka.math_VECTOR_magnitude_set)
    def __init__(self): 
        this = _Eureka.new_math_VECTOR()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_math_VECTOR
    __del__ = lambda self : None;
math_VECTOR_swigregister = _Eureka.math_VECTOR_swigregister
math_VECTOR_swigregister(math_VECTOR)

class math_point(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, math_point, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, math_point, name)
    __repr__ = _swig_repr
    __swig_setmethods__["X"] = _Eureka.math_point_X_set
    __swig_getmethods__["X"] = _Eureka.math_point_X_get
    if _newclass:X = _swig_property(_Eureka.math_point_X_get, _Eureka.math_point_X_set)
    __swig_setmethods__["Y"] = _Eureka.math_point_Y_set
    __swig_getmethods__["Y"] = _Eureka.math_point_Y_get
    if _newclass:Y = _swig_property(_Eureka.math_point_Y_get, _Eureka.math_point_Y_set)
    def __init__(self): 
        this = _Eureka.new_math_point()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_math_point
    __del__ = lambda self : None;
math_point_swigregister = _Eureka.math_point_swigregister
math_point_swigregister(math_point)

class Physics(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Physics, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Physics, name)
    __repr__ = _swig_repr
    def NewtonianForce(self, axis='x'): return _Eureka.Physics_NewtonianForce(self, axis)
    def Relativity(self, axis='x'): return _Eureka.Physics_Relativity(self, axis)
    def rel_NewtonianForce(self, axis='x'): return _Eureka.Physics_rel_NewtonianForce(self, axis)
    def rel_CalculateForceB(self, *args): return _Eureka.Physics_rel_CalculateForceB(self, *args)
    def Impulse(self, *args): return _Eureka.Physics_Impulse(self, *args)
    def Friction(self, *args): return _Eureka.Physics_Friction(self, *args)
    def Update_Velocity(self, *args): return _Eureka.Physics_Update_Velocity(self, *args)
    def UpdateForce(self, *args): return _Eureka.Physics_UpdateForce(self, *args)
    def Update_Acceleration(self): return _Eureka.Physics_Update_Acceleration(self)
    def math_CalculateDirectionDegrees(self, *args): return _Eureka.Physics_math_CalculateDirectionDegrees(self, *args)
    def GetDistance(self, *args): return _Eureka.Physics_GetDistance(self, *args)
    def GetLoc(self): return _Eureka.Physics_GetLoc(self)
    def GetMU(self): return _Eureka.Physics_GetMU(self)
    def GetMass(self): return _Eureka.Physics_GetMass(self)
    def GetB2DDirection(self): return _Eureka.Physics_GetB2DDirection(self)
    def GetBMagnitude(self): return _Eureka.Physics_GetBMagnitude(self)
    def GetGravity(self): return _Eureka.Physics_GetGravity(self)
    def GetVelocity(self, *args): return _Eureka.Physics_GetVelocity(self, *args)
    def GetElasticity(self): return _Eureka.Physics_GetElasticity(self)
    def math_CalculateForceFromChargedParticles(self, *args): return _Eureka.Physics_math_CalculateForceFromChargedParticles(self, *args)
    def math_CalculateEField(self, *args): return _Eureka.Physics_math_CalculateEField(self, *args)
    def math_Sign(self, *args): return _Eureka.Physics_math_Sign(self, *args)
    def math_CalculateMomentum(self, *args): return _Eureka.Physics_math_CalculateMomentum(self, *args)
    def math_CalculateForceFromMagneticField(self, *args): return _Eureka.Physics_math_CalculateForceFromMagneticField(self, *args)
    def GetForceCount(self, *args): return _Eureka.Physics_GetForceCount(self, *args)
    def isUnmovable(self): return _Eureka.Physics_isUnmovable(self)
    def SetForceCount(self, *args): return _Eureka.Physics_SetForceCount(self, *args)
    def SetVelocity(self, *args): return _Eureka.Physics_SetVelocity(self, *args)
    def AddForce(self, *args): return _Eureka.Physics_AddForce(self, *args)
    def __init__(self, location=""): 
        this = _Eureka.new_Physics(location)
        try: self.this.append(this)
        except: self.this = this
    def Update_Position(self, *args): return _Eureka.Physics_Update_Position(self, *args)
    def ChangePlanetGravitationalConstant(self, *args): return _Eureka.Physics_ChangePlanetGravitationalConstant(self, *args)
    def Load_Physics(self, *args): return _Eureka.Physics_Load_Physics(self, *args)
    def GetCharge(self): return _Eureka.Physics_GetCharge(self)
    __swig_destroy__ = _Eureka.delete_Physics
    __del__ = lambda self : None;
Physics_swigregister = _Eureka.Physics_swigregister
Physics_swigregister(Physics)


def CalculateDistance(*args):
  return _Eureka.CalculateDistance(*args)
CalculateDistance = _Eureka.CalculateDistance
ERROR = _Eureka.ERROR
class data_base(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, data_base, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, data_base, name)
    __repr__ = _swig_repr
    def __init__(self, location="", read=True): 
        this = _Eureka.new_data_base(location, read)
        try: self.this.append(this)
        except: self.this = this
    def GetStrBuffer(self): return _Eureka.data_base_GetStrBuffer(self)
    def GetValueFromData(self, *args): return _Eureka.data_base_GetValueFromData(self, *args)
    def GetStrFromData(self, *args): return _Eureka.data_base_GetStrFromData(self, *args)
    def GetIntFromData(self, *args): return _Eureka.data_base_GetIntFromData(self, *args)
    def GetValueFromDataWithLine(self, *args): return _Eureka.data_base_GetValueFromDataWithLine(self, *args)
    def GetStrFromDataWithLine(self, *args): return _Eureka.data_base_GetStrFromDataWithLine(self, *args)
    def GetStateOfInternalBuffer(self): return _Eureka.data_base_GetStateOfInternalBuffer(self)
    def OpenFile(self, *args): return _Eureka.data_base_OpenFile(self, *args)
    def OpenFileForQuickWrite(self, *args): return _Eureka.data_base_OpenFileForQuickWrite(self, *args)
    def CloseFile(self, streamsToClose="all"): return _Eureka.data_base_CloseFile(self, streamsToClose)
    def GetMode(self): return _Eureka.data_base_GetMode(self)
    def WriteValue(self, *args): return _Eureka.data_base_WriteValue(self, *args)
    def WriteValueWithLineIndex(self, *args): return _Eureka.data_base_WriteValueWithLineIndex(self, *args)
    def WriteValueAndFlush(self, *args): return _Eureka.data_base_WriteValueAndFlush(self, *args)
    def GetLineCount(self): return _Eureka.data_base_GetLineCount(self)
    def GetNumInstances(self, *args): return _Eureka.data_base_GetNumInstances(self, *args)
    def SearchTermExists(self, *args): return _Eureka.data_base_SearchTermExists(self, *args)
    __swig_destroy__ = _Eureka.delete_data_base
    __del__ = lambda self : None;
data_base_swigregister = _Eureka.data_base_swigregister
data_base_swigregister(data_base)

class draw_base(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, draw_base, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, draw_base, name)
    __repr__ = _swig_repr
    def Load_Texture(self, *args): return _Eureka.draw_base_Load_Texture(self, *args)
    def apply_surface(self, *args): return _Eureka.draw_base_apply_surface(self, *args)
    def GetHeightOfMainRect(self): return _Eureka.draw_base_GetHeightOfMainRect(self)
    def GetWidthOfMainRect(self): return _Eureka.draw_base_GetWidthOfMainRect(self)
    def GetAnimCounter(self): return _Eureka.draw_base_GetAnimCounter(self)
    def GetDOM(self): return _Eureka.draw_base_GetDOM(self)
    def isNoLoop(self): return _Eureka.draw_base_isNoLoop(self)
    def GetTexture(self): return _Eureka.draw_base_GetTexture(self)
    def setColor(self, *args): return _Eureka.draw_base_setColor(self, *args)
    def setBlendMode(self, *args): return _Eureka.draw_base_setBlendMode(self, *args)
    def setAlpha(self, *args): return _Eureka.draw_base_setAlpha(self, *args)
    def ClearTexture(self): return _Eureka.draw_base_ClearTexture(self)
    def SetTextureFromPointer(self, *args): return _Eureka.draw_base_SetTextureFromPointer(self, *args)
    def __init__(self): 
        this = _Eureka.new_draw_base()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_draw_base
    __del__ = lambda self : None;
draw_base_swigregister = _Eureka.draw_base_swigregister
draw_base_swigregister(draw_base)


def apply_surface(*args):
  return _Eureka.apply_surface(*args)
apply_surface = _Eureka.apply_surface

def LoadTexture(*args):
  return _Eureka.LoadTexture(*args)
LoadTexture = _Eureka.LoadTexture
class UI(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, UI, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, UI, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_UI(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_UI
    __del__ = lambda self : None;
    def isVisible(self): return _Eureka.UI_isVisible(self)
    def toggleVisibility(self): return _Eureka.UI_toggleVisibility(self)
    def Update(self): return _Eureka.UI_Update(self)
    def ProcessEvents(self, *args): return _Eureka.UI_ProcessEvents(self, *args)
    def AddNumToPBar(self, *args): return _Eureka.UI_AddNumToPBar(self, *args)
    def Draw(self): return _Eureka.UI_Draw(self)
UI_swigregister = _Eureka.UI_swigregister
UI_swigregister(UI)

class Unit(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Unit, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Unit, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_Unit(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_Unit
    __del__ = lambda self : None;
    def isMelee(self): return _Eureka.Unit_isMelee(self)
    def MoveAI(self): return _Eureka.Unit_MoveAI(self)
    def LoadAI(self, *args): return _Eureka.Unit_LoadAI(self, *args)
    def AttackAI(self, *args): return _Eureka.Unit_AttackAI(self, *args)
    def ExecuteAI(self, *args): return _Eureka.Unit_ExecuteAI(self, *args)
    def MoveTowardsAI(self, *args): return _Eureka.Unit_MoveTowardsAI(self, *args)
    def SetTimer(self, *args): return _Eureka.Unit_SetTimer(self, *args)
    def Update_NewTime(self): return _Eureka.Unit_Update_NewTime(self)
    def Update_OldTime(self): return _Eureka.Unit_Update_OldTime(self)
    def GetTimeChange(self): return _Eureka.Unit_GetTimeChange(self)
    def GetName(self): return _Eureka.Unit_GetName(self)
    def GetVRange(self): return _Eureka.Unit_GetVRange(self)
    def GetPhysics(self): return _Eureka.Unit_GetPhysics(self)
    def GetDefaultDrawObject(self): return _Eureka.Unit_GetDefaultDrawObject(self)
    def ToggleMelee(self): return _Eureka.Unit_ToggleMelee(self)
    def GetHP(self): return _Eureka.Unit_GetHP(self)
    def GetAD(self): return _Eureka.Unit_GetAD(self)
    def GetAP(self): return _Eureka.Unit_GetAP(self)
    def GetAttackSpeed(self): return _Eureka.Unit_GetAttackSpeed(self)
    def GetRange(self): return _Eureka.Unit_GetRange(self)
    def GetVisionRange(self): return _Eureka.Unit_GetVisionRange(self)
    def GetMovementSpeed(self): return _Eureka.Unit_GetMovementSpeed(self)
    def SetHP(self, *args): return _Eureka.Unit_SetHP(self, *args)
    def SetAD(self, *args): return _Eureka.Unit_SetAD(self, *args)
    def SetAP(self, *args): return _Eureka.Unit_SetAP(self, *args)
    def SetAttackSpeed(self, *args): return _Eureka.Unit_SetAttackSpeed(self, *args)
    def SetRange(self, *args): return _Eureka.Unit_SetRange(self, *args)
    def SetVisionRange(self, *args): return _Eureka.Unit_SetVisionRange(self, *args)
    def SetMovementSpeed(self, *args): return _Eureka.Unit_SetMovementSpeed(self, *args)
    def GetDeath(self): return _Eureka.Unit_GetDeath(self)
    def ToggleDeath(self): return _Eureka.Unit_ToggleDeath(self)
    def UpdateAssets(self, *args): return _Eureka.Unit_UpdateAssets(self, *args)
    def AddBuff(self, *args): return _Eureka.Unit_AddBuff(self, *args)
    def RemoveBuff(self, *args): return _Eureka.Unit_RemoveBuff(self, *args)
    def ApplyBuffs(self): return _Eureka.Unit_ApplyBuffs(self)
    def isColliding(self, *args): return _Eureka.Unit_isColliding(self, *args)
    def Update_Physics(self, *args): return _Eureka.Unit_Update_Physics(self, *args)
    def OnCollision(self, *args): return _Eureka.Unit_OnCollision(self, *args)
    def LoadScript(self, *args): return _Eureka.Unit_LoadScript(self, *args)
    def ProcessKeyEvent(self, *args): return _Eureka.Unit_ProcessKeyEvent(self, *args)
    def LoadKeyScript(self, *args): return _Eureka.Unit_LoadKeyScript(self, *args)
    def LoadKeyBindings(self, *args): return _Eureka.Unit_LoadKeyBindings(self, *args)
    def ProcessMouseMovement(self, *args): return _Eureka.Unit_ProcessMouseMovement(self, *args)
    def ProcessMouseKey(self, *args): return _Eureka.Unit_ProcessMouseKey(self, *args)
Unit_swigregister = _Eureka.Unit_swigregister
Unit_swigregister(Unit)

class textbox(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, textbox, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, textbox, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_textbox(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_textbox
    __del__ = lambda self : None;
    def Draw(self, *args): return _Eureka.textbox_Draw(self, *args)
    def SetLoc(self, *args): return _Eureka.textbox_SetLoc(self, *args)
    def GetType(self): return _Eureka.textbox_GetType(self)
    def GetDeath(self): return _Eureka.textbox_GetDeath(self)
    def GetBlitOrder(self): return _Eureka.textbox_GetBlitOrder(self)
    def ToggleDeath(self): return _Eureka.textbox_ToggleDeath(self)
    def SetOwner(self, *args): return _Eureka.textbox_SetOwner(self, *args)
    def GetOwner(self): return _Eureka.textbox_GetOwner(self)
    def GetText(self): return _Eureka.textbox_GetText(self)
    def GetLoc(self): return _Eureka.textbox_GetLoc(self)
    def GetDOM(self): return _Eureka.textbox_GetDOM(self)
    def GetDrawObject(self): return _Eureka.textbox_GetDrawObject(self)
    def isInside(self, *args): return _Eureka.textbox_isInside(self, *args)
    def changeMsg(self, *args): return _Eureka.textbox_changeMsg(self, *args)
    def changeFont(self, *args): return _Eureka.textbox_changeFont(self, *args)
    def changeColor(self, *args): return _Eureka.textbox_changeColor(self, *args)
    def changeFontSize(self, *args): return _Eureka.textbox_changeFontSize(self, *args)
    def isWritable(self): return _Eureka.textbox_isWritable(self)
textbox_swigregister = _Eureka.textbox_swigregister
textbox_swigregister(textbox)

class Button(textbox):
    __swig_setmethods__ = {}
    for _s in [textbox]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, Button, name, value)
    __swig_getmethods__ = {}
    for _s in [textbox]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, Button, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_Button(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_Button
    __del__ = lambda self : None;
    def ProcessMouseLoc(self, *args): return _Eureka.Button_ProcessMouseLoc(self, *args)
    def MouseClick(self, *args): return _Eureka.Button_MouseClick(self, *args)
Button_swigregister = _Eureka.Button_swigregister
Button_swigregister(Button)

class Trigger(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Trigger, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Trigger, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_Trigger(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_Trigger
    __del__ = lambda self : None;
    def GetID(self): return _Eureka.Trigger_GetID(self)
    def SetID(self, *args): return _Eureka.Trigger_SetID(self, *args)
    def isUnitOnTrigger(self, *args): return _Eureka.Trigger_isUnitOnTrigger(self, *args)
    def ConsumeTrigger(self, *args): return _Eureka.Trigger_ConsumeTrigger(self, *args)
    def GetDeath(self): return _Eureka.Trigger_GetDeath(self)
    def ToggleDeath(self): return _Eureka.Trigger_ToggleDeath(self)
Trigger_swigregister = _Eureka.Trigger_swigregister
Trigger_swigregister(Trigger)

class sound_base(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, sound_base, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, sound_base, name)
    __repr__ = _swig_repr
    def Load_Sound(self, *args): return _Eureka.sound_base_Load_Sound(self, *args)
    def Play(self, loops=0): return _Eureka.sound_base_Play(self, loops)
    def Pause(self): return _Eureka.sound_base_Pause(self)
    def Stop(self): return _Eureka.sound_base_Stop(self)
    def isPlaying(self): return _Eureka.sound_base_isPlaying(self)
    def PlayEffect(self, *args): return _Eureka.sound_base_PlayEffect(self, *args)
    def isLoopingEffect(self): return _Eureka.sound_base_isLoopingEffect(self)
    def FadeOut(self, *args): return _Eureka.sound_base_FadeOut(self, *args)
    def SetVol(self, *args): return _Eureka.sound_base_SetVol(self, *args)
    def SoundType(self): return _Eureka.sound_base_SoundType(self)
    def SetPoint(self): return _Eureka.sound_base_SetPoint(self)
    def Update_Sound_Distance(self, *args): return _Eureka.sound_base_Update_Sound_Distance(self, *args)
    def Update_Sound_Position(self, *args): return _Eureka.sound_base_Update_Sound_Position(self, *args)
    __swig_destroy__ = _Eureka.delete_sound_base
    __del__ = lambda self : None;
    def __init__(self, random_blob=False): 
        this = _Eureka.new_sound_base(random_blob)
        try: self.this.append(this)
        except: self.this = this
sound_base_swigregister = _Eureka.sound_base_swigregister
sound_base_swigregister(sound_base)

class Timer(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Timer, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Timer, name)
    __repr__ = _swig_repr
    def __init__(self): 
        this = _Eureka.new_Timer()
        try: self.this.append(this)
        except: self.this = this
    def start(self): return _Eureka.Timer_start(self)
    def stop(self): return _Eureka.Timer_stop(self)
    def pause(self): return _Eureka.Timer_pause(self)
    def unpause(self): return _Eureka.Timer_unpause(self)
    def get_ticks(self): return _Eureka.Timer_get_ticks(self)
    def is_started(self): return _Eureka.Timer_is_started(self)
    def is_paused(self): return _Eureka.Timer_is_paused(self)
    __swig_destroy__ = _Eureka.delete_Timer
    __del__ = lambda self : None;
Timer_swigregister = _Eureka.Timer_swigregister
Timer_swigregister(Timer)

class ProgressBar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ProgressBar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ProgressBar, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_ProgressBar(*args)
        try: self.this.append(this)
        except: self.this = this
    def Update(self, *args): return _Eureka.ProgressBar_Update(self, *args)
    def Draw(self, *args): return _Eureka.ProgressBar_Draw(self, *args)
    def SetRectangleDimensions(self, *args): return _Eureka.ProgressBar_SetRectangleDimensions(self, *args)
    def GetRectangleHeight(self): return _Eureka.ProgressBar_GetRectangleHeight(self)
    def GetRectangleWidth(self): return _Eureka.ProgressBar_GetRectangleWidth(self)
    __swig_destroy__ = _Eureka.delete_ProgressBar
    __del__ = lambda self : None;
ProgressBar_swigregister = _Eureka.ProgressBar_swigregister
ProgressBar_swigregister(ProgressBar)


def init():
  return _Eureka.init()
init = _Eureka.init

def FrameCapper():
  return _Eureka.FrameCapper()
FrameCapper = _Eureka.FrameCapper

def SpawnUnit(*args):
  return _Eureka.SpawnUnit(*args)
SpawnUnit = _Eureka.SpawnUnit

def FindNearbyUnit(*args):
  return _Eureka.FindNearbyUnit(*args)
FindNearbyUnit = _Eureka.FindNearbyUnit

def FindUnitByName(*args):
  return _Eureka.FindUnitByName(*args)
FindUnitByName = _Eureka.FindUnitByName

def loadGameConstants():
  return _Eureka.loadGameConstants()
loadGameConstants = _Eureka.loadGameConstants

def GetRenderer():
  return _Eureka.GetRenderer()
GetRenderer = _Eureka.GetRenderer
class pChar(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pChar, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pChar, name)
    __repr__ = _swig_repr
    __swig_setmethods__["pBuffer"] = _Eureka.pChar_pBuffer_set
    __swig_getmethods__["pBuffer"] = _Eureka.pChar_pBuffer_get
    if _newclass:pBuffer = _swig_property(_Eureka.pChar_pBuffer_get, _Eureka.pChar_pBuffer_set)
    __swig_setmethods__["size"] = _Eureka.pChar_size_set
    __swig_getmethods__["size"] = _Eureka.pChar_size_get
    if _newclass:size = _swig_property(_Eureka.pChar_size_get, _Eureka.pChar_size_set)
    def __init__(self): 
        this = _Eureka.new_pChar()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _Eureka.delete_pChar
    __del__ = lambda self : None;
pChar_swigregister = _Eureka.pChar_swigregister
pChar_swigregister(pChar)


def charToInt(*args):
  return _Eureka.charToInt(*args)
charToInt = _Eureka.charToInt

def cStrToInt(*args):
  return _Eureka.cStrToInt(*args)
cStrToInt = _Eureka.cStrToInt

def intToStr(*args):
  return _Eureka.intToStr(*args)
intToStr = _Eureka.intToStr

def cStrToNum(*args):
  return _Eureka.cStrToNum(*args)
cStrToNum = _Eureka.cStrToNum

def searchChar(*args):
  return _Eureka.searchChar(*args)
searchChar = _Eureka.searchChar

def findString(*args):
  return _Eureka.findString(*args)
findString = _Eureka.findString

def slice(*args):
  return _Eureka.slice(*args)
slice = _Eureka.slice

def shiftArrayLeft(*args):
  return _Eureka.shiftArrayLeft(*args)
shiftArrayLeft = _Eureka.shiftArrayLeft

def transferStr(*args):
  return _Eureka.transferStr(*args)
transferStr = _Eureka.transferStr

def createPCharFromBuffer(*args):
  return _Eureka.createPCharFromBuffer(*args)
createPCharFromBuffer = _Eureka.createPCharFromBuffer

def removeCharFromStr(*args):
  return _Eureka.removeCharFromStr(*args)
removeCharFromStr = _Eureka.removeCharFromStr

def removeMultipleCharFromStr(*args):
  return _Eureka.removeMultipleCharFromStr(*args)
removeMultipleCharFromStr = _Eureka.removeMultipleCharFromStr

def searchCharIndex(*args):
  return _Eureka.searchCharIndex(*args)
searchCharIndex = _Eureka.searchCharIndex

def sliceStr(*args):
  return _Eureka.sliceStr(*args)
sliceStr = _Eureka.sliceStr

def numToInt(*args):
  return _Eureka.numToInt(*args)
numToInt = _Eureka.numToInt

def fuseStrs(*args):
  return _Eureka.fuseStrs(*args)
fuseStrs = _Eureka.fuseStrs
class inputMouse(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, inputMouse, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, inputMouse, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_inputMouse(*args)
        try: self.this.append(this)
        except: self.this = this
    def UpdateProcessedCoordinates(self): return _Eureka.inputMouse_UpdateProcessedCoordinates(self)
    def ChangeCoordinates(self, *args): return _Eureka.inputMouse_ChangeCoordinates(self, *args)
    def buttonPress(self): return _Eureka.inputMouse_buttonPress(self)
    def getButtonState(self): return _Eureka.inputMouse_getButtonState(self)
    def GetButton(self): return _Eureka.inputMouse_GetButton(self)
    __swig_destroy__ = _Eureka.delete_inputMouse
    __del__ = lambda self : None;
inputMouse_swigregister = _Eureka.inputMouse_swigregister
inputMouse_swigregister(inputMouse)

class inputKeyboard(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, inputKeyboard, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, inputKeyboard, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _Eureka.new_inputKeyboard(*args)
        try: self.this.append(this)
        except: self.this = this
    def setInputText(self): return _Eureka.inputKeyboard_setInputText(self)
    def toggleTextMode(self): return _Eureka.inputKeyboard_toggleTextMode(self)
    def getText(self): return _Eureka.inputKeyboard_getText(self)
    def GetKey(self): return _Eureka.inputKeyboard_GetKey(self)
    __swig_destroy__ = _Eureka.delete_inputKeyboard
    __del__ = lambda self : None;
inputKeyboard_swigregister = _Eureka.inputKeyboard_swigregister
inputKeyboard_swigregister(inputKeyboard)

# This file is compatible with both classic and new-style classes.


