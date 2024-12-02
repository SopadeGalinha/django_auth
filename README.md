# Managing Upgrades in SingleStore

## Two Approaches to Upgrading

### **Offline Cluster Upgrade**
- The cluster is shut down during the upgrade process.
- SingleStore Tools manage the upgrade using the following command:
  ```bash
  sdb-deploy upgrade
  ```

### **Online Cluster Upgrade**
- The cluster remains operational during the upgrade.
- Requires Redundancy Level 2 for high availability.
- Managed by SingleStore Tools with the following command:
  ```bash
  sdb-deploy upgrade --online
  ```

---

## A Word about "Offline" and "Online"

### **In the Context of Installation:**
- **Online:** Internet connectivity is available.
- **Offline:** No Internet connectivity.

### **In the Context of Upgrades:**
- **Online:** The cluster remains available throughout the upgrade.
- **Offline:** The cluster becomes unavailable at some point during the upgrade.

### **Possible Upgrade Scenarios:**
- **Online/Online:** Internet and cluster are available throughout the process.
- **Online/Offline:** Internet is available, but the cluster is unavailable at some point.
- **Offline/Online:** No Internet, but the cluster remains available throughout the process.
- **Offline/Offline:** No Internet, and the cluster becomes unavailable at some point.

---

## Upgrade Health Check

Before performing any upgrade, run a health check to ensure cluster readiness:

```bash
sdb-deploy upgrade --precheck-only
```

### This command performs the following:
1. Checks the current version.
2. Verifies cluster health:
   - All nodes are online and healthy.
   - All partitions are healthy.
3. Identifies any pending rebalance operations.
4. Takes snapshots of all databases for safety.

---

## Upgrade Scenarios

| Type of Upgrade       | SingleStore Tools Command                          |
|-----------------------|---------------------------------------------------|
| **Online/Online**     | `sdb-admin upgrade --version x.y.z --yes --online`|
| **Online/Offline**    | `sdb-admin upgrade --version x.y.z --yes`         |
| **Offline/Online**    | `sdb-admin upgrade --file-path <path> --yes --online` |
| **Offline/Offline**   | `sdb-admin upgrade --file-path <path> --yes`      |

### Explanation of Parameters:
- `--version`: Specifies the SingleStore Server version to upgrade to (x=major, y=minor, z=patch).
- `--file-path`: Absolute path to the upgrade package.
- `--yes`: Performs an unattended installation.
- `--online`: Indicates that the cluster should remain operational during the upgrade.

---

## Offline Upgrade Process

1. **Health Checks**:
   - Ensure all nodes and partitions are healthy.
   - Confirm no pending rebalance operations.
2. **Snapshot Databases**:
   - Take a snapshot of all databases before proceeding.
3. **Update Node Configuration**:
   - Apply necessary changes to node configurations.
4. **Restart the Cluster**:
   - The entire cluster is taken offline and restarted.
5. **Snapshot Databases Again**:
   - After restarting, take a new snapshot to confirm data integrity.

---

## Online Upgrade Process

1. The cluster remains operational during the upgrade.
2. **Master Aggregator** manages the overall process.
3. **Child Aggregators** assist in distributing the upgrade workload.
4. **Leaf Nodes** are upgraded sequentially to ensure minimal disruption.

---

## Upgrading SingleStore Tools, Studio, & Client

### **Online (Debian Hosts):**
```bash
sudo apt update
sudo apt install singlestoredb-studio singlestoredb-toolbox singlestore-client
```

### **Online (RHEL Hosts):**
```bash
sudo yum install singlestoredb-studio singlestoredb-toolbox singlestore-client
```

### **Offline:**
1. Download the appropriate packages for your hosts (.deb, .rpm).
2. Copy them to your hosts.
3. Install them using `dpkg` or `rpm`.
4. Refer to the SingleStore documentation for more details.

---

This document summarizes the key processes and commands for managing upgrades in SingleStore. Proper preparation and understanding of the upgrade scenarios ensure a smooth and efficient upgrade process.

