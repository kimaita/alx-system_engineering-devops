# MySQL

This project aims to get MySQL servers up and running on `web-01` and `web-02`.  
`web-02` will serve as the replica for `web-01`.

We will install MySQL version `5.7.x`, see [here](https://askubuntu.com/a/1199516) for steps used, and allow traffic through `ufw` for port 3306(MySQL default port).

We then create a user on the primary/source/master server for the replication server like:

```sql
CREATE USER 'replica_user'@'%' IDENTIFIED BY 'replica_user_password';
```

This user needs replication permission, which we grant like:

```sql
GRANT REPLICATION SLAVE ON *.* TO 'replica_user'@'%';
```

You can confirm this succeded by running a query like:

```sql
SELECT user, Repl_slave_priv FROM mysql.user WHERE user='replica_user';
```

which should output the below if successfully granted:

```ascii
+--------------+-----------------+
| user         | Repl_slave_priv |
+--------------+-----------------+
| replica_user | Y               |
+--------------+-----------------+
1 row in set (0.00 sec)
```

We can create a test database on the master server using the script [create_table](./create_table.sql) from the `mysql` shell:

```bash
mysql> source /<absolute path to file>/create_table.sql;
```

We also create an empty database on the replica server with the same name:

```SQL
mysql> CREATE DATABASE IF NOT EXISTS tyrell_corp;
```

## MySQL Configuration Files

We now proceed to editing the MySQL configuration file `/etc/mysql/mysql.conf.d/mysqld.cnf` to enable replication.  
See [here](https://www.digitalocean.com/community/tutorials/how-to-set-up-replication-in-mysql) for the full instructions.

### Master/Primary

Edit `/etc/mysql/mysql.conf.d/mysqld.cnf` as below:

1. Remove the `bind-address` option by commenting it out

2. Add/uncomment the `server-id` option, assigning it a unique integer value:  
`server-id       = 1`

3. Add/uncomment the `log_bin` directive:  
    `log_bin         = /var/log/mysql/mysql-bin.log`

4. Add/uncomment the `binlog_do_db` option, assigning it the name of the database to replicate:  
    `binlog_do_db    = tyrell_corp`

That done, restart the MySQL service:

```bash
sudo systemctl restart mysql
```

### Slave/Replica

Edit `/etc/mysql/mysql.conf.d/mysqld.cnf` as below:

1. Add/uncomment the `server-id` option, assigning it a unique, positive integer value:  
`server-id       = 2`

2. Update the `log_bin` and `binlog_do_db` options to match the master/source configuration:  

    ```ascii
    log_bin         = /var/log/mysql/mysql-bin.log
    binlog_do_db    = tyrell_corp
    ```

3. Add the `relay-log` option defining the location of the replica’s relay log file.  
`relay-log      = /var/log/mysql/mysql-relay-bin.log`

That done, restart the MySQL service:

```bash
sudo systemctl restart mysql
```

## Replication

Since we will be using MySQL's **binary log file position-based replication**, we must provide the replica with a set of coordinates that detail the name of the source’s binary log file and a specific position within that file. The replica uses these coordinates to determine the point in the log file from which it should begin copying database events and track which events it has already processed.

To obtain these details from the source server, open the mysql shel and:

1. Close and lock all tables on all databases on the server:

```sql
FLUSH TABLES WITH READ LOCK;
```

2. Get the binary log file current status:

```sql
SHOW MASTER STATUS;
```

which should output:

```ascii
+------------------+----------+--------------+------------------+-------------------+
| File             | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000001 |      588 | tyrell_corp  |                  |                   |
+------------------+----------+--------------+------------------+-------------------+
1 row in set (0.00 sec)
```

### Migrate data

We can migrate any existing data first by performing a dump using `mysqldump` then copying this dump file over to the replica server where we will import it.
On the master/source, replace `tyrell_corp` with the database name and `db.sql` with whatever name you'd like for the dump file:

```bash
sudo mysqldump -u root tyrell_corp > db.sql
```

Send this file over to the replica using `scp`:

```bash
scp db.sql USER@replica_server_ip:/<path to save>
```

Import the dump file contents into the empty database we'd created earlier:

```bash
sudo mysql tyrell_corp < <path to dump file>/db.sql
```

### Enable Replication

On the replica/slave server, open a mysql shell and run the `CHANGE SOURCE` command. This is where we specify the master/source server, the replication user and binary log file details(name, position).  
This command varies with the version of MySQL installed.

MySQL 5.7:

```sql
CHANGE MASTER TO
MASTER_HOST='master_server_ip',
MASTER_USER='replica_user',
MASTER_PASSWORD='replica_user_password',
MASTER_LOG_FILE='mysql-bin.000001',
MASTER_LOG_POS=306;
```

Then activate:

```sql
START SLAVE;
```

MySQL 8.0:

```sql
CHANGE REPLICATION SOURCE TO
SOURCE_HOST='source_server_ip',
SOURCE_USER='replica_user',
SOURCE_PASSWORD='replica_user_password',
SOURCE_LOG_FILE='mysql-bin.000001',
SOURCE_LOG_POS=306;
```

Activate using:

```sql
START REPLICA;
```

You can view the status using:  
MySQL 5.7:

```sql
SHOW SLAVE STATUS\G;
```

MySQL 8.0:

```sql
SHOW REPLICA STATUS\G;
```
