# python-scripts

### How to add SSH Keys to github and generate it in local

1. SSH (Secure Shell) is used communicate with github(server) from your local machine(Client) in encrypted form which is more secure than HTTPS.
2. using HTTPS asks for password everytime when you push the code but SSH don't ask.

### How to generate and add SSH keys?
1. Check whether you have existing keys in your local machine via git bash or linux terminal
    ```bash
      ls -al ~/.ssh
    ```

2. Generate a new SSH Key using GitBash
  ```bash
     ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
  ```
`-t rsa:` Specifies the type of key (RSA).
`-b 4096:` Specifies the number of bits in the key (4096 for stronger security).
`-C "your_email@example.com":` Adds a label (your email) for the key.

You will be asked where to save the key:
- Press Enter to save it to the default location (/c/Users/your-username/.ssh/id_rsa).
- Optionally, you can add a passphrase for an extra layer of security.

SSH will generate 2 keys:
- public key: we need to add this to github in ssh key section
- private key: present in local machine

3. Add the SSH Key to the SSH Agent
Next, you need to add your private key to the SSH agent. Run these commands in Git Bash:

    1. Start the SSH agent:
    ```bash
    eval "$(ssh-agent -s)"
    ```
    2. Add your SSH private key to the agent:
    ```bash
    ssh-add ~/.ssh/id_rsa
    ```
4. Add the SSH Key to GitHub
   Now that you've created an SSH key, you need to add the public key (id_rsa.pub) to your GitHub account:
   Copy the public key to your clipboard by running:
   ```bash
   cat ~/.ssh/id_rsa.pub
   ```
   Copy the output (it starts with ssh-rsa and ends with your email).

   Go to GitHub:
      1. Log in to your GitHub account.
      2. Go to GitHub SSH Keys Settings.
      3. Click New SSH key.
      4. Give the key a descriptive title.
      5. Paste your SSH key in the "Key" field.
      6. Click Add SSH key.

5. Test the SSH Connection
   You can test your SSH connection by running the following command in Git Bash:
     ```bash
     ssh -T git@github.com
     ```
   You may get a message asking if you want to continue connecting (yes/no). Type yes and press Enter.

   If everything is set up correctly, you'll see a message like:
   ```vbnet
   Hi your-username! You've successfully authenticated, but GitHub does not provide shell access.
   ```

6. Configure Git to Use SSH
If you cloned your GitHub repository using HTTPS, you'll need to change the remote URL to use SSH instead. To do this:

  1. Change the remote URL: 
      ```bash
       git remote set-url origin git@github.com:your-username/your-repository.git
      ```
  3. Now you can push your code using SSH:
      ```bash
       git push -u origin master
      ```
