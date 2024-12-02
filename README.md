
# Sharding and Shard Keys in SingleStore

Sharding is a technique used in SingleStore to distribute data across multiple partitions, ensuring scalability, performance, and efficient data management.

---

## **Distributing Data**
- **Image Reference: "Distributing Data"**  
  Data is distributed across leaf nodes using a **shard key**.  
  - The **aggregator** node is responsible for receiving and routing queries to the appropriate **leaf nodes**.  
  - Each leaf contains multiple **partitions**, which store the sharded data.  

---

## **Importance of a Shard Key**
A **shard key** determines how data is distributed across the partitions. Choosing the right shard key is critical to ensure even distribution of data, which minimizes performance bottlenecks.

---

## **Low Skew**
- **Image Reference: "Low Skew"**  
  A well-chosen shard key (e.g., `orderId`) ensures even data distribution across all partitions.  
  - This balances the load, enabling optimal query performance and resource utilization.  
  - Skewed distributions can lead to performance issues by overloading some partitions while underutilizing others.

---

## **Single Partition**
- **Image Reference: "Single Partition"**  
  A poorly chosen shard key (e.g., `customerId` for this dataset) can result in all data being stored in a single partition.  
  - This creates a performance bottleneck as only one partition handles all queries, leaving other partitions idle.

---

## **Setting a Shard Key**
- **Image Reference: "Setting the Shard Key"**  
  When creating a table, the shard key can be specified using the `SHARD KEY` clause:  
  ```sql
  CREATE TABLE order(
      orderId BIGINT,
      customerId BIGINT,
      orderDate DATETIME,
      status VARCHAR(30),
      SHARD KEY(orderId)
  );
  ```
  - In this example, `orderId` is used as the shard key, ensuring even data distribution.

---

## **Key Takeaways**
1. **Shard Key Selection**:
   - A good shard key ensures even data distribution and minimizes skew.
   - Poor shard key choices can lead to uneven load and bottlenecks.
2. **Performance**:
   - Even distribution enables better performance for both queries and data storage.
3. **Flexibility**:
   - Choose shard keys based on the query and data patterns of your application.

---

Let me know if you’d like further adjustments or additions!
