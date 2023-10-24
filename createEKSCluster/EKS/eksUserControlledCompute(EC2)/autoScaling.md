In Amazon Elastic Kubernetes Service (EKS), the load on the nodes (EC2 instances) is typically determined based on the resource utilization of your applications' pods. When the resource utilization, such as CPU and memory, exceeds certain thresholds, the Auto Scaling group associated with your node group can automatically scale to meet the increased demand. Conversely, if resource utilization is consistently low, the Auto Scaling group can scale in to reduce costs.

The key parameters that affect how scaling is performed in a node group include:

1. **Pod Resource Utilization**: The CPU and memory utilization of the containers running in your pods. If these values exceed the specified thresholds, it can trigger scaling actions.

2. **Horizontal Pod Autoscaler (HPA)**: You can configure Horizontal Pod Autoscalers in Kubernetes to automatically adjust the number of pod replicas based on metrics like CPU and memory usage.

3. **Cluster Autoscaler**: The EKS Cluster Autoscaler, when configured, can detect resource constraints and scale the node group to meet the demand. It uses pod resource requests and limits to make scaling decisions.

4. **Auto Scaling Group (ASG) Configuration**: The ASG associated with your node group has scaling policies that specify how and when to scale. These policies are typically based on Amazon CloudWatch metrics like CPU utilization.

5. **Custom Metrics**: You can configure custom CloudWatch metrics based on the specific needs of your applications and use them to trigger scaling actions.

To modify load scaling and behavior, you can adjust the following parameters and configurations:

- **ASG Scaling Policies**: You can modify the scaling policies for your Auto Scaling group to change the thresholds and scaling behavior. For example, you can change the CPU utilization thresholds that trigger scaling actions.

- **HPA Configuration**: You can adjust the HPA settings for your deployments and stateful sets to control how your application pods are auto-scaled based on metrics like CPU and memory utilization.

- **Cluster Autoscaler Configuration**: You can configure the Cluster Autoscaler to respond to certain metrics or policies that match your scaling requirements.

- **Custom Metrics**: If your applications have specific resource metrics that you want to use for scaling, you can configure custom CloudWatch metrics and set up scaling policies based on those metrics.

- **Node Group Capacity Configuration**: When creating your node group, you can specify node capacity settings, such as the instance type and number of nodes, which can impact scaling behavior.

To fine-tune and customize the load-based scaling behavior for your EKS node group, you'll typically work with a combination of Kubernetes configurations, ASG settings, and custom scaling policies based on the specific requirements of your applications and workloads.