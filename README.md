# Medical Robotics 🤖
Hello! This is an assignment repository for the University of Surrey's Medical Robotics class. You'll find kinematics simulation and workspace analysis for a 4-DOF PincherX 100 robot arm in this repository. I've built the simulations using [Peter Corke's Robotics Toolbox in Python](https://github.com/petercorke/robotics-toolbox-python). The write-up can be found [here](https://www.notion.so/frankcholula/Medical-Robotics-Coursework-1403b40fbcd580b9b51ddbc292d31d40?pvs=4) on my personal Notion page.

If you are a **University of Surrey student**, you are welcome to use this project as a learning resource and reference for your coursework. A simple credit to the OC (wee! that's me, [Frank](https://frankcholula.notion.site/)) would be greatly appreciated. However, please note that submitting this work as your own academic assignment is not permitted and may lead to [academic misconduct penalties](https://www.surrey.ac.uk/office-student-complaints-appeals-and-regulation/academic-misconduct-and-appeals). Just make sure you're submitting your orignal work 😊.

## Setup 🛠
T️his project uses `Python 3.10.7` and [Poetry](https://python-poetry.org/) for dependency management. To install the dependencies, run the following command:
```bash
cd assignment1
poetry shell
poetry install
```

I also highly recommend using `pyenv` to manage your Python versions. If you're a Mac user, you can install `pyenv` using the following command:
```bash
brew install pyenv
pyenv install 3.10.7
```

For Windows users, you can install `pyenv-win` using [chocolatey](https://chocolatey.org/) or run the following command in PowerShell as an administrator:
```bash
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```

## Directory Layout 📖
```bash
mr
├── LICENSE
├── README.md
├── assignment1
│   ├── Makefile
│   ├── README.md
│   ├── assignment1
│   ├── assignment1_brief.pdf
│   ├── assignment1_submission.pdf
│   ├── model_files
│   ├── model_files.zip
│   ├── poetry.lock
│   ├── pyproject.toml
│   └── references
├── assignment1.zip
└── practicals
    ├── Medical Robotics Practical 1a.pdf
    ├── Medical Robotics Practical 1b.pdf
    ├── graphics.mat
    ├── lab3.m
    ├── license.txt
    ├── linksdata.mat
    └── puma_simulation.m
```
You'll find the Trossen PincherX 100 model files in `.stl`, `.step`, and `.f3d` format in the model_files directory. All simulations and workspace analysis are in the `assignment1` directory. The `practicals` directory contains MATLAB files for the practicals.

## Other Learning Resources 📚
- [Peter Corke's Robotics Toolbox in Python](https://github.com/petercorke/robotics-toolbox-python)
- [Interbotix PincherX 100 Arm Specification](https://docs.trossenrobotics.com/interbotix_xsarms_docs/specifications/px100.html)

## License 📃
This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). 
This means:
1.  **Attribution**: You must give appropriate credit to the original author (me, Frank Lu) if you use or modify this project.
2.  **Freedom**: You are free to use, modify, and distribute this project, including for commercial purposes, without restriction.
3.	**No Warranty**: This project is provided “as-is” without any warranty or liability on the part of the author.

You can read the full license in the [LICENSE](LICENSE) file.