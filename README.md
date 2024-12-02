Based on the additional images provided, I’ve added more content to expand the document on **Database Partitions in SingleStore**. Here’s the updated structure with these new topics:

---

# Database Partitions in SingleStore

## Default Partitions
- **Default Setup**: SingleStore assigns one partition per CPU by default.
- **Reference Partition**:
  - Contains metadata and small datasets replicated to every node.
- **Replica Partitions**:
  - Ensure fault tolerance and load balancing.
  - Created synchronously across paired nodes.

*Image Reference: Fits with "Default Partitions."*

---

## Setting the Number of Partitions
- Customize partitions during database creation to suit workload requirements.
- Example command:
  ```sql
  CREATE DATABASE db_name PARTITIONS=16;
  ```
  - **16 partitions** distributed across nodes, ensuring balanced processing.

*Image Reference: Fits with "Setting the Number of Partitions."*

---

## Query Performance and Partitions

### Single Query — 1 Partition/Core
- A single query leverages one partition per core.
- Efficient for workloads with fewer concurrent queries but higher resource demands per query.

*Image Reference: Fits with "Single Query — 1 Partition/Core."*

---

### Single Query — 4 Partitions/Core
- With 4 partitions per core, SingleStore incurs **latency from partition switching** during query execution.
- This setup is better suited for scenarios requiring higher data concurrency but may affect single-query performance.

*Image Reference: Fits with "Single Query — 4 Partitions/Core."*

---

### Multiple Queries — 1 Partition/4 Cores
- Designed for concurrent query execution:
  - Each query uses its own partition, sharing CPU cores among them.
- Optimizes system utilization for high-concurrency environments.

*Image Reference: Fits with "Multiple Queries — 1 Partition/4 Cores."*

---

### Single Query — 1 Partition/4 Cores
- Allocates all CPU resources for a single query on one partition.
- Ideal for low-concurrency workloads with high resource demands per query.

*Image Reference: Fits with "Single Query — 1 Partition/4 Cores."*

---

## Flexible Parallelism
- Enables a single query to execute across multiple partitions.
- Significantly boosts performance for data-intensive workloads by leveraging all available CPU cores.

*Image Reference: Fits with "Flexible Parallelism."*

---

## Partition Affinity
- Ensures that a query operates on a specific partition.
- **Limitation**: Reduces parallelism by restricting the query to fewer resources.

*Image Reference: Fits with "Partition Affinity."*

---

## Cluster Expansion
- Partitions are automatically rebalanced when new nodes are added to the cluster.
- Ensures that workloads remain evenly distributed across all nodes for scalability.

*Image Reference: Fits with "Cluster Expansion."*

---

## Column Segments
- **Definition**: Basic storage unit in SingleStore, consisting of up to **1,024,000 rows by default**.
- **Key Features**:
  - Sorted on a designated sort key.
  - Metadata includes the maximum and minimum values for fast query filtering.
- Use smaller column segments for more granular filtering or larger ones for compression.

*Image Reference: Fits with "Column Segments."*

---

## How Many Records per Segment
- Configure the size of column segments to optimize for performance:
  ```sql
  SET GLOBAL columnstore_segment_rows=n;
  CREATE TABLE my_table (... SORT KEY(id) WITH (columnstore_segment_rows=n));
  ```
  - **Smaller Segments**:
    - Faster filtering with more segment elimination.
  - **Larger Segments**:
    - Greater compression and reduced disk usage.

*Image Reference: Fits with "How Many Records per Segment."*

---

## Summary of Partition Benefits
1. **Scalability**: Partitions allow datasets to be split across multiple nodes.
2. **Parallel Processing**: Enables faster query execution.
3. **Fault Tolerance**: Replica partitions ensure data availability in case of node failure.
4. **Customizability**: Flexible partition settings accommodate diverse workloads.

---

Would you like to add anything else or adjust specific sections?
