docker network create proxy

docker-compose up -d

cd ./api

docker-compose up -d

cd ..

docker network inspect proxy
