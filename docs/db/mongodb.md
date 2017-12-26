# mongodb

# install
https://docs.mongodb.com/master/tutorial/install-mongodb-on-red-hat/


vim /etc/yum.repos.d/mongodb-org-3.4
`
[mongodb-org-3.4]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/3.4/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-3.4.asc
`
# docker install
docker search mongo
docker pull mongo
docker run mongo 。。。。

# 
