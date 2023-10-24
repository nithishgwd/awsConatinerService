A Headless Service is a special type of Kubernetes service that is used when you don't need or want load balancing or a stable virtual IP (ClusterIP) for your service. In a Headless Service, there is no ClusterIP, and DNS resolution for the service name returns the individual IP addresses of the pods selected by the service. 

Key characteristics of Headless Services:

1. **No ClusterIP:** A Headless Service does not have a ClusterIP, which means it doesn't create a stable virtual IP address for the service.

2. **DNS-Based Service Discovery:** When you perform DNS queries for the service name, you receive a list of IP addresses of the pods selected by the service. This allows direct communication with individual pods.

3. **Use Cases:** Headless Services are useful for stateful applications, such as databases, where you need to address specific pods directly without load balancing, or for scenarios where you want to maintain full control over network traffic.

4. **Stable Pod DNS Names:** When a Headless Service is created, it also ensures that pods targeted by the service are given DNS entries in the form of `<pod-name>.<service-name>.<namespace>.svc.cluster.local`.

Example of a Headless Service:

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-headless-service
spec:
  clusterIP: None
  selector:
    app: my-app
  ports:
    - protocol: TCP
      port: 80
```

In this example, we define a Headless Service named "my-headless-service" with no ClusterIP. It selects pods with the label `app: my-app` and exposes them without load balancing on port 80. DNS queries for "my-headless-service" will return the individual IP addresses of the selected pods.