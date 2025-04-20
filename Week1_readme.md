
# Week1_README.md

## Task Summary:
As part of Week 1 of the internship, the following tasks were completed:

- Created **one public** and **one private** GitHub repository.
- Pushed a previously developed website folder (`Insecure_Web_App`) from a local Linux machine to the private repository using Git CLI commands.
- Explored and utilized basic Git commands via CLI.
- Added the internship supervisor as a **collaborator** to the **private** repository.
- Documented all steps and commands used during this process.

---

## Steps Followed:

### Step 1: Created GitHub Repositories

- Logged into GitHub.
- Created a **public repository** named `Cyber-Allegiance-Internship-Public`.
- Created a **private repository** named `Cyber-Allegiance-Internship-Private`.

---

### Step 2: Open Terminal in Linux Machine

- Navigated to the working directory where the project folder `Insecure_Web_App` is located.

---

### Step 3: Cloned the Private GitHub Repository Locally

```bash
git clone https://github.com/AtejiEmmanuel/Cyber-Allegiance-Internship-Private.git
```

---

### Step 4: Verified Git Status

```bash
cd CyberAllegiance-Private
git status
```

---

### Step 5: Added the Project Folder to Git

```bash
cp -r /path/to/Insecure_Web_App .
git add Insecure_Web_App
```

---

### Step 6: Committed the Changes

```bash
git commit -m "Added Insecure Web Application project"
```

---

### Step 7: Pushed Code to GitHub

```bash
git push origin main
```

---

### Step 8: Verified Project Was Pushed Successfully

- Checked the GitHub web interface to confirm files were uploaded correctly.

---

### Step 9: Added Collaborator to Private Repository

- Navigated to the **Settings** of the `CyberAllegiance-Private` repository.
- Selected **Collaborators** under **Access** settings.
- Invited the internship supervisor's GitHub username as a collaborator.

---

### Step 10: Explored Basic Git Commands

- `git init` – Initialize a new Git repository
- `git clone` – Clone a repository into a new directory
- `git status` – Show the working directory status
- `git add <file/folder>` – Add files to staging area
- `git commit -m "message"` – Commit changes with a message
- `git push` – Push local changes to remote
- `git pull` – Pull changes from remote to local
- `git log` – View commit history
- `git branch` – View and manage branches
- `git checkout` – Switch branches or restore files
- `git remote -v` – View connected remotes

---

### Notes:

- All activities and report submissions for the internship will be maintained and updated in the private repository.
- This file (`Week1_README.md`) serves as documentation for all actions and commands performed during Week 1.

