# Linked Out


![GitHub stars](https://img.shields.io/github/stars/RATED-R-SUNDRAM/LINKED_OUT?style=social)
![GitHub forks](https://img.shields.io/github/forks/RATED-R-SUNDRAM/LINKED_OUT?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/RATED-R-SUNDRAM/LINKED_OUT?style=social)
![Repo. Size](https://img.shields.io/github/repo-size/RATED-R-SUNDRAM/LINKED_OUT?color=white) 


![GitHub contributors](https://img.shields.io/github/contributors/RATED-R-SUNDRAM/LINKED_OUT?color=blue)
![GitHub Closed issues](https://img.shields.io/github/issues-closed-raw/RATED-R-SUNDRAM/LINKED_OUT?color=brightgreen)
![GitHub PR Open](https://img.shields.io/github/issues-pr/RATED-R-SUNDRAM/LINKED_OUT?color=red)
![GitHub PR closed](https://img.shields.io/github/issues-pr-closed-raw/RATED-R-SUNDRAM/LINKED_OUT?color=red)
![GitHub language count](https://img.shields.io/github/languages/count/RATED-R-SUNDRAM/LINKED_OUT?style=plastic)
![GitHub top language](https://img.shields.io/github/languages/top/RATED-R-SUNDRAM/LINKED_OUT?style=plastic)
![GitHub last commit](https://img.shields.io/github/last-commit/RATED-R-SUNDRAM/LINKED_OUT?color=red&style=plastic)
![GitHub Maintained](https://img.shields.io/badge/Maintained%3F-yes-brightgreen.svg?v=103)


## About the Project 
This Project is aimed to solve the problems of beginner and intermeddiate programmers whose want to collaborate with other like minded individuals over any project, In this way 2 or more completely unknown persons with similar skill-sets and willing to do a project or collaboration can find themselves on the platform and team up to proceed about it.

### What it does
This web app is an end-to-end solution for anyone willing to find people with similar interestss and skills. 

- *It suggests individuals based on similar intrests and skill sets by **custom algorithm***).
- Allows collaboration (*Create a group with 2 or more person , chat , video and audio calling , also code sharing via chat*). 
- Users can showcase their work through *news feeds*.

### How does it work

- First user registers on the website.
- Then user fills info separated into two categories:

    1. Personal info(contact related)
    2. Skill-set info

- The second type of infomration is used to suggest other users with similar skill-set someone can also search individuals for a particular label.

- Then the individuals audit the persons and send them a *collaborate-request* with a message(with purpose of collaboration).

- The users can see all the pending collaborate-requests and accept the ones they like. When accepted, a chat group is created and they can start brainstorming and contributing.

### Where can I learn more about it
You can refer to the [slack channel link](https://join.slack.com/t/kwoc-koss/shared_invite/zt-wlftnk75-VoQHEEB9WpkHfza6~GGpWQ) to join the slack group for kwoc or mail me [ss6437p[at]gmail.com](mailto:ss6437p@gmail.com) to know more.

## Setup Locally

- Clone the repo: 
    ```
    git clone https://github.com/RATED-R-SUNDRAM/LINKED_OUT.git
    ```
- Move to the base directory:
    ```
    cd LINKED_OUT
    ```
- Create a new python enveronment.
    ```
    python -m venv env
    ```
- Activate enveronment
    
    On Windows:
    ```
    env\Scripts\activate
    ```
    
    On Mac and Linux:
    ```
    source env/bin/activate
    ```
- Install required dependences.
    ```
    pip install -r requirements.txt
    ``` 
- Make migrations.
    ```
    python manage.py makemigrations
    python manage.py migrate.
    ```
- Run app locally.
    ```
    # for development, use dev_settings.py file
    python manage.py runserver --settings hiya.dev_settings

    #for production, use settings.py file
    python manage.py runserver 
    ```



## Future plans

We will split the time we have for kwoc in 3 regions the first 1.5 weeks for front-end requirements then a week or so for algorithmic finalizing and the rest 1.5 weeks for back-end related requirements.

Currently the front-end related requirements is listed in issues read through the materials and suggest more of them. I will also be putting more issues related to the timeframe accordingly.


## KWoC-2021

Currently, This project is under development in the [KWOC 2021](https://kwoc.kossiitkgp.org/) program. Join the  [link](https://join.slack.com/t/kwoc-koss/shared_invite/zt-wlftnk75-VoQHEEB9WpkHfza6~GGpWQ) for joining the discussion group. 


### Contributors

![Contributors](https://contributors-img.web.app/image?repo=RATED-R-SUNDRAM/LINKED_OUT)
