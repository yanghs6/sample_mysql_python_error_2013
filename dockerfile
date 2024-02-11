FROM mysql/mysql-server:8.0

ADD ./to_container/init.d /docker-entrypoint-initdb.d/
ADD ./to_container/config/my.cnf /etc/my.cnf

ENV TZ=Asia/Seoul \
    MYSQL_ROOT_PASSWORD=root \
    MYSQL_DATABASE=testDB

EXPOSE 3306 33060 33061
