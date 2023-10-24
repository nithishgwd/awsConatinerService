- used Wsl for ubuntu 

- installed docker engine on ubuntu
https://docs.docker.com/engine/install/ubuntu/

- downloaded minikube binary from doc 
**link**
https://minikube.sigs.k8s.io/docs/start/

- i am using docker to host minikube (can have QEMU, Hyperkit, Hyper-V, KVM, Parallels, Podman, VirtualBox, or VMware Fusion/Workstation)

- The Docker driver allows you to create a local, single-node Kubernetes cluster within a Docker container on your local machine. This can be a convenient and lightweight way to run Kubernetes for development and testing purposes.

```bash
minikube start --memory 4096 --cpus 4 --driver=docker
```

Minikube can be started using different hypervisors or container runtimes, depending on your requirements and environment. Here are some of the possible ways to start Minikube:

1. **Docker Driver**: Minikube can run a Kubernetes cluster as a Docker container on your local machine. This is a convenient option for local development and testing. Use the `--driver=docker` flag when starting Minikube.

```bash
minikube start --driver=docker
```

2. **VirtualBox**: You can run Minikube with VirtualBox as the hypervisor. This option provides a full VM-based Kubernetes cluster on your local machine.

```bash
minikube start --driver=virtualbox
```

3. **KVM2**: If you're using a Linux machine and have KVM installed, you can use KVM2 as the driver. It's a lightweight option for Linux users.

```bash
minikube start --driver=kvm2
```

4. **VMware**: If you have VMware installed, you can use the VMware driver to start Minikube.

```bash
minikube start --driver=vmware
```

5. **Hyper-V**: If you're on a Windows machine, you can use Hyper-V as the driver. Make sure to enable Hyper-V and install the necessary components.

```bash
minikube start --driver=hyperv
```

6. **Podman**: Minikube can also be started using Podman as the container runtime if you prefer Podman over Docker.

```bash
minikube start --driver=podman
```

7. **Custom Driver**: Minikube allows you to create custom drivers to run Kubernetes clusters in different environments or with other container runtimes.

These are some of the most common ways to start Minikube, and the choice of driver depends on your host OS, environment, and specific requirements. Each driver has its own advantages and limitations, so choose the one that best fits your use case. You can specify the driver using the `--driver` flag when running `minikube start`.

