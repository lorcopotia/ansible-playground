# Repo ansible-playground

This project is based on an Ansible sample exam that you may find here:

https://www.lisenet.com/2019/ansible-sample-exam-for-ex407/

This is just to keep track of my progress with Ansible. 

Feel free to clone it. Enjoy!

## Extras (AAP - Ansible Automation Platform)

Un simple playbook para desplegar un pod en kubernetes utilizando AAP:

```yaml
cat  << EOF > /var/lib/awx/projects/hello/pod.yaml
---
- name: Crea un Pod en Kubernetes utilizando Ansible
  hosts: localhost
  tasks:
  - name: Crea un Pod utilizando Ansible
    kubernetes.core.k8s:
      state: present
      definition:
        apiVersion: v1
        kind: Pod
        metadata:
          name: nginx
          namespace: ansible-automation-platform
        spec:
          containers:
          - name: mi-web
            image: nginx
EOF
```
