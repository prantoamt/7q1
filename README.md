### Table of Contents  
---------------------

- [Before you start](#before-you-start)
- [Quick Start](#quick-start)
    + [Install pdm as python package manager](#install-pdm-as-python-package-manager)
    + [Clone repo](#clone-repo)
    + [Goto the base directory](#goto-the-base-directory)
    + [Install the dependencies](#install-the-dependencies)
    + [Run the project](#run-the-project)
    + [See project in action](#see-project-in-action)
- [Api](#api)


# Before you start
----------------------------
Hello! Welcome to the [7Q1](https://www.7q1.de/en/) assigment repo. 
This `readme.md` file will guide you to run the project in your local machine (Development Environment). 
The section [Quick Start](#quick-start) has all the required steps to run the project. Before that, please read the following notes:

- A SQLite database is used for this project.
- Few custom commands have been written in `app/administration/management/commands` to populate the database from provided files. 
- A user is will be created with `username: john` and `password: j123j123` when you will run the project (Not SuperUser).
- **Please use this user's credentials for api authentication.**


# Quick Start
-----------------
In order to run the project, please pursue the following steps.

#### Install pdm as python package manager
-------------------------------------------
- First of all, please install [PDM](https://pdm.fming.dev/latest/) from their official website based on your local machine's operating system.

#### Clone repo
--------------------
Clone this git repository to your local machine. Open your terminal and run the command
```
git clone https://github.com/prantoamt/7q1.git
```

#### Goto the base directory
------------------------------------
After cloning the repo, goto the django project's base directory by executing the following command: 
```
cd 7q1
```

#### Install the dependencies
-----------------------------------------------------------------
Now, install the dependencies with PDM lock file.
```
pdm install
```

### Run the project
-------------------
There is a run.sh file inside this directory where all neccessary commands are provided to run the project. 
Execute the following commands to run the .sh file:
```
chmod +x ./run.sh
./run.sh
```

### See project in action
-------------------------
Congratulations! you have successfully run the project in development server. You can access the project at `8000` port.

# Api
-----
An OpenApi 3 specification has been added to the project to explain and demonstrate the end-points.
Please find the swagger specification at: `http://127.0.0.1:8000/api/schema/swagger-ui/`

- To submit a list of keywords (products) in `api/companies/`, you can write your query params as follows:
    - `api/companies/?product=PTFE%HOSE&product=HIGH%PRESSURE%HOSES`
    - I choosed this method to submit multiple values for one param because it is supported for most application and
    django also recommends this method. Though there is no standard method to send multiple values. [Reference](https://stackoverflow.com/a/24728298/6092533).
    - Exmaple req: 
        ```
        curl -X 'GET' \
        'http://127.0.0.1:8000/api/companies/?product=HIGH%20PRESSURE%20HOSES&product=PTFE%HOSE' \
        -H 'accept: application/json' \
        -H 'Authorization: Token 183d43b34dbca3e58596fa43680ea0a09c38b7ee'
        ```
