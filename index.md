<p align="center">
  <img src="https://github.com/MShawon/Truss-101/blob/gh-pages/logo.png?raw=True" width="125" height="125">
</p>
<p align="center">
  <a href="https://github.com/MShawon/Truss-101/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/MShawon/Truss-101?color=success"></a>
  <a href="https://github.com/MShawon/Truss-101/releases/latest"><img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/MShawon/Truss-101?color=success"></a>
  <a href="https://github.com/MShawon/Truss-101/"><img alt="GitHub Downloads" src="https://img.shields.io/github/downloads/MShawon/Truss-101/total?label=GitHub%20downloads&color=success"></a>
  <a href="https://sourceforge.net/projects/truss-101/"><img alt="SourceForge Downloads" src="https://img.shields.io/sourceforge/dt/truss-101?label=SourceForge%20downloads&color=success"></a>
  <img alt="OS" src="https://img.shields.io/badge/OS-Windows%20/%20Linux / Mac-success">
</p>
<p align="center">
  <a href="https://github.com/MShawon/Truss-101/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/MShawon/Truss-101?color=important"></a>
  <a href="https://github.com/MShawon/Truss-101/blob/main/DONATE.md"><img alt="Donate" src="https://img.shields.io/badge/Donate-PayPal / Crypto-green.svg"></a>
</p>

<p align='center'><img src='https://github.com/MShawon/Truss-101/blob/main/Tutorial/gif.gif?raw=True' width='90%' height='90%' ></p>

# Truss 101
A desktop application to solve statically determinate and indeterminate 2D truss structures using Matrix Displacement Method (aka Finite Element Method).


## Why Truss 101?
* Develop Structures using Nodes and Members
* Unit conversion
* Supports
  * Pinned and Roller support 
  * Stability check
* Multiple loads at the same point
* Individual property for members 
  * Modulus of Elasticity (E)
  * Area (A)
* Nodal displacements
  * Graphs
  * Tabulated
  * Animation
* Member forces and support reactions
  * Force and stress
  * Graphs showing members relative strength
  * Tension, compression value in Tabulated form
* Influence line for a unit load
* Multiple projects
* Beautiful Report 
  * Input-Output data
  * Member Stiffness Matrices
  * Global Stiffness Matrix
  * Force Matrix
  * Influence Line Diagram


# Windows
* ## Binary Release
  For windows you can download the latest binary release from the following button. Download the exe, setup it by just clicking *next*, *next*, *next* and you are good to go.
  
  <p align='left'>
    <a href="https://github.com/MShawon/Truss-101/releases/download/1.1.4/Truss.101_win_Setup_v1.1.4.exe">
    <img src="https://img.shields.io/badge/v1.1.4-Download%20Truss%20101-green?logo=windows&logoWidth=10&flat&logoColor=black" width="450" height="55">
    </a>
  </p>
* ## Installation
  *If you wish to run it from the source code, keep reading.*

  First, make sure you have installed git and Python version between 3.7.x to 3.9.x

  Then open command prompt (cmd) and type
  ```
  git clone https://github.com/MShawon/Truss-101.git --depth 3
  ```
  ```
  cd Truss-101
  ```
  ```
  pip install -r requirements.txt
  ```
* ## Usage
  Open command prompt in Truss-101 folder and run
  ```
  python main.py
  ```

# Linux / Mac
* ## Installation
  First, make sure you have installed git and Python version between 3.7.x to 3.9.x

  Then open your favourite terminal and run
  ```
  git clone https://github.com/MShawon/Truss-101.git --depth 3
  ```
  ```
  cd Truss-101
  ```
  ```
  pip3 install -r requirements.txt
  ```
* ## Usage
  Open your favourite terminal in Truss-101 folder and run
  ```
  python3 main.py
  ```
# Tutorial 
**1) Analysis of Truss Structures**

[![YouTube video](https://github.com/MShawon/Truss-101/blob/gh-pages/tutorial.png?raw=True)](https://www.youtube.com/watch?v=5yi33cXewrU)

**2) Truss Influence Line**

[![YouTube video 2](https://github.com/MShawon/Truss-101/blob/gh-pages/tutorial2.png?raw=True)](https://www.youtube.com/watch?v=7H7eLLeZys8)


# Changelog
## v1.1.4
* Cross-platform compatible code
* Include all of the members' ILD in the report
* Few other bug fixes. 

## v1.1.3
* fix large truss report bug

## v1.1.2
* up to 1000 nodes, members, supports, loads, and properties are now possible
* setting unit before creating a new file
* stress calculation is now available on the force page
* showing force or stress value directly on the graph instead of a number is available by force checkbox
* better font in debug window and naming convention in code
* report bug fixes

## v1.1.1
* wrong reaction calculation fixes
* UI improved for 1280*720 resolution
* overall UI improvement
* debug window is added
* Added few other features

## v1.1.0
* Influence line for a unit load is added.
* Automatic table update due to spinbox value change is deprecated. Now the update button must be used.
* Matrices bug in Report is fixed. 
* Application startup and closing time is improved.
* Few other bug fixes.

## v1.0.2
Application startup time is improved

## v1.0.0
Initial release


# License
* This software is under GPL v3 license. See more <a href="https://github.com/MShawon/Truss-101/blob/main/LICENSE">https://github.com/MShawon/Truss-101/blob/main/LICENSE</a>
* Some icons are from icons8.  <a href="https://icons8.com">https://icons8.com</a>
* This program uses Qt Version 5.15.2. Please see <a href="https://www.qt.io/licensing/">https://www.qt.io/licensing/</a> for an overview of Qt licensing.
