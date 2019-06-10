+++
title = "Create SSH Tunnel To Backup PostgreSQL Database"
date = "2015-08-31"
slug = "2015/08/31/create-ssh-tunnel-to-backup-postgresql-database"
Categories = ["Unix and Linux", "PostgreSQL"]
+++

Today, I was trying to create a backup of production database. The problem is we have two different version of PostgreSQL running on production and these databases can only be accessed from front end(FE) server. We have older version of PostgreSQL client installed in all FE server which means I can't use it to run pg_dump. 

## SSH Tunnel to the rescue

One solution to this problem is to create a SSH tunnel. Since I have the latest version of PostgreSQL client installed in my machine, I can run pg_dump locally which will connect to the database through SSH tunnel.

Here is the command I used to create SSH tunnel:
```bash
# Format: ssh -L <local-port>:<db-hostname>:<db-port> <fe-username>@<fe-hostname>
ssh -L 9000:database.com:5432 ubuntu@production.servers.com
```

After this you can check whether the SSH tunnel is succesfully created by running this and look for port 9000
```bash
netstat -na | grep LISTEN
```

If you confirm that the SSH tunnel is working, you can run psql to connect or pg_dump to backup your database
```bash
psql -h localhost -p 9000
```
