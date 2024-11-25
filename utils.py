'''
/* //////////////////////////////////////////////////////////////////////////////////
// 
// Project :        Chess 2D 
// Description :    2D chess game in Python
// Programmer :     Uldrix | https://github.com/Uldrix
// Licence :        GNU
// 
// 
// 
//     ⠀⠀ ⠀⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣴⠞⠋⠁⣀⣠⣴⣶⣾⣿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆
//     ⠀ ⠀⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⠟⢻⣧⣤⣴⣿⠿⠋⠁⣴⡿⠿⢿⣿⣿⣿⣷⣶⣶⣶⣶⡶⠶⠚⠁⠀⠀⣠⣾⠏⠀
//⠀⠀⠀   ⠀⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⣀⣠⣴⣾⣿⣥⣤⣤⣭⣍⣁⡀⠀⠀⠘⣿⣇⠀⠀⠀⠈⠉⠉⠉⠉⠀⠀⠀⠀⢀⣠⣴⣿⠟⠁⠀⠀
//⠀⠀⠀⠀⠀ ⠀   ⠀⠀⠀⢀⣤⡶⠟⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠘⢿⣷⣦⣄⣀⣀⣀⣀⣀⣤⣤⣶⣾⣿⡿⠛⠁⠀⠀⢀⡀
//⠀⠀   ⠀⠀ ⠀⠀⠀⣠⡾⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⣩⣿⠿⠋⠁⠀⠀⣠⣶⠟⠋⠀
//⠀⠀   ⠀ ⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢄⠀⠀⠀⠀⣼⣿⠁⠀⠀⠀⢠⣾⡿⠃⠀⠀⠀
//⠀   ⠀⠀⠀⣠⡟⡡⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧⠀⠀⠀⠸⣿⣄⠀⢀⣴⣿⣿⠁⠀⠀⠀⠀
//⠀  ⠀⠀⢠⡟⡜⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠀⠀⠀⠀⠀⢀⣤⠶⠒⠛⠛⠒⠲⢤⡀⠀⠘⣷⠀⠀⠀⠙⠻⠿⠿⢿⣿⠇⠀⠀⠀⠀⠀
//⠀  ⣠⡶⠿⢇⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀⢀⡴⢪⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠙⢄⠀⢹⡄⠀⠀⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⠀⠀
//⠀  ⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠿⣦⣤⡞⣰⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡄⠀⡇⠀⠀⠀⢀⣠⣾⠟⢠⠀⠀⠀⠀⠀⠀
//⠀  ⠀⠀⡟⣿⣆⢀⠀⠀⠀⠀⠀⣠⠾⠕⠉⢉⣉⠀⣿⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠃⠀⣠⣶⣿⠟⠋⢀⣾⠀⠀⠀⠀⠀⠀
//⠀⠀  ⠀⢰⣿⣿⣯⣧⠠⠮⠴⠞⣁⣠⣴⣾⣿⣿⣷⡌⣿⠋⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⡟⠉⠀⠀⣠⣾⡏⠀⠀⠀⠀⠀⠀
//  ⠀⣠⠴⢾⣿⣿⣿⣿⠀⠳⣾⣿⣿⣿⣿⣿⣿⣿⣿⡇⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣷⣤⣴⣾⣿⠟⠀⠀⠀⠀⠀⠀⠀
//  ⢰⠁⠀⠀⠙⣿⣿⣧⠈⡆⢻⢿⣿⣿⣿⣿⣿⠿⠟⣃⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠂⣼⠀⢈⣩⣽⠿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀
//  ⣞⠀⠀⠀⣠⣿⣿⡿⠀⢺⡀⢑⡈⠉⠉⠉⠀⠀⠀⠀⠀⠀⠈⠻⣦⡞⠀⠀⠀⠀⠀⢠⣮⣾⣿⠿⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⢻⣦⣄⣴⡿⡿⠷⣿⠠⣀⡨⠥⣞⣳⡄⠀⢀⡀⠀⠀⠀⠀⠀⣀⣿⣇⠀⠀⠀⣀⣴⣿⠟⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠉⢻⠇⠀⠀⠀⠈⠣⠀⠀⠀⠀⢀⡽⣷⣄⡈⠉⠉⠀⠀⣊⣽⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠀⣾⠀⠀⠀⠀⠀⠀⠀⠀⠀⡰⠉⡴⣫⣿⣿⣒⡢⢄⣠⡾⠋⠉⠉⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⢸⠛⣷⣤⢀⡄⢀⠇⣠⠂⣸⣡⣚⣼⠋⠁⠀⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠘⣾⡀⡏⠙⡗⠻⠟⢻⠚⢻⢹⠙⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
//  ⠀⠀⠈⠓⠧⠴⣇⣴⣄⢼⣤⠟⠚⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
// 
// In Tenebris we code :: Forged by Uldrix :: Be aware of the Matrix :: ~~~~~~~~~~~~
// 
// ////////////////////////////////////////////////////////////////////////////////// */
'''
import pygame

def load_image(path):
    try:
        return pygame.image.load(path).convert_alpha()
    except pygame.error as e:
        raise FileNotFoundError(f"Image not found: {path}. Error: {e}")

def load_font(path, size):
    try:
        return pygame.font.Font(path, size)
    except pygame.error as e:
        raise FileNotFoundError(f"Font not found: {path}. Error: {e}")
