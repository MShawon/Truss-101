<p align="center">
  <img src="Tutorial/logo.png" width="125" height="125"
</p>
<p align="center">
  <a href="https://github.com/MShawon/Truss-101/releases/latest"><img alt="GitHub release (latest by date)" src="https://img.shields.io/github/v/release/MShawon/Truss-101?color=success"></a>
  <a href="https://github.com/MShawon/Truss-101/releases/latest"><img alt="GitHub Release Date" src="https://img.shields.io/github/release-date/MShawon/Truss-101?color=success"></a>
  <a href="https://github.com/MShawon/Truss-101/"><img alt="GitHub Downloads" src="https://img.shields.io/github/downloads/MShawon/Truss-101/total?label=GitHub%20downloads&color=success"></a>
  <a href="https://sourceforge.net/projects/truss-101/"><img alt="SourceForge Downloads" src="https://img.shields.io/sourceforge/dt/truss-101?label=SourceForge%20downloads&color=success"></a>
  <img alt="OS" src="https://img.shields.io/badge/OS-Windows-success">
</p>
<p align="center">
  <a href="https://github.com/MShawon/Truss-101/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/MShawon/Truss-101?color=important"></a>
  <a href="https://saythanks.io/to/as2robot143@gmail.com">
  <img alt="SayThanks" src="https://img.shields.io/badge/Say-thanks!-1EAEDB.svg">
  </a>
  <a href="https://paypal.me/shawon107">
    <img alt="Donate" src="https://img.shields.io/badge/Donate-PayPal-green.svg">
  </a>
</p>

<p align='center'><img src='Tutorial/gif.gif' width='90%' height='90%' ></p>

# Truss 101
A desktop application to solve statically determinate and indeterminate 2D truss structures using Matrix Displacement Method (aka Finite Element Method).

## Where to download?
<p align='left'>
  <a href="https://github.com/MShawon/Truss-101/releases/download/1.0.2/Truss.101_win_Setup_v1.0.2.exe">
  <img src="https://img.shields.io/badge/v1.0.2-Download%20Truss%20101-green?logo=github&logoWidth=10&flat&logoColor=black" width="450" height="55">
  </a>
</p>


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
  * Graphs showing members relative strength
  * Tension, compression value in Tabulated form
* Multiple projects
* Beautiful Report 
  * Input-Output data
  * Member Stiffness Matrices
  * Global Stiffness Matrix
  * Force Matrix

# Tutorial 
<a href="https://www.youtube.com/watch?v=5yi33cXewrU"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white"></a>
[![YouTube video](Tutorial/YouTube_photo.png)](https://www.youtube.com/watch?v=5yi33cXewrU)


# TO DO

* Influence line for a unit load
* 3D truss

# Known Issues
Program works fine. Just two bugs in Report.
* Constrained global stiffness matrix is not removing constrained rows in Report.
* Force matrix shows wrong degrees of freedom in Report. Those dofs should be incremented by 1.
* Support nodes value greater than 10 is not reading correctly when opened from saved files.

These will be patched in the next update.

> I welcome any feedback at as2robot143@gmail.com


