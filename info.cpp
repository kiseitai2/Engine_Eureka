#include "info.h"

//Engine name space macro
//ENGINE_NAMESPACE

/*ScreenInfo*/

const std::string ScreenInfo::OPENGL = "opengl";
const std::string ScreenInfo::DIRECT3D = "direct3d";
const std::string ScreenInfo::SOFTWARE = "software";

ScreenInfo::ScreenInfo()
{
    m_frames_per_second = 0;
    m_screen_width = 0;
    m_screen_height = 0;
    m_screen_bpp = 0;
}

void ScreenInfo::SetScreenInfo(size_t displayCount, size_t display, size_t frames_per_second, size_t screenWidth,
                               size_t screenHeight, size_t screenBPP, const std::string& driver, size_t screenmode)
{
    m_display_count = displayCount;
    m_display = display;
    m_frames_per_second = frames_per_second;
    m_screen_width = screenWidth;
    m_screen_height = screenHeight;
    m_screen_bpp = screenBPP;
    m_screenmode = screenmode;
    video_driver = driver;
}

math_point& ScreenInfo::GetScreenLoc()
{
    return screenLoc;
}

size_t ScreenInfo::GetMaxFramesPerSec() const
{
    return m_frames_per_second;
}

size_t ScreenInfo::GetScreenBPP() const
{
    return m_screen_bpp;
}

size_t ScreenInfo::GetScreenHeight() const
{
    return m_screen_height;
}

size_t ScreenInfo::GetScreenWidth() const
{
    return m_screen_width;
}

size_t ScreenInfo::GetDisplayIndex() const
{
    return m_display;
}

size_t ScreenInfo::GetDisplayCount() const
{
    return m_display_count;
}

void ScreenInfo::SetScreenLoc(int x, int y)
{
    screenLoc.X = x;
    screenLoc.Y = y;
}

size_t ScreenInfo::GetScreenMode() const
{
    return m_screenmode;
}

std::string ScreenInfo::GetRenderDriver() const
{
    return video_driver;
}
/*End of ScreenInfo*/

/*SoundInfo*/
SoundInfo::SoundInfo()
{
    m_frequency =0;
    m_channels = 0;
    m_chunksize = 0;
}

void SoundInfo::SetSoundInfo(size_t frequency, size_t channels, size_t chunksize)
{
    m_frequency = frequency;
    m_channels = channels;
    m_chunksize = chunksize;
}

size_t SoundInfo::GetSoundFrequency() const
{
    return m_frequency;
}

size_t SoundInfo::GetSoundChannels() const
{
    return m_channels;
}

size_t SoundInfo::GetSoundChunkSize() const
{
    return m_chunksize;
}

/*End of SoundInfo*/

/*GameInfo*/
const std::string GameInfo::EMPTY = "";

GameInfo::GameInfo():ScreenInfo(), SoundInfo()
{
    m_rootdata = "";
    m_mod = "";
    m_saveloc = "";
    m_name = "";
    m_icon = "";
    m_render_quality = "";
    m_blitlevels = 0;
}

void GameInfo::SetInfo(const std::string& rootdata, const std::string& mod, const std::string& saveloc,
            const std::string& name, const std::string& icon, const std::string& renderQuality,
            size_t displayCount, size_t display, size_t frames_per_second, size_t screenWidth, size_t screenHeight, size_t screenBPP,
            size_t blitlevels, size_t screenmode, const std::string& driver, size_t frequency, size_t channels, size_t chunksize)
{
    SetScreenInfo(displayCount, display, frames_per_second, screenWidth, screenHeight, screenBPP, driver, screenmode);
    SetSoundInfo(frequency, channels, chunksize);
    m_rootdata = rootdata;
    m_mod = mod;
    m_saveloc = saveloc;
    m_name = name;
    m_icon = icon;
    m_render_quality = renderQuality;
    m_blitlevels = blitlevels;
}
std::string GameInfo::GetRootDirectory() const
{
    return m_rootdata;
}

std::string GameInfo::GetModName() const
{
    return m_mod;
}

std::string GameInfo::GetGameName() const
{
    return m_name;
}

std::string GameInfo::GetIconLoc() const
{
    return m_icon;
}

size_t GameInfo::GetBlitLevels() const
{
    return m_blitlevels;
}

std::string GameInfo::GetRenderQuality() const
{
    return m_render_quality;
}
/*End of GameInfo*/

//End of namespace macro
//ENGINE_NAMESPACE_END
