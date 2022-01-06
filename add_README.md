# Understanding RoRD

Understanding the fork of RoRD repository on [TheProjectsGuy/RoRD](https://github.com/TheProjectsGuy/RoRD) (original from [UditSinghParihar/RoRD](https://github.com/UditSinghParihar/RoRD)). The following repositories have also been referenced:

- [touranisatyajit/DVD-RRC](https://github.com/touranisatyajit/DVD-RRC)

This file is for additional/understanding purposes.

## Table of contents

- [Understanding RoRD](#understanding-rord)
    - [Table of contents](#table-of-contents)
    - [Direct Evaluations](#direct-evaluations)
    - [Understanding](#understanding)
    - [References](#references)
    - [Credits](#credits)

## Direct Evaluations

The `Direct Evals` folder (see [References](#references) for links) has evaluations (not explanation: only runs and minor change details). You can use this to run commands, and for guidance if things don't go as expected. The Direct Evals has the following items

| Item Name | Description |
| :---- | :---- |
| `RoRD Eval 1.txt` | Extracting matches using RoRD |
| `RoRD Eval 2.txt` | Evaluating on the DiverseView dataset. Both pair-wise and using CSV |
| `RoRD Eval 3.txt` | Training on PhotoTourism set |
| `RoRD Eval 4.txt` | Inference on Oxford Car Dataset |

The above files contain the brief commands, outputs, errors and patches I executed to achieve the goal mentioned in the description. These same goals are also listed in the official repo README.

## Understanding

These explore the code in-depth: code execution, sample scripts, parallels from the paper, outputs (see `Resources` folder in references) as images, etc. These are divided based on the python script being analyzed. Each folder will have a `.txt` file containing the detailed explanation and `imgs` folder containing images, sample scripts, etc.

| S. No. | Folder Name | Script | Description |
| :---- | :----- | :---- | :---- |
| 1 | `Understanding RoRD - Eval - ExtractMatches / Understanding 1` | `./extractMatch.py` | Evaluating RoRD on two simple images. No orthographic views, depth, etc. only two simple images whose descriptors are matched |
| 2 | `Undesctanding RoRD - Eval - DiverseView / Understanding 2` | `./demo/register.py` | Pose estimation on a single pair of images in the DiverseView dataset. Note that the depth information, as well as homography to generate the orthographic view (from the image) is also needed (so only use samples from DiverseView). |
| 3 | `Undesctanding RoRD - Eval - DiverseView / Understanding 3` | `./evaluation/DiverseView/evalRT.py` | Pose estimation on a sequence of images (specified in a CSV file, check the `imgs` folder for format) from the DiverseView dataset. Very similar from `Understanding 2` |
| 4 | `Undesctanding RoRD - Training / Understanding 4` | `.\trainPT_ipr.py` | Run training on the PhotoTourism dataset's `brandenburg_gate` (only the images are used, `stereo` data not required). The checkpoints (output) are in `Resources` folder (check references). Though the `brandenburg_gate` is about 5 GB in size, the actual training data (required for this) is only about 600 MB (subset shared in `Resources/phototourism`). |
| 5 | `Understanding RoRD - Eval - OxfordCar / Understanding 5` | `./extractMatchTopRobo.py` (touranisatyajit/DVD-RRC repo) | Top view / orthogonal view matches. Testing/evaluation on Oxford Car dataset images. Homography has to be calculated and stored beforehand. |

## References

- Main link to the `Understanding` folder on [my OneDrive](https://iiitaphyd-my.sharepoint.com/:f:/g/personal/avneesh_mishra_research_iiit_ac_in/Etblr7dQRJpBgQLTGFpY72oBIsBh6FI18fYebaBsjiPJdg?e=863i9d) (IIIT-Hyderabad CAS login required): The folder contains all the material described above (except the `Resources` described below)
- Resources folder on [my OneDrive](https://iiitaphyd-my.sharepoint.com/:f:/g/personal/avneesh_mishra_research_iiit_ac_in/EnIRBjM3lOlEvKrhSe4wOP4BO85c6gMCX3ppLOerOM2FKQ?e=Y3hcO7) (IIITH CAS login required): The folder contains the outputs (of training), starting model (D2-Net and RoRD), the DiverseView dataset, and the subset of `brandenburg_gate` useful for training. This was last updated on 23 Dec 2021.

## Credits

This file is maintained by Avneesh Mishra and can be accessed through the [fork of RoRD](https://github.com/TheProjectsGuy/RoRD), the [official RoRD repository](https://github.com/UditSinghParihar/RoRD) belongs to Udit Singh Parihar.
