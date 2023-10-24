To allow users to run Docker without needing to use `sudo`, you can add your user to the `docker` group. Here's how you can do it:

1. First, make sure the Docker daemon is running.

2. Create a group (e.g., 'docker'):

```bash
sudo groupadd docker
```

3. Add your user to the `docker` group:

```bash
sudo usermod -aG docker $USER
```

Replace `$USER` with your username.

4. Log out and log back in, or run the following command to apply the group changes to your current session:

```bash
newgrp docker
```

5. To verify that you can run Docker without `sudo`, you can run a simple Docker command, like:

```bash
docker --version
```

You should be able to run Docker commands without needing `sudo` now.

Please note that adding a user to the `docker` group grants them significant privileges, as they can interact with the Docker daemon, potentially leading to security risks. Make sure you trust the user you're adding to the group and understand the implications.

Additionally, be aware that in some Linux distributions, you might need to restart your system for the group changes to take effect.