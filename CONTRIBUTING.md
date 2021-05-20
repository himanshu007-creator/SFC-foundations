## ⭐ First time contributing?

Refer to the following articles on the basics of Git and Github and can also contact the Project Mentors, in case you are stuck:

* [Watch this video to get started, if you have no clue about open source](https://youtu.be/SL5KKdmvJ1U)
* [Getting started with Git and GitHub](https://docs.github.com/en/free-pro-team@latest/github/getting-started-with-github)
* [Forking a Repo](https://help.github.com/en/github/getting-started-with-github/fork-a-repo)
* [Cloning a Repo](https://help.github.com/en/desktop/contributing-to-projects/creating-a-pull-request)
* [How to create a Pull Request](https://opensource.com/article/19/7/create-pull-request-github)

<img src="https://camo.githubusercontent.com/71995d6b0e620a9ef1ded00a04498241c69dd1bf/68747470733a2f2f6769746875622d696d616765732e73332e616d617a6f6e6177732e636f6d2f736b697463682f6973737565732d32303132303931332d3136323533392e6a7067"></img>

# Contributing Guidelines👩‍💻👨‍💻

This documentation contains a set of guidelines to help you during the contribution process.
When contributing to this repository, please first discuss the change you wish to make via issue, email, or any other method with the owners of this repository before making a change.

## 💥 How to start?!

Below you will find the process and workflow used to review and merge your changes.

### Step 0 : Find an issue🤔

- Take a look at the Existing [Issues](https://github.com/himanshu007-creator/SFC-foundations/issues) or create your own Issues!
- Wait for the Issue to be assigned to you after which you can start working on it.
- Note : Every change in this project should/must have an associated issue.


### Step 1 : Fork the Repository🔗

**1.** Fork this Repository .  Click on the <img src="https://img.icons8.com/ios/24/000000/code-fork.png"> symbol at the top right corner. This will create a Local Copy of this Repository on your Github Profile.
Keep a reference to the original project in `upstream` remote.  

**2.** Clone the forked repository.

```bash
git clone https://github.com/<your-username>/<repo-name>  
```

**3.** Navigate to the project directory.

```bash
cd SFC-foundations
```

**4.** Add a reference(remote) to the original repository.

```bash
git remote add upstream https://github.com/<upstream-owner>/<repo-name>  
```

**5.** Check the remotes for this repository.
```
git remote -v
```
  
- If you have already forked the project, update your copy before working.

```bash
git remote update
git checkout <branch-name>
git rebase upstream/<branch-name>
```  

### Step 2 : Branch

**6.** Create a new branch. Use its name to identify the issue your addressing.

```bash
# It will create a new branch with name Branch_Name and switch to that branch 
git checkout -b branch_name
```

### Step 3 : Work on the issue assigned

**7.** Add all the files/folders needed.

```bash  
# To add all new files to branch Branch_Name  
git add .  

# To add only a few files to Branch_Name
git add <some files>
```

### Step 4 : Commit your changes .

**8.** Give a descriptive message for the convenience of reviewer by:

```bash
# This message get associated with all files you have changed  
git commit -m "message"  
```

- **NOTE**: A PR should have only one commit. Multiple commits should be squashed.

### Step 5 : Work Remotely

**9.** Now you are ready to your work to the remote repository.
- When your work is ready and complies with the project conventions, upload your changes to your fork:

```bash  
# To push your work to your remote repository
git push -u origin Branch_Name
```

### Step 6 : Pull Request

- Go to your forked repository in browser and click on compare and pull requests.
Then add a title and description to your pull request that explains your contribution.  
- Create a Pull Request which will be reviewed and suggestions would be added to improve it.
- Add Screenshots to help us know what this enhancement/implementation is all about.
Your Pull Request has been submitted and will be reviewed by the maintainer and merged.

**10.** **Congratulations!✨✨** Sit and relax, you've made your contribution to [SFC-foundations](https://github.com/mansijain980/SFC-foundations) project.😎

## Things to remember while contributing:
* Please make sure to update tests case wherever necessary.
* If any package is used that was not present in the requirements.txt, add the package name and the version used to the requirements.txt file.

<b>For major changes, you are welcomed to open an issue and discuss what you would like to contribute. Enhancements will be appreciated.</b>

<p align = "center">

[![built with love](https://forthebadge.com/images/badges/built-with-love.svg)]()
[![Open Source Love svg2](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

</p>
<img src="https://github.blog/wp-content/uploads/2014/06/55f2798a-eb56-11e3-92e7-b79ad791a697.gif" style = "width:300px ; height;200px;">
