# запускаем контейнер с бд
 
```shell
docker run --name some-mysql  -p 3306:3306  -e MYSQL_ROOT_PASSWORD=root -e MYSQL_USER=user -e MYSQL_PASSWORD=password -e MYSQL_DATABASE=db -d percona:ps-8.0.36-28
```
проверить  
mysqld --verbose --help | grep bind-address
vi etc/my.cnf
# Accept connections from any IP address
bind-address	            = 0.0.0.0

mysql -u root(ЭТО MYSQL_USER) -p
mysql -u root -p
SHOW DATABASES;
SELECT host, user FROM mysql.user;
```shell
docker run --name demo -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=postgres -e POSTGRES_DB=demo -d postgres:11-alpine
```