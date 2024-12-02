# Database Partitions in SingleStore

## **Default Partitions**

### **What are Partitions?**
Partitions in SingleStore are the fundamental units of data storage and processing. They divide a database's data into smaller segments, distributed across nodes in the cluster to ensure scalability and performance.

### **How Default Partitions Work**
- By default, SingleStore creates **one partition per CPU core** available on each leaf node.
- For example:
  - If a node has **4 CPUs**, and there are **2 nodes**, the database will have a total of **8 partitions** (4 partitions per node).
- Partitions include both:
  - **Primary Partitions**: Actively store data and serve queries.
  - **Replica Partitions**: Provide high availability and fault tolerance by maintaining a synchronized copy of the primary partition.

### **Partition Replication**
- **Reference Partitions** are replicated to every node.
- **Replica Partitions** are created synchronously on paired nodes or load-balanced as needed.

### **Diagram Reference:**
Refer to the "Default Partitions" diagram to visualize the relationship between the master aggregator, child aggregator, and partitions spread across leaf nodes.

---

## **Setting the Number of Partitions**

### **Customizing Partitions**
While the default setup works for many use cases, you can explicitly define the number of partitions during database creation to better suit your workload.

### **Example Command**
To create a database with a specific number of partitions, use the following syntax:
```sql
CREATE DATABASE db_name PARTITIONS = 16;
```
- This command creates **16 partitions** distributed across the nodes in the cluster.
  - If there are **2 nodes**, each node will store **8 partitions**.

### **When to Customize Partitions?**
1. **High Workload Scenarios**:
   - Increase the number of partitions to spread the workload across more nodes and CPUs.
2. **Optimized Query Performance**:
   - By having smaller partitions, query execution can leverage parallelism for better performance.
3. **Balance Data Distribution**:
   - Ensure balanced partitioning for consistent load distribution across nodes.

### **Diagram Reference:**
Refer to the "Setting the Number of Partitions" diagram to see how partitions are distributed when explicitly defined.

---

## **Benefits of Partitioning in SingleStore**
1. **Scalability:**
   - Distributes data and workload across multiple nodes to scale seamlessly.
2. **Parallel Query Execution:**
   - Queries are processed in parallel across partitions, improving performance.
3. **High Availability:**
   - Replica partitions provide fault tolerance and ensure minimal downtime.
4. **Flexible Configuration:**
   - You can adjust the number of partitions to fit specific workload requirements.

---

This document provides an overview of database partitioning in SingleStore, explaining both default behavior and customization options. Proper partitioning ensures that your database performs optimally and scales efficiently with your needs.
