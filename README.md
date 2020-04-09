# Try ARGO with Openshift

## Read me to follow

https://github.com/argoproj/argo/blob/master/examples/README.md#hello-world

Steps - 
>Install Argo CLI<br>
>oc login into cluster
>Run argo commands

Note - 
Point to your argo service account in openshift. 
```
spec:
  serviceAccountName: argo
```

Argo CLI Commands
```
argo submit hello-world.yaml    # submit a workflow spec to Kubernetes
argo list                       # list current workflows
argo get hello-world-xxx        # get info about a specific workflow
argo logs -w hello-world-xxx    # get logs from all steps in a workflow
argo logs hello-world-xxx-yyy   # get logs from a specific step in a workflow
argo delete hello-world-xxx     # delete workflow
```
