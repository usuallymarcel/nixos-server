docker network create proxy

cd ..

docker-compose up -d

cd build-scripts

docker network inspect proxy
